# 📝 Log Analyzer (Python)

A lightweight Python tool that scans log files for **ERROR** and **WARNING** messages, generates a summary report, and optionally exports flagged lines to a CSV file for further analysis.  

This project demonstrates skills in Python scripting, file handling, string processing, and CSV data export using only built-in libraries.

---

## 🚀 Features
- 🔍 Detects **ERROR** and **WARNING** messages in log files.  
- 🧾 Displays counts of errors and warnings with line numbers.  
- 📂 Optionally exports flagged lines to `log_report.csv`.  
- ⚡ Case-insensitive scanning for flexible log parsing.  
- ✅ No external dependencies — runs on any system with Python 3.

---

## 📂 Example Usage

### 1. Run the script:
```bash
python analyze_log.py

Enter the log file name (e.g., sample.log): sample.log

=== Log Analysis Report ===
Total Errors:   3
Total Warnings: 2
----------------------------
Flagged Lines:
[Line 4] ERROR: Failed to connect
[Line 10] WARNING: Deprecated API usage
[Line 15] ERROR: Invalid configuration

If you choose to export:
Report exported to log_report.csv

Run the script with Python 3:
python analyze_log.py

📑 Project Structure
Log-Analyzer/
│
├── analyze_log.py     # main script
├── README.md          # project documentation
├── .gitignore         # ignored files (logs, CSVs, cache)
└── sample.log         # example log file (optional)

## 💡 Skills Demonstrated
- ✅ **Python scripting fundamentals** – clean, structured, reusable code  
- ✅ **File I/O and error handling** – safe log reading and parsing  
- ✅ **String processing and conditionals** – analyzing and filtering data  
- ✅ **CSV export and reporting** – creating structured outputs  
- ✅ **Command-line interaction** – user prompts and automation

