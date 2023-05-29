# Code to import test cases from xls document to the postgres db, provide CLI and REST api to return test case data in JSON, and Web UI to retrieve test case data

Environment configuration:

1. Install python3.10 to your env > clone the repository > from the terminal run `pip install -r src/requirements.txt` command
2. Install docker to your env > from the terminal run `docker-compose up` command to start the postgress service and Web API
3. Run `src/xls_to_sql_import.py`
4. In case of changes in Web API you will need to rebuild web container wih `docker-compose build` command

Usage:

1. Use `python3 src/query_details.py` to query test case details from CLI. Running without parameters provides list of all test cases and if you specify test case name as parameter it will provide test_case details. E.g. `python3 src/query_details.py "Login positive test"`
2. Use "http://localhost:8000/api/test_cases" URL to obtain test cases details from Web API. E.g. `curl "http://localhost:8000/cases"` to list all test cases and `curl "http://localhost:8000/api/test_cases/Login%20positive%20test"` to get specific test case details. Remember that spaces in test case name should be URL encoded (e.g. %20).
