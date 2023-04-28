import sys
from sql_api import get_test_cases, get_test_case_details_by_name

if len(sys.argv) < 2:
    test_cases_json = get_test_cases()
    print(test_cases_json)
else:
    test_case_details_json = get_test_case_details_by_name(sys.argv[1])
    print(test_case_details_json)
