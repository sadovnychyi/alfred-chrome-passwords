import base64
from Crypto.Cipher import AES
import hashlib
import subprocess
import sys


def main(password):
  master_password = subprocess.check_output([
    '/usr/bin/security', 'find-generic-password', '-w', '-s',
    'Chrome Safe Storage', '-a', 'Chrome']).strip()
  key = hashlib.pbkdf2_hmac(hash_name='sha1', password=master_password,
                            salt=b'saltysalt', iterations=1003, dklen=16)
  cipher = AES.new(key, AES.MODE_CBC, IV=b' ' * 16)
  data = cipher.decrypt(base64.b64decode(password))
  try:
    s = ''.join([chr(i) for i in data if i >= 32])
  except TypeError:
    s = ''.join([i for i in data if ord(i) >= 32])
  return sys.stdout.write(s)


if __name__ == '__main__':
  main(sys.argv[1] if len(sys.argv) > 1 else '')
