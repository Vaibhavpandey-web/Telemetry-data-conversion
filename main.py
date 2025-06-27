import json
from datetime import datetime, timezone

# IMPLEMENT: convert ISO timestamp to milliseconds
def convert_iso_to_millis(iso_str):
    """
    Convert ISO 8601 timestamp (e.g. "2023-01-01T10:00:00Z") to milliseconds since epoch.
    """
    # Parse string into datetime object and assign UTC timezone
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    dt = dt.replace(tzinfo=timezone.utc)
    # Convert to Unix timestamp and convert to milliseconds
    return int(dt.timestamp() * 1000)

# IMPLEMENT: merge the two telemetry sources into the target format
def merge_sources(data1, data2):
    """
    Combine and normalize telemetry data from two formats into a unified sorted list.
    """
    merged = []

    # Convert ISO timestamps in data1
    for item in data1:
        millis = convert_iso_to_millis(item["timestamp"])
        merged.append({
            "timestamp": millis,
            "value": item["value"]
        })

    # Append data2 (already in milliseconds)
    for item in data2:
        merged.append({
            "timestamp": item["timestamp"],
            "value": item["value"]
        })

    # Sort the merged list by timestamp
    merged.sort(key=lambda x: x["timestamp"])
    return merged

# DO NOT MODIFY BELOW THIS LINE UNLESS TOLD TO DO SO
def main():
    # Read input files
    with open("data-1.json") as f1:
        data1 = json.load(f1)

    with open("data-2.json") as f2:
        data2 = json.load(f2)

    # Get merged output
    result = merge_sources(data1, data2)

    # Write to output.json
    with open("output.json", "w") as outf:
        json.dump(result, outf, indent=2)

    # Load expected output
    with open("data-result.json") as expectedf:
        expected = json.load(expectedf)

    # Verify output matches expected result
    if result == expected:
        print("✅ All tests passed!")
    else:
        print("❌ Test failed: Output does not match expected result.")
        print("\nYour Output:\n", json.dumps(result, indent=2))
        print("\nExpected Output:\n", json.dumps(expected, indent=2))

# Run the program
if __name__ == "__main__":
    main()
