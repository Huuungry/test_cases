from sql_api import get_test_case_details_by_name

test_case_details_json = get_test_case_details_by_name("Login positive test")

print(test_case_details_json)
