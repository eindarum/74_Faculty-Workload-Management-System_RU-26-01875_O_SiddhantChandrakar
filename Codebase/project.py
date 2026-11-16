import pandas as pd

FILE_NAME = "workload.csv"
WEEKLY_LIMIT = 16


def load_workload():
    #reads workload.csv using pandas and handles a missing file
    try:
        df = pd.read_csv(FILE_NAME)
        return df
    except FileNotFoundError:
        print(f"Error: '{FILE_NAME}' was not found in the current folder.")
        print("Please make sure workload.csv exists before running the program.")
        return None


def get_faculty_hours(df):
    #groups the data by faculty and returns a dictionary
    #using sort=False keeps the faculty in the order they appear in your csv file
    return df.groupby("Faculty", sort=False)["Hours"].sum().to_dict()


def show_workload_summary(df):
    #testcase1- displays total hours,free hours ,or overload status for each faculty
    totals = get_faculty_hours(df)
    for faculty, total_hours in totals.items():
        if total_hours > WEEKLY_LIMIT:
            overloaded_by = total_hours - WEEKLY_LIMIT
            print(f"{faculty} : {total_hours} hours - OVERLOADED by {overloaded_by} hours")
        else:
            free_hours = WEEKLY_LIMIT - total_hours
            print(f"{faculty} : {total_hours} hours ({free_hours} free)")


def assign_subject(df):
    #testcase 2and3- assign a new subject after validating hours and the 16hours limit
    faculty = input("Faculty: ").strip()
    subject = input("Subject: ").strip()
    hours_input = input("Hours: ").strip()

    # testcase- hours is a positive wholenumber
    try:
        hours = int(hours_input)
        if hours <= 0:
            print("Hours must be a positive whole number.")
            return df
    except ValueError:
        print("Hours must be a positive whole number.")
        return df

    totals = get_faculty_hours(df)
    current_hours = totals.get(faculty, 0)
    new_total = current_hours + hours

    #testcase- assignment does not exceed the 16hours limit
    if new_total > WEEKLY_LIMIT:
        print(f"Cannot assign: {faculty} would have {new_total} hours, exceeding the {WEEKLY_LIMIT}-hour limit.")
        return df

    # add the new subject to dataframe and save back to workload.csv
    new_row = pd.DataFrame([{"Faculty": faculty, "Subject": subject, "Hours": hours}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    #testcase2- display confirmation message
    if new_total == WEEKLY_LIMIT:
        print(f"Assigned. {faculty} now has {new_total} hours (limit reached).")
    else:
        free_left = WEEKLY_LIMIT - new_total
        print(f"Assigned. {faculty} now has {new_total} hours ({free_left} free).")

    return df


def find_faculty_with_free_hours(df):
    #testcase4- find all faculty members with at least requested free hours
    hours_input = input("Hours needed: ").strip()
    try:
        hours_needed = int(hours_input)
        if hours_needed <= 0:
            print("Hours needed must be a positive whole number.")
            return
    except ValueError:
        print("Hours needed must be a positive whole number.")
        return

    totals = get_faculty_hours(df)
    print(f"Faculty available for {hours_needed} hours:")
    found = False

    for faculty, total_hours in totals.items():
        free_hours = WEEKLY_LIMIT - total_hours
        if free_hours >= hours_needed:
            print(f"{faculty} : {free_hours} hours free")
            found = True

    if not found:
        print("No faculty available with enough free hours.")


def main():
    df = load_workload()
    if df is None:
        return  # Exit cleanly if workload.csv is missing

    while True:
        print("\n--- Faculty Workload Management System ---")
        print("1. Show workload summary")
        print("2. Assign subject")
        print("3. Find faculty with free hours")
        print("4. Exit")

        choice = input("Menu: ").strip()

        if choice == "1":
            show_workload_summary(df)
        elif choice == "2":
            df = assign_subject(df)
        elif choice == "3":
            find_faculty_with_free_hours(df)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()