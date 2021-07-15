#!/usr/bin/env python3

from cryptography.fernet import Fernet
import argparse


parser = argparse.ArgumentParser(description='Encrypt and decrypt files.')

parser.add_argument('-e', '--encrypt', help='Encrypt file')
parser.add_argument('-d', '--decrypt', help='Decrypt file')
parser.add_argument('-k', '--key', help='Encyption key')
parser.add_argument('-m', '--makekey', help='Make encyption key')


args = parser.parse_args()


def create_key(n):

    key = Fernet.generate_key()

    with open(n, 'wb') as filekey:
        filekey.write(key)


def encrypt_file(f, k):
    with open(k, 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(f, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(f, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt_file(f, k):

    with open(k, 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(f, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(f, 'wb') as dec_file:
        dec_file.write(decrypted)


if args.makekey:
    create_key(args.makekey)
    exit(1)

if args.encrypt and args.key:
    encrypt_file(args.encrypt, args.key)
    exit(1)

if args.decrypt and args.key:
    decrypt_file(args.decrypt, args.key)
    exit(1)
