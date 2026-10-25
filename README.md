# Password Strength Checker

A small command-line tool written in Python that rates a password as Weak, Medium or Strong and tells you what to fix. I built it as Project 1 of the DecodeLabs Cyber Security Industrial Training Kit (Batch 2026).

## What it checks

- Length: under 8 characters is an immediate Weak
- Common passwords: anything on a built-in list (like `password1`) is Weak
- Character variety: uppercase letters, digits and symbols
- Strong needs all three character types and 12+ characters

## How to run

```
python3 checker.py
```

The password is read with `getpass`, so it is not shown on screen while you type.

## Example results

| Password | Result |
|---|---|
| `abc` | Weak (too short) |
| `password1` | Weak (common password) |
| `hello12345` | Weak (only one character type) |
| `Hello1234` | Medium |
| `Tr0ub4dor&3xyz!` | Strong |

## Notes

- `any()` with a generator checks each rule and stops at the first match, so the scan stays linear in the password length.
- Passwords are never printed, logged or saved.
- The common-password list is only a small sample. A larger list could be loaded from a file.

## Ideas for next steps

- Loop so several passwords can be tested in one run
- Load a bigger leaked-password list from a file
- Add unit tests

## Author

Noman Atiq
