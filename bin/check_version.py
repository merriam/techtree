# python 3

# A little program to check if there are later versions of packages I rely upon.
# This may grow into a full fledged service, but not today.

import subprocess
import re

def curl_match(url, regex):
    out = subprocess.check_output(
        ['curl', '--silent', url])
    num = re.search(regex, out).group(1)  # may toss exception
    return num

def check_version(name, version, url, regex):
    print(name, end =" ")
    try:
       num = curl_match(url, regex)
       if num == version:
           print("is current(", version, ")")
           return True
       else:
           print("is out date.  Expected", version,
                "but current version is", num.decode('utf-8'))
    except (OSError, IndexError, subprocess.CalledProcessError):
       print("cannot be verified at url", url, " with matching", regex)
    return False

checks = [ ("VirtualBox", b"4.3.6",
        'https://www.virtualbox.org/wiki/Downloads',
        b'OS X.*/virtualbox/(\d\.\d\.\d)/'),
           ("Docker", b"0.8.0",
        'https://raw.github.com/dotcloud/docker/release/VERSION',
        b'(\d.\d.\d)') ]

exit_code = 0
for check in checks:
    if not check_version(*check):
        exit_code = 1
exit(exit_code)
