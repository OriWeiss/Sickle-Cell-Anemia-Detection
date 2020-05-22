#!C:\Users\oweiss\Desktop\code\Sickle_Cell\Python\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'scikit-image==0.17.2','console_scripts','skivi'
__requires__ = 'scikit-image==0.17.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('scikit-image==0.17.2', 'console_scripts', 'skivi')()
    )
