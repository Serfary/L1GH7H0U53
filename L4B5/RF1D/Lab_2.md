# Lab 2: Cloning Badges

## Overview

RFID Badges are a common form of authentication granting access to everything from hotels and transportation to office buildings and workstations. While higher security solutions exist, the most commonly used chipsets are quickly cloned and usable with little to no interaction.

## Requirements

-   Proxmark3 Easy
-   Low-Frequency Tag
-   T5577 Tag

## Steps

#### Reading Card Data

1. Connect to the Proxmark3 Easy
    - Using the `pm3` command
    - `help` will show additional details
2. Place the low-frequency card on the reader
    - Identify the **chipset** with `lf search`
    - Confirm the **details** with `lf {chipset} reader`
3. Store the information for later
    - **Card Number** - Assigned to the cardholder
    - **Facility Code** - Assigned to a specific company, building, or location
    - **Raw Data** - The full value with parity bits for error checking

#### Writing Card Data

1. Replace the Low-Frequency Tag with a T5577 on the reader
    - This card type is rewritable with the ability to emulate multiple different formats
2. Reference the **chipset** information to build the cloning command
    - `lf {chipset} clone --help` will provide examples of valid parameters
    - HID for example will use **Raw Data** `lf hid clone -r {raw data}`
3. Run the command and **validate** the resulting tag
    - Check the values using `lf {chipset} reader` against the original card

