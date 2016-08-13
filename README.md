# Alfred Chrome Passwords

Browse your passwords saved in Google Chrome using Alfred instead of https://password.google.com.

# Demo

![sample](https://cloud.githubusercontent.com/assets/193864/17643019/7d16b81c-618f-11e6-824a-784b678a4f50.gif)

# Installation

See [releases](https://github.com/sadovnychyi/alfred-chrome-passwords/releases)
to download latest build. Simply open it with Alfred and follow instructions.

# Usage

Type `password` keyword to see the most frequent passwords you have used.
Continue typing to filter them and press `Enter` to copy it. Note that by
default you will be required to type your OS password to decrypt selected
password.

# Using non-default profile

Provide `--profile` argument to `passwords.py` script. For example:
```bash
python passwords.py --query="$1" --profile="Profile 1"
```
![image](https://cloud.githubusercontent.com/assets/193864/17643119/9ac8a2d2-6192-11e6-9763-b53ad6769a1c.png)

# Security

Chrome stores all your passwords inside of sqlite database named `Login Data`.
All passwords are securely encrypted by a master password which is stored in
your keychain. By default you have to use your OS password to access Chrome's
safe storage password. If you feel super safe allowing anybody who has physical
access to your Mac to access your passwords – you can remove that confirmation
window. To do so, open `Keychain Access`, search for `Chrome Safe Storage`, go
to `Access Control` and select `Allow all applications to access this item`. But... just don't!

![image](https://cloud.githubusercontent.com/assets/193864/17643070/0f400788-6191-11e6-9c6e-02a0d411a05c.png)
