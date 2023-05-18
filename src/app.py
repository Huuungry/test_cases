import flask
from flask import Flask
from sql_api import get_test_cases, get_test_case_details_by_name
import json

app = Flask(__name__, template_folder='templates')

@app.route("/api/test_cases")
def cases():
    return get_test_cases()

@app.route("/api/test_cases/<string:case_name>")
def get_case(case_name):
    return get_test_case_details_by_name(case_name)

@app.route("/test_cases")
def test_cases():
    json_result = get_test_cases()
    return flask.render_template("index.html", jsonData=json_result)

@app.route("/test_cases/<string:test_case_name>")
def get_test_case(test_case_name):
    json_result = get_test_case_details_by_name(test_case_name)
    return flask.render_template("test_case_details.html", jsonData=json_result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
