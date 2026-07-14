"""Hash identifier and cracker — auto-detects algorithm by hash length and cracks against a wordlist."""

import hashlib

algos = {
    32: hashlib.md5,
    40: hashlib.sha1,
    56: hashlib.sha224,
    64: hashlib.sha256,
    96: hashlib.sha384,
    128: hashlib.sha512,
}

def crack_hash(targets, wordlist):
    with open(targets, "r", errors="ignore") as t:
        for target in t:
            target = target.strip()
            if not target:
                continue
            algo = algos.get(len(target))
            if algo is None:
                print("unknown hash:", target)
                continue
            with open(wordlist, "r", errors="ignore") as f:
                for line in f:
                    if target == algo(line.strip().encode()).hexdigest():
                        print("found", target, "=", line.strip())
                        break
                else:
                    print("not found:", target)

x = input("enter the hash path :")
w = input("enter wordlist path :")
crack_hash(x, w)
