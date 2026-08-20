# Pentools

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)

Small cybersecurity utilities I built while learning — port scanning, hash cracking, password auditing, PDF protection testing, and blind SQLi extraction. Each tool is self-contained and focused on one thing, written to understand security concepts by coding them myself.

Designed for learning, lab practice, and authorized security testing only.

---

## Tools

| Tool                                                 | Description                                                                                                             |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [`port_scanner.py`](port_scanner.py)                 | TCP connect port scanner — scan a target IP or hostname across a port range.                                            |
| [`hash_cracker.py`](hash_cracker.py)                 | Hash identifier and cracker — auto-detects algorithm by hash length and cracks against a wordlist.                      |
| [`hasher.py`](hasher.py)                             | Password hasher — generate MD5, SHA1, SHA224, SHA256, SHA384, or SHA512 hashes.                                         |
| [`pdf_cracker.py`](pdf_cracker.py)                   | PDF password auditor — generates targeted wordlists from personal info and tests encrypted PDFs.                        |
| [`blind_sqli_extractor.py`](blind_sqli_extractor.py) | Blind SQL injection password extractor — Oracle conditional-error oracle (`TO_CHAR(1/0)`) with char-by-char extraction. |

---

## Installation

```bash
git clone https://github.com/Utkarsh464/pentools.git
cd pentools
pip install -r requirements.txt
```

## Usage

### Port Scanner

```bash
python port_scanner.py
# enter target ip or hostname: 192.168.1.1
# start port: 1
# end port: 1024
```

### Hash Cracker

```bash
python hash_cracker.py
# enter the hash path: hashes.txt
# enter wordlist path: wordlist.txt
```

### Hasher

```bash
python hasher.py
# enter the password: mysecret
# choose algo (md5/sha1/sha224/sha256/sha384/sha512): sha256
```

### PDF Cracker

```bash
python pdf_cracker.py
# PDF path: protected.pdf
# Name: John
# Mobile Number: 1234567890
# DOB (MMDDYYYY): 01011990
```

### Blind SQLi

```bash
python blind_sqli_extractor.py
# Lab URL: https://0a1b2c...web-security-academy.net/
# Session cookie value: ...
# TrackingId cookie value: ...
```

Solves PortSwigger's _Blind SQL injection with conditional errors_ lab on an Oracle backend by asking the app yes/no questions ("is this character correct?") and reading the answer from the HTTP status code (500 = TRUE, 200 = FALSE). Uses `requests`.

Written alongside my [PortSwigger Academy lab writeups](https://github.com/Utkarsh464/portswigger-academy) — see the [Blind SQL injection with conditional errors](https://github.com/Utkarsh464/portswigger-academy/blob/main/SQL%20Injection/13%20-%20Blind%20SQL%20injection%20with%20conditional%20errors/README.md) writeup for the walkthrough this tool automates.

---

## Requirements

- Python 3.10+
- [`pypdf`](https://pypi.org/project/pypdf/) — for PDF cracking (included in `requirements.txt`)
- [`requests`](https://pypi.org/project/requests/) — for `blind_sqli_extractor.py` (included in `requirements.txt`)

All other tools use only the Python standard library.

---

## Disclaimer

These tools are provided **for educational and authorized testing purposes only**. Unauthorized use of security tools against systems you do not own or have explicit permission to test is illegal. The author is not responsible for any misuse of these tools.

---

## License

Licensed under the [MIT License](LICENSE).

---

**Utkarsh Solanki** — Cybersecurity Student
[LinkedIn](https://linkedin.com/in/utkarsh-solanki-337806252) · [GitHub](https://github.com/Utkarsh464)

---

## Limitations

- The blind SQLi extractor uses a lowercase-only charset and caps password length at 99 characters.
- HTTP requests in the blind SQLi extractor have no timeout set.
