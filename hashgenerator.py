from ast import parse
from asyncio.windows_events import NULL
import sys

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('text to hash', font='starwars'), 'yellow', attrs=['bold'])

import hashlib
import argparse

def main(text, hashType):
    encoder = text.encode('utf_8')
    myHash = NULL

    if hashType.lower() == 'md5':
        myHash = hashlib.md5(encoder).hexdigest()
    elif hashType.lower() == 'sha1':
        myHash = hashlib.sha1(encoder).hexdigest()
    elif hashType.lower() == 'sha224':
        myHash = hashlib.sha224(encoder).hexdigest()
    elif hashType.lower() == 'sha256':
        myHash = hashlib.sha256(encoder).hexdigest()
    elif hashType.lower() == 'sha384':
        myHash = hashlib.sha384(encoder).hexdigest()
    elif hashType.lower() == 'sha512':
        myHash = hashlib.sha512(encoder).hexdigest()
    else:
        print('[!][!][!] Your input does not support this format [!][!][!]')
        exit(0)
    print("Your hash has been generated:", myHash)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='text to hash')
    parser.add_argument('-t', '--text', dest='text', required=True)
    parser.add_argument('-T', '--Type', dest='hash', required=True)
    args = parser.parse_args()

    txt = args.text
    hType = args.hash
    main(txt, hType)