"""PDF password auditor — generates targeted wordlists from personal info and tests encrypted PDFs."""

import pypdf


def make_wordlist(name: str, mobile: str, dob: str) -> list[str]:
    name = name.strip()
    mobile = mobile.strip()
    dob = dob.strip()

    first3 = name[:3]
    first4 = name[:4]
    year = dob[-4:]      # YYYY from MMDDYYYY
    month = dob[:2]
    day = dob[2:4]
    last4mobile = mobile[-4:]
    first4mobile = mobile[:4]

    passwords = {
        # Original patterns
        first3 + first4mobile,
        first4 + first4mobile,
        first4 + "@" + first4mobile,
        first3 + year,
        first4 + year,
        first3 + "@" + year,
        first4 + "@" + year,
        name[(len(name) - 1) // 2] + first4mobile,
        name[len(name) // 2] + first4mobile,

        # Capitalization
        first4.upper() + year,
        first4.capitalize() + year,
        first4.lower() + year,

        # With symbols
        first4.upper() + "@" + year,
        first4.capitalize() + "@" + year,
        first4 + "#" + year,
        first4 + "_" + year,
        first4 + "." + year,

        # Common numeric suffixes
        first4 + "123",
        first4 + "1234",
        first4 + "12345",
        first4 + "2024",
        first4 + "2025",
        first4 + "2026",

        # Birth date combinations
        first4 + month + day,
        first4 + day + month,
        first4 + dob,
        first4 + "@" + dob,

        # Mobile combinations
        first4 + last4mobile,
        first4.upper() + last4mobile,
        first4.capitalize() + last4mobile,
        first4 + "@" + last4mobile,

        # Mixed patterns
        first4.upper() + year + "!",
        first4.capitalize() + "123",
        first4 + "@" + "123",
        first4 + "#" + "123",
        first4 + "_" + "123",

        # Reversed name
        first4[::-1] + year,
        first4[::-1] + first4mobile,
    }

    return list(passwords)


def crack_pdf(pdf_path: str, wordlist: list[str]) -> str | None:
    """Try each password until one succeeds."""

    try:
        pdf = pypdf.PdfReader(pdf_path)
    except Exception as e:
        print(f"Could not open PDF: {e}")
        return None

    if not pdf.is_encrypted:
        print("This PDF is not encrypted.")
        return None

    total = len(wordlist)

    for i, password in enumerate(wordlist, start=1):
        print(f"[{i}/{total}] Trying: {password}")

        try:
            result = pdf.decrypt(password)

            if result:
                print(f"\nPassword found: {password}")
                return password

        except Exception:
            continue

    print("\nPassword not found in generated wordlist.")
    return None


def main():
    print("=" * 40)
    print("      PDF Password Wordlist Tester")
    print("=" * 40)

    pdf_path = input("PDF path: ").strip()
    name = input("Name: ").strip()
    mobile = input("Mobile Number: ").strip()
    dob = input("DOB (MMDDYYYY): ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if len(mobile) != 10 or not mobile.isdigit():
        print("Invalid mobile number.")
        return

    if len(dob) != 8 or not dob.isdigit():
        print("DOB should be in MMDDYYYY format.")
        return

    wordlist = make_wordlist(name, mobile, dob)

    print(f"\nGenerated {len(wordlist)} unique passwords.\n")

    crack_pdf(pdf_path, wordlist)


if __name__ == "__main__":
    main()