from model import TestCasesMetadata, TestCasesDetails
from sql_connection import session, engine, meta
from sqlalchemy import inspect
import json


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


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

def get_test_cases():
    test_case_metadata = session.query(TestCasesMetadata).all()
    test_case_metadata_dict = {}
    test_case_metadata_dict["CASES"] = []
    for test_case in test_case_metadata:
        test_case_metadata_dict["CASES"].append(object_as_dict(test_case))
    return json.dumps(test_case_metadata_dict)


def get_test_case_details_by_name(test_case_name):
    test_case_metadata = session.query(TestCasesMetadata).filter(TestCasesMetadata.TEST_CASE_NAME == test_case_name)
    test_case_metadata_dict = object_as_dict(test_case_metadata.first())
    test_case_metadata_dict["STEPS"] = []
    for test_case_step in session.query(TestCasesDetails).filter(TestCasesDetails.TEST_CASE_ID == test_case_metadata_dict["ID"]):
        test_case_step_dict = object_as_dict(test_case_step)
        test_case_metadata_dict["STEPS"].append(test_case_step_dict)
    return json.dumps(test_case_metadata_dict)


metadata = session.query(TestCasesMetadata).all()
details = session.query(TestCasesDetails).all()
