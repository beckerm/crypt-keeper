#!/usr/bin/env python3

from cryptography.fernet import Fernet
import argparse
import os


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

    if os.path.exists(k):

        try:
            with open(k, 'rb') as filekey:
                key = filekey.read()
        except Exception as e:
            print(f"Error: {e}")
            exit()

        fernet = Fernet(key)

        try:
            with open(f, 'rb') as file:
                original = file.read()
        except Exception as e:
            print(f"Error: {e}")
            exit()

        encrypted = fernet.encrypt(original)

        try:
            with open(f, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        except Exception as e:
            print(f"Error: {e}")
            exit()

    else:
        print(f"Error: Key file '{k}' not found.")


def decrypt_file(f, k):

    if os.path.exists(k):

        try:
            with open(k, 'rb') as filekey:
                key = filekey.read()
        except Exception as e:
            print(f"Error: {e}")
            exit()

        fernet = Fernet(key)

        try:
            with open(f, 'rb') as encrypted_file:
                encrypted = encrypted_file.read()
        except Exception as e:
            print(f"Error: {e}")
            exit()

        decrypted = fernet.decrypt(encrypted)

        try:
            with open(f, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
        except Exception as e:
            print(f"Error: {e}")
            exit()

    else:
        print(f"Error: Key file '{k}' not found.")



if __name__ == "__main__":

    if args.makekey:
        create_key(args.makekey)
    elif args.encrypt and args.key:
        encrypt_file(args.encrypt, args.key)
    elif args.decrypt and args.key:
        decrypt_file(args.decrypt, args.key)
    else:
        exit()
