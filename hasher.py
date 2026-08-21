"""Password hasher — generate MD5, SHA1, SHA224, SHA256, SHA384, or SHA512 hashes."""

import argparse
import hashlib

algos = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
}


def hasher(algo, password):
    return algo(password.strip().encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Password hasher")
    parser.add_argument("password", help="password to hash")
    parser.add_argument(
        "--algo",
        choices=["md5", "sha1", "sha224", "sha256", "sha384", "sha512"],
        default="sha256",
        help="hash algorithm",
    )
    args = parser.parse_args()

    func = algos.get(args.algo)
    if func is None:
        print("unknown algo")
    else:
        print(hasher(func, args.password))


if __name__ == "__main__":
    main()
