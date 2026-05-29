# Lab 1: Identifying RFID Frequencies & Card Types

## Overview

Using a Radio Frequency Field Detector can reveal information about the reader and cards being tested. This additional configuration makes tools faster and more reliable, increasing the chances of a successful read by focusing on known types rather than guessing.

## Requirements

-   Proxmark3 Easy
-   Proxgrind
-   RFID Tags

## Steps

#### Identifying Reader Frequencies

1. Examine the Proxgrind tool
    - Two small LEDs at the top and bottom
    - **13.56MHz** - High-Frequency
    - **125KHz** - Low-Frequency
2. Connect to the Proxmark3 Easy
    - Using the `pm3` command
    - `help` will show additional details
3. Place the Proxgrind tool on the reader
    - **NO LED** - Indicates no RF fields detected
    - Use the `auto` command to enable the reader
    - Detection tool will respond to the reader testing for all potential tags
4. Test for Low-Frequency
    - Use `lf search` to set the reader to low-frequency
    - **RED LED** - Low-Frequency detected
5. Test for High-Frequency
    - Use `hf search` to set the reader to LF Mode
    - **WHITE LED** - High-Frequency detected

#### Identifying Card Types

1. Select a RFID Tag to replace the RF Detector
2. Run the `auto` command to scan the tag
    - The reader cycles all known tags to identify potential matches
    - Matches are based on the card **data length** and **decoding** output
    - Valid **chipset** details include frequency type and name
3. Based on details from the scan:
    - **Narrow** the frequency with `[lf|hf] search`
    - **Validate** the chipset with `lf {chipset} reader`
    - **Focus** the reader with `lf {chipset} watch`

