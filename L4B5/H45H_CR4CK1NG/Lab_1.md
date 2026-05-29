# Lab 1: Hashing Algorithms & Password Complexity

## Overview

16+ characters, uppercase, lowercase, numbers, and symbols...

We all know the requirements of a good password, but how do each of these elements actually make a password stronger? When designing an application, which hashing algorithm would you choose to protect your users?

## Requirements

-   Hashcat
-   Wordlists
-   Hashes

## Steps

**_Use the BadUSB to generate Lab Environment_**

#### Bruteforcing MD5

1.  Review the Hashcat command options
    -   Using `hashcat --help` to show additional details
    -   **Attack Type** - Sets the method of attack being used
    -   **Hash Modes** - Sets the algorithm to target
    -   **Charset** - The characters to use in generated passwords
2.  Create the command to look for any passwords up to 4 characters
    -   Full Command - `hashcat -a 3 -m 0 hashes.txt -i ?a?a?a?a`
    -   `-a 3 | Brute-force` - Attempts to match hashes by generating all possible combinations of characters
    -   `-m 0 | MD5` - Converts the generated passwords to MD5 for comparison
    -   `hashes.txt` - The path to the hash file
    -   `-i ?a?a?a?a` -
3.  Review the output
    -   **Time** -
    -   **Speed** -
    -   **Recovered** -
4.  Repeat the attack with different lengths character options
    ```
    ? | Charset
    ===+=========
    l | abcdefghijklmnopqrstuvwxyz [a-z]
    u | ABCDEFGHIJKLMNOPQRSTUVWXYZ [A-Z]
    d | 0123456789                 [0-9]
    h | 0123456789abcdef           [0-9a-f]
    H | 0123456789ABCDEF           [0-9A-F]
    s |  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    a | ?l?u?d?s
    b | 0x00 - 0xff
    ```
