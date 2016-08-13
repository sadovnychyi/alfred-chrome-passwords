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
  return sys.stdout.write(cipher.decrypt(password.decode('base64')))


if __name__ == '__main__':
  main(sys.argv[1] if len(sys.argv) > 1 else '')
