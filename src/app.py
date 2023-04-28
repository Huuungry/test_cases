from flask import Flask
from sql_api import get_test_cases, get_test_case_details_by_name

app = Flask(__name__)

@app.route("/cases")
def cases():
    return get_test_cases()

@app.route("/cases/<string:case_name>")
def get_case(case_name):
    return get_test_case_details_by_name(case_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
