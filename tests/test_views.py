from app import app
from flask import json
from testData import rawTimetableData
import subprocess


"""
test hello world API
"""
def test_helloAPI():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'hello'

"""
test generate timetables API
"""
def test_generateTimetablesAPI():
    response = app.test_client().post(
        '/api/v1/test',
        data=json.dumps(rawTimetableData),
        content_type='application/json',
    )

    # check anything goes wrong during the transfromation from json to xml
    assert response.status_code == 200

"""
use fet to test whether the generated xml file is valid or not
and validate some values in the timetable data files generated by fet
"""
def test_fet():
    stdoutdata = subprocess.getoutput("sudo fet-cl --inputfile=test.fet")
    print(stdoutdata)

# TODO: validate some values in the timetable data files generated by fet
