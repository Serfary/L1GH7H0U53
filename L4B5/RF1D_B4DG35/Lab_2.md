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
3. Store the information for cloning
    - **Card Number** - Assigned to the cardholder
    - **Facility Code** - Assigned to a specific company, building, or location
    - **Raw Data** - The full value with parity bits for error checking
