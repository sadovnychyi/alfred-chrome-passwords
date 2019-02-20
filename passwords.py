import argparse
import base64
import codecs
import fuzzywuzzy.process
import json
import os
import sqlite3
import sys
import tempfile
try:
  from urlparse import urlparse
except ImportError:
  from urllib.parse import urlparse

HOME = os.path.expanduser('~')
CHROME = 'Library/Application Support/Google/Chrome'
PROFILE = 'Default'
LOGIN_DATA = 'Login Data'


def main(query, profile):
  with tempfile.NamedTemporaryFile() as tmp:
    with open(os.path.join(HOME, CHROME, profile, LOGIN_DATA), 'rb') as f:
      tmp.write(f.read())
    cursor = sqlite3.connect(tmp.name).cursor()
    cursor.execute('''SELECT origin_url, username_value, password_value
                      FROM logins ORDER BY times_used desc''')
    passwords = []
    for origin_url, account, password in cursor.fetchall():
      password = base64.b64encode(password[3:]).decode('utf8')
      url = urlparse(origin_url)
      title = codecs.decode(url.netloc.encode('utf8'), 'idna')
      if title.lower().startswith('www.'):
        title = title[4:]
      if url.scheme == 'android':
        title = '%s://%s' % (url.scheme, title.split('@')[1])
      passwords.append({
        'type': 'default',
        'title': title,
        'subtitle': account,
        'arg': password,
        'valid': 'true' if len(password) > 0 else 'false',
        'autocomplete': title,
      })
  passwords = fuzzywuzzy.process.extractBests(
    query, passwords, processor=lambda x: '%s %s' % (
      x['title'], x['subtitle']) if isinstance(x, dict) else x)
  json.dump({'items': [p[0] for p in passwords]}, sys.stdout, indent=2)
  sys.stdout.flush()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--query', default='')
  parser.add_argument('--profile', default=PROFILE)
  args = parser.parse_args()
  main(args.query, args.profile)
