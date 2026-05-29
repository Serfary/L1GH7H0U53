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
    - Two small `LEDs` at the top and bottom
    - `13.56MHz` High-Frequency
    - `125KHz` Low-Frequency
2. Connect to the Proxmark3 Easy
    - Using the `pm3` command
    - `help` will show additional details
3. Place the Proxgrind tool on the reader
    - `NO LED` shows that the reader is currently inactive
    - Use the `auto` command to enable the reader
    - Detection tool will respond to the reader testing for all potential tags
4. Test for Low-Frequency
    - Use `lf search` to set the reader to LF Mode
    - `RED LED` shows that the reader is looking for Low-Frequency
5. Test for High-Frequency
    - Use `lf search` to set the reader to LF Mode
    - `WHITE LED` shows that the reader is currently inactive
