#!C:\Users\oweiss\Desktop\code\Sickle_Cell\Python\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'imagecodecs==2020.2.18','console_scripts','imagecodecs'
__requires__ = 'imagecodecs==2020.2.18'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('imagecodecs==2020.2.18', 'console_scripts', 'imagecodecs')()
    )
