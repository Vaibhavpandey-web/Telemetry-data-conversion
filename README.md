<div align="center">

# Telemetry Data Conversion

Normalize two timestamp formats into one chronologically sorted data stream.

![Python](https://img.shields.io/badge/Python-111827?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-111827?style=flat-square) ![Standard library](https://img.shields.io/badge/Standard%20library-111827?style=flat-square)

</div>

---

[Source](main.py) · [Input format](#input-format) · [Run locally](#run-locally)

## Overview

A Python training exercise associated with the Deloitte Australia / Daikibo scenario. The implementation converts UTC ISO timestamps to Unix milliseconds, merges two lists and compares the result with expected output.

This repository contains the conversion script. A private dashboard, authentication system and live factory monitoring are not implemented here.

## Input format

| File | Expected data |
| --- | --- |
| `data-1.json` | List of objects with `timestamp` in `YYYY-MM-DDTHH:MM:SSZ` format and a `value` |
| `data-2.json` | List of objects with numeric millisecond `timestamp` and a `value` |
| `data-result.json` | Expected merged, sorted list |

## Run locally

Requires Python 3; no third-party packages are used.

```bash
git clone https://github.com/Vaibhavpandey-web/Telemetry-data-conversion.git
cd Telemetry-data-conversion
python main.py
```

**Before running:** supply the three JSON files listed above in the working directory. They are not currently included in the repository. The script writes `output.json` and prints whether it matches the expected result.

<details>
<summary><strong>Conversion details</strong></summary>

1. Parse UTC timestamps from the first source.
2. Convert them to milliseconds since the Unix epoch.
3. Append the second source's already-normalized records.
4. Sort all records by timestamp.
5. Write the result and compare it with the expected list.

The parser accepts the exact UTC format shown above; fractional seconds and other timezone offsets are not supported. The script assumes valid input keys and does not remove duplicates.

</details>

---

Built by [Vaibhav Pandey](https://github.com/Vaibhavpandey-web) · [Portfolio](https://vaibhav-pandey-portfolio-henna.vercel.app/)
