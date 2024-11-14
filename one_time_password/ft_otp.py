import argparse
import struct
import binascii
import hmac
import time
from cryptography.fernet import Fernet
import hashlib


def encrypt_key(key: str, password: bytes) -> bytes:
    fernet = Fernet(password)
    encrypted = fernet.encrypt(key.encode())
    return encrypted


def decrypt_key(encrypted_key: bytes, password: bytes) -> str:
    fernet = Fernet(password)
    decrypted = fernet.decrypt(encrypted_key)
    return decrypted.decode()


def parse_args():
    parser = argparse.ArgumentParser(
        description="TOTP program to generate and verify OTPs.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-g", "--generate", type=str,
                       help="Path to the file containing a hexadecimal key")
    group.add_argument("-k", "--key", type=str,
                       help="Key file for OTP verification")
    return parser.parse_args()


def hotp(key: str, counter: int) -> str:
    # Convert hex key to bytes
    key_bytes = binascii.unhexlify(key)

    # Create HMAC-SHA-1 hash
    counter_bytes = struct.pack('>Q', counter)
    hmac_hash = hmac.new(key_bytes, counter_bytes, hashlib.sha1).digest()

    # Dynamic truncation to get a 31-bit number
    offset = hmac_hash[-1] & 0x0F
    binary = (hmac_hash[offset] << 24) | (hmac_hash[offset + 1] <<
                                          16) | (hmac_hash[offset + 2] << 8) | hmac_hash[offset + 3]

    # Generate OTP
    otp = binary % 10**6  # Get a 6-digit OTP
    return f"{otp:06d}"  # Format with leading zeros


def main():
    args = parse_args()
    if args.generate:
        # print(args.generate)
        with open(args.generate, 'r') as f:
            key = f.read().strip()
        if len(key) != 64 or not all(c in '0123456789abcdefABCDEF' for c in key):
            print("./ft_otp: error: key must be 64 hexadecimal characters.")
            return
        password = Fernet.generate_key()
        encrypted_key = encrypt_key(key, password)
        with open('ft_otp.key', 'wb') as f:
            f.write(encrypted_key + b'\n' + password)
        print("Key successfully saved in 'ft_otp.key'.")
        # encrypt_and_store_key(args.generate)
    else:
        with open('ft_otp.key', 'rb') as f:
            data = f.readlines()
            encrypted_key = data[0].strip()
            password = data[1].strip()

        key = decrypt_key(encrypted_key, password)
        time_step = 30  # Time step in seconds
        counter = int(time.time() // time_step)
        otp = hotp(key, counter)
        print(otp)


if __name__ == "__main__":
    main()
