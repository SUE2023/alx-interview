#!/usr/bin/python3

import sys
import re
from collections import defaultdict

def print_msg(status_counts, total_size):
    """
    Method to print the file size and status codes.
    
    Args:
        status_counts: defaultdict with status codes and their counts
        total_size: total size of files processed
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def process_logs():
    """
    Processes log lines from stdin and prints statistics.
    """
    valid_status_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    status_counts = defaultdict(int)
    total_size = 0
    line_count = 0
    log_pattern = re.compile(r'^.* - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

    try:
        for line in sys.stdin:
            match = log_pattern.match(line)
            if match:
                status_code, file_size = match.groups()
                if status_code in valid_status_codes:
                    file_size = int(file_size)
                    status_counts[status_code] += 1
                    total_size += file_size
                    line_count += 1

                    if line_count % 10 == 0:
                        print_msg(status_counts, total_size)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass

    finally:
        # Print final statistics
        print_msg(status_counts, total_size)

if __name__ == "__main__":
    process_logs()
