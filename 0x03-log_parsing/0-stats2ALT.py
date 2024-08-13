#!/usr/bin/python3

import sys
from collections import defaultdict

def print_msg(status_counts, total_size):
    """
    Method to print the file size and status codes.
    
    Args:
        status_counts: defaultdict with status codes and their counts
        total_size: total size of files processed
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

def process_logs():
    """
    Processes log lines from stdin and prints statistics.
    """
    status_counts = defaultdict(int)
    total_size = 0
    line_count = 0

    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue

        try:
            file_size = int(parts[0])
            status_code = parts[1]
        except ValueError:
            continue

        total_size += file_size
        status_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_msg(status_counts, total_size)

    # Print final statistics
    print_msg(status_counts, total_size)

if __name__ == "__main__":
    process_logs()

