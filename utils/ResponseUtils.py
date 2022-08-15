import copy
import json

from bean.CheckResponseResult import CheckResponseResult
from config.FlaskConfig import flask


def responseModelAndView(result):
    result = result
    response = flask.make_response(result)
    response.headers = {"Content-Type": "application/json;charset=utf8", "Access-Control-Allow-Origin": "*"}
    response.status_code = 200
    return response


def change_type(byte):
    if isinstance(byte, bytes):
        return str(byte, encoding="utf-8")
    return json.JSONEncoder.default(byte)


def reportToStrModelAndView(checkResponseResult: CheckResponseResult):
    checkResponseResultCopy = copy.copy(checkResponseResult)
    sequence = checkResponseResult.get_infCallSequence()
    checkResponseResult.set_infCallSequence(None)

    masterReport = checkResponseResult.__dict__
    viceReport = []
    if sequence is not None:
        for inf in sequence:
            viceReport.append(inf.__dict__)
        masterReport['resultInfList'] = viceReport
    # dict__ = checkResponseResult.__dict__
    # print(dict__)
    # sequence___dict__ = sequence.__dict__
    # print(sequence___dict__)
    return masterReport

