import getpass

MIN_LENGTH = 8       # below this = immediate fail (per the policy slide)
STRONG_LENGTH = 12   # needed for a "Strong" rating

# Tiny sample list. For the bonus, load a bigger one from a file.
COMMON_PASSWORDS = {
    "password", "password1", "123456", "12345678", "qwerty",
    "abc123", "admin", "letmein", "welcome", "iloveyou",
}


def check_password(password):
    """Return (rating, list_of_tips)."""
    # Rule 1: length gate
    if len(password) < MIN_LENGTH:
        return "Weak", [f"Use at least {MIN_LENGTH} characters."]

    # Rule 2: common password gate
    if password.lower() in COMMON_PASSWORDS:
        return "Weak", ["This is a very common password. Pick something unique."]

    # Rule 3: character variety (any() stops at the first match)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    tips = []
    if not has_upper:
        tips.append("Add an uppercase letter.")
    if not has_digit:
        tips.append("Add a number.")
    if not has_symbol:
        tips.append("Add a symbol (e.g. ! @ # $).")
    if len(password) < STRONG_LENGTH:
        tips.append(f"Use {STRONG_LENGTH}+ characters for a stronger password.")

    types_met = sum([has_upper, has_digit, has_symbol])

    if types_met == 3 and len(password) >= STRONG_LENGTH:
        rating = "Strong"
    elif types_met >= 2:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, tips


def main():
    # getpass hides the input so it isn't shown on screen
    password = getpass.getpass("Enter password: ")
    rating, tips = check_password(password)

    print(f"\nPassword strength: {rating}")
    for tip in tips:
        print(f"  - {tip}")


if __name__ == "__main__":
    main()
