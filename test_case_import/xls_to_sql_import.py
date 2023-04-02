import sql_api
import pandas as pd
from sql_api import set_test_cases_details, set_test_cases_metadata, get_test_case_id_by_name, session
from model import *

# Read test cases from Excel file
df = pd.read_excel('test_cases.xls')

# Insert test case into the database
current_test_case_name = ""
for row in df.itertuples():
    if isinstance(row.name, str):
        try:
            current_test_case_name = row.name
            set_test_cases_metadata(row.name, row.precondition, row.attachments, row.priority)
            set_test_cases_details(get_test_case_id_by_name(current_test_case_name), row.step_number, row.description,
                                   row.expected_result, row.actual_result, row.status, None)
            print(f"Test case '{current_test_case_name}' added to the DB")
        except Exception as e:
            session.rollback()
            print(
                f"WARNING: Data was not imported. Ensure that test case '{current_test_case_name}'"
                f" does not already exist in the DB")
    else:
        test_case_id = get_test_case_id_by_name(current_test_case_name)
        # check if the same step number already exists in the DB for the same test case
        if len(session.query(TestCasesDetails).filter((TestCasesDetails.TEST_CASE_ID == test_case_id)
                                                      & (TestCasesDetails.STEP_NUMBER == row.step_number)).all()) == 0:
            set_test_cases_details(test_case_id, row.step_number, row.description,
                                   row.expected_result, row.actual_result, row.status, None)
