# Cyber Utils

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

A collection of small cybersecurity utilities built with Python — designed for learning, lab practice, and authorized security testing.

Each tool is self-contained, minimal, and focused on a single task: scanning, hashing, cracking, or auditing.

---

## Tools

| Tool | Description |
|------|-------------|
| [`port_scanner.py`](port_scanner.py) | TCP connect port scanner — scan a target IP or hostname across a port range. |
| [`hash_cracker.py`](hash_cracker.py) | Hash identifier and cracker — auto-detects algorithm by hash length and cracks against a wordlist. |
| [`hasher.py`](hasher.py) | Password hasher — generate MD5, SHA1, SHA224, SHA256, SHA384, or SHA512 hashes. |
| [`pdf_cracker.py`](pdf_cracker.py) | PDF password auditor — generates targeted wordlists from personal info and tests encrypted PDFs. |

---

## Installation

```bash
git clone https://github.com/Utkarsh464/cyber-utils.git
cd cyber-utils
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

---

## Requirements

- Python 3.8+
- [`pypdf`](https://pypi.org/project/pypdf/) — for PDF cracking (included in `requirements.txt`)

All other tools use only the Python standard library.

---

## Disclaimer

These tools are provided **for educational and authorized testing purposes only**. Unauthorized use of security tools against systems you do not own or have explicit permission to test is illegal. The author is not responsible for any misuse of these tools.

---

## License

Licensed under the [MIT License](LICENSE).

---

**Utkarsh Solanki** — Cybersecurity & AI Student
[LinkedIn](https://linkedin.com/in/utkarsh-solanki-337806252) · [GitHub](https://github.com/Utkarsh464)
