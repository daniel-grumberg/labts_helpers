#!/usr/local/bin/python3

import argparse
from cryptography.fernet import Fernet

def decrypt(credentials_file, key_file):
    credentials = b''
    key = b''
    with open(credentials_file, 'rb') as cf:
        credentials = cf.read(-1)

    with open(key_file, 'rb') as kf:
        key = kf.read(-1)

    f = Fernet(key)
    byte_str = f.decrypt(credentials)
    return byte_str.decode('utf-8')

def main(args):
    token_str = args.username + '\n' + args.password
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(token_str.encode('utf-8'))
    with open(args.output, 'w+b') as out_file:
        out_file.write(token)

    with open(args.key, 'w+b') as key_file:
        key_file.write(key)

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    arg_parser.add_argument('username',
            help='''Your DoC username''')
    arg_parser.add_argument('password',
            help='''Your DoC password''')
    arg_parser.add_argument('-o', '--output',
            default='./.credentials.bin',
            help='''The file where to store your encrypted credentials''')
    arg_parser.add_argument('-k', '--key',
            default='./.key.bin',
            help='''The file to store your secret key in''')
    args = arg_parser.parse_args()
    main(args)

