import argparse
from cryptography_operations import base64_operations

def main():
    print("Cheguei na função")
    parser = argparse.ArgumentParser(description="Crypto Tool CLI")
    subparsers = parser.add_subparsers(dest="command", help="Choose a command")

    base64_parser = subparsers.add_parser("base64", help="Base64 encoding/decoding operations")
    base64_parser.add_argument("--encode", action="store_true", help="Encode using Base64")
    base64_parser.add_argument("--decode", action="store_true", help="Decode using Base64")

    args = parser.parse_args()

    if args.command == "base64":
        if args.encode:
            data_to_encode = "String"
            encoded_data = base64_operations.calculate_base64(data_to_encode.encode('utf-8'))
            print("Encoded Base64:", encoded_data)
        elif args.decode:
            base64_encoded_data = "Base64"
            decoded_data = base64_operations.decode_base64(base64_encoded_data)
            print("Decoded Data:", decoded_data.decode('utf-8'))
    