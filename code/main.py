#!/usr/bin/env python3

from backend.iostream import IOStream
import sys

messager = IOStream()

def main(*args, **kwargs) -> None:
    if 'put' in sys.argv:
        messager.put(input('Enter your message:\n'))
    elif 'get' in sys.argv:
        messager.get()
    else:
        string = ''
        while string not in ['put', 'get']:
            string = input('What you want do? [put/get] ').lower()

        if string == 'get':
            messager.get()
        else:
            messager.put(input('Enter your message:\n'))

if __name__ == '__main__':
    main()