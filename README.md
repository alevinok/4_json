# Prettify JSON

The script that accepts the path to the input file with arbitrary data in JSON format 
and displays its contents to the console in a readable form: adds line breaks, indents to the left, and spaces.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
...

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
