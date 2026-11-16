# Faculty Workload Management System

A Python-based command-line application designed to track, manage, and allocate teaching hours for faculty members while enforcing a maximum weekly workload limit.

## Features

* **Workload Summary:** View total assigned hours, remaining free hours, or overload status for every faculty member.
* **Subject Assignment with Validation:** Assign new subjects to faculty members with built-in checks to ensure:
  * Assigned hours are positive whole numbers.
  * Total weekly hours do not exceed the maximum limit of **16 hours**.
* **Persistent Storage:** Automatically saves new subject assignments back to `workload.csv`.
* **Availability Search:** Quickly find faculty members who have enough free hours available to take on a new course or task.

---

## Prerequisites

* **Python 3.x**
* **pandas** library

To install `pandas`, run:
```bash
pip install pandas
```

---

## Project Structure

```text
├── project.py       # Main application script
├── workload.csv     # Data file storing faculty, subject, and hour records
└── README.md        # Project documentation
```

### `workload.csv` Format
Ensure that `workload.csv` exists in the same directory as `project.py` before running the program. It must contain the following column headers:

```csv
Faculty,Subject,Hours
Dr. Smith,Data Structures,6
Dr. Smith,Algorithms,4
Prof. Johnson,Database Systems,8
```

---

## Usage

Run the application from your terminal:

```bash
python project.py
```

### Menu Options

1. **Show workload summary**
   Displays each faculty member's current hours and whether they have free capacity or are overloaded (exceeding 16 hours).
2. **Assign subject**
   Prompts for a faculty name, subject name, and number of hours. If valid and within the 16-hour weekly limit, the entry is appended and saved to `workload.csv`.
3. **Find faculty with free hours**
   Prompts for the number of hours needed and lists all faculty members who have at least that many free hours remaining.
4. **Exit**
   Closes the application.

---

## Configuration

You can adjust the file path or maximum weekly hour threshold directly at the top of `project.py`:

```python
FILE_NAME = "workload.csv"
WEEKLY_LIMIT = 16
```