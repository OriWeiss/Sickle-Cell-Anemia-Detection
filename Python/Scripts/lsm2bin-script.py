#!C:\Users\oweiss\Desktop\code\Sickle_Cell\Python\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tifffile==2020.5.11','console_scripts','lsm2bin'
__requires__ = 'tifffile==2020.5.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tifffile==2020.5.11', 'console_scripts', 'lsm2bin')()
    )
