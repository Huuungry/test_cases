import sql_api
import pandas as pd
from sql_api import set_test_cases_details, set_test_cases_metadata, get_test_case_id_by_name

# Read test cases from Excel file
df = pd.read_excel('test_cases.xls')
# Connect to the database using SQLAlchemy

# Insert test case metadata into the database
current_test_case_name = ""
for row in df.itertuples():
    try:
        if isinstance(row.name, str):
            current_test_case_name = row.name
            set_test_cases_metadata(row.name, row.precondition, row.attachments, row.priority)
            set_test_cases_details(get_test_case_id_by_name(current_test_case_name), row.step_number, row.description,
                                   row.expected_result, row.actual_result, row.status, None)
        else:
            set_test_cases_details(get_test_case_id_by_name(current_test_case_name), row.step_number, row.description,
                                   row.expected_result, row.actual_result, row.status, None)
    except Exception as e:
        print(f"WARNING: Data was not imported. Ensure that test case '{current_test_case_name}' does not already exist in the DB")
