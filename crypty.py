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

    try:
        with open(k, 'rb') as filekey:
            key = filekey.read()
    except Exception as e:
        print(str(e))
        exit(1)

    fernet = Fernet(key)

    try:
        with open(f, 'rb') as file:
            original = file.read()
    except Exception as e:
        print(str(e))
        exit(1)

    encrypted = fernet.encrypt(original)

    try:
        with open(f, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    except Exception as e:
        print(str(e))
        exit(1)


def decrypt_file(f, k):

    try:
        with open(k, 'rb') as filekey:
            key = filekey.read()
    except Exception as e:
        print(str(e))
        exit(1)

    fernet = Fernet(key)

    try:
        with open(f, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
    except Exception as e:
        print(str(e))
        exit(1)

    decrypted = fernet.decrypt(encrypted)

    try:
        with open(f, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
    except Exception as e:
        print(str(e))
        exit(1)


if args.makekey:
    create_key(args.makekey)
    exit(1)

if args.encrypt and args.key:
    encrypt_file(args.encrypt, args.key)
    exit(1)

if args.decrypt and args.key:
    decrypt_file(args.decrypt, args.key)
    exit(1)
