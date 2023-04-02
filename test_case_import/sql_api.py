from model import *
from sql_connection import session, engine, meta


def set_test_cases_metadata(test_case_name, precondition, attachment, priority):
    record = TestCasesMetadata(TEST_CASE_NAME=test_case_name, PRECONDITION=precondition, ATTACHMENTS=attachment,
                               PRIORITY=priority)
    session.add(record)
    session.commit()
# set_test_cases_metadata("test name2", "site available", "linkto some stuff", "High")


def set_test_cases_details(test_case_id, step_number, description, expected_result, actual_result, status, screenshot):
    record = TestCasesDetails(TEST_CASE_ID=test_case_id, STEP_NUMBER=step_number, DESCRIPTION=description,
                              EXPECTED_RESULT=expected_result, ACTUAL_RESULT=actual_result, STATUS=status,
                              SCREENSHOT=screenshot)
    session.add(record)
    session.commit()
# set_test_cases_details(1, 2, "description", "expected", "actual", "Passed", None)


def get_test_case_id_by_name(test_case_name):
    result = session.query(TestCasesMetadata).filter(TestCasesMetadata.TEST_CASE_NAME == test_case_name).first()
    return result.ID


# metadata = session.query(TestCasesMetadata).all()
# details = session.query(TestCasesDetails).all()

