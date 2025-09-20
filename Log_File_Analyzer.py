import csv

def analyze_log(file_path):
    errors = 0
    warnings = 0
    flagged_lines = []   # store line number + content

    with open(file_path, "r") as f:
        for line_num, line in enumerate(f, start=1):
            if "ERROR" in line.upper():       # case-insensitive
                errors += 1
                flagged_lines.append((line_num, "ERROR", line.strip()))
            elif "WARNING" in line.upper():
                warnings += 1
                flagged_lines.append((line_num, "WARNING", line.strip()))

    # Print summary
    print("=== Log Analysis Report ===")
    print(f"Total Errors:   {errors}")
    print(f"Total Warnings: {warnings}")
    print("----------------------------")

    if flagged_lines:
        print("Flagged Lines:")
        for line_num, level, content in flagged_lines:
            print(f"[Line {line_num}] {level}: {content}")
    else:
        print("No errors or warnings found.")

    # Ask user if they want to export
    if flagged_lines:
        choice = input("\nDo you want to export flagged lines to CSV? (y/n): ")
        if choice.lower() == "y":
            with open("log_report.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Line Number", "Level", "Message"])
                writer.writerows(flagged_lines)
            print("Report exported to log_report.csv")
        else:
            print("Export skipped.")


if __name__ == "__main__":
    log_file = input("Enter the log file name (e.g., sample.log): ")
    analyze_log(log_file)
