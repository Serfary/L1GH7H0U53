#!/usr/bin/env python3
import os, random, string, hashlib, bcrypt

base_path = os.path.expanduser("~")
resource_path = "L1GH7H0U53/R350URC35/W0RDL1575"

PASSWORD_FILE = os.path.join(base_path, resource_path, "passwords.txt")
HASH_OUTPUT_FILE = os.path.join(base_path, "hashes.txt")
WORDLIST_OUTPUT_FILE = os.path.join(base_path, "wordlist.txt")

TOTAL_FROM_FILE = 50
TOTAL_GENERATED = 50
TOTAL_MD5 = 90
TOTAL_BCRYPT = 10

GEN_LOWERCASE = 20
GEN_NUMERIC = 10
GEN_MIXED = 20

WORDLIST_MATCH_COUNT = 90
WORDLIST_FILLER_COUNT = 410

def rand_len():
    return random.randint(2, 8)

def random_lowercase():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(rand_len()))

def random_numeric():
    return "".join(random.choice(string.digits) for _ in range(rand_len()))

def random_mixed():
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(rand_len()))

def random_filler():
    choice = random.randint(0, 2)

    if choice == 0:
        return random_lowercase()
    elif choice == 1:
        return random_numeric()
    else:
        return random_mixed()

def md5_hash(value):
    return hashlib.md5(value.encode()).hexdigest()

def bcrypt_hash(value):
    return bcrypt.hashpw(value.encode(), bcrypt.gensalt()).decode()

def main():
    with open(PASSWORD_FILE, "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f if line.strip()]

    if len(passwords) < TOTAL_FROM_FILE:
        raise ValueError(f"{PASSWORD_FILE} must contain at least {TOTAL_FROM_FILE} non-empty lines")

    selected_passwords = random.sample(passwords, TOTAL_FROM_FILE)

    generated_strings = []

    for _ in range(GEN_LOWERCASE):
        generated_strings.append(random_lowercase())

    for _ in range(GEN_NUMERIC):
        generated_strings.append(random_numeric())

    for _ in range(GEN_MIXED):
        generated_strings.append(random_mixed())

    all_strings = selected_passwords + generated_strings
    random.shuffle(all_strings)

    bcrypt_items = set(random.sample(range(len(all_strings)), TOTAL_BCRYPT))

    with open(HASH_OUTPUT_FILE, "w", encoding="utf-8") as out:
        for i, value in enumerate(all_strings):
            if i in bcrypt_items:
                out.write(bcrypt_hash(value) + "\n")
            else:
                out.write(md5_hash(value) + "\n")

    wordlist_entries = random.sample(all_strings, WORDLIST_MATCH_COUNT)

    for _ in range(WORDLIST_FILLER_COUNT):
        wordlist_entries.append(random_filler())

    random.shuffle(wordlist_entries)

    with open(WORDLIST_OUTPUT_FILE, "w", encoding="utf-8") as out:
        for word in wordlist_entries:
            out.write(word + "\n")

if __name__ == "__main__":
    main()
