from flask import jsonify, abort, request, Flask
import utilities
from http import HTTPStatus

app = Flask(__name__)


def getfare(getrequest):
    toll_id = getrequest.get('toll_id')
    vehicle_type = getrequest.get('vehicle_type')
    journey_type = getrequest.get('journey_type')
    resp = {}
    try:
        dbconn = utilities.getPGConnection()
        dbconn.autocommit = True
        crsr = dbconn.cursor()
        crsr.execute("select netc_getfare('" + toll_id + "','" + vehicle_type + "','" + journey_type + "')")
        row = crsr.fetchone()
        print(row)
        resp['fare_amount'] = row[0]
        crsr.close()
        dbconn.close()
        
    except Exception as error:

        resp['status'] = 'Invalid data'
    return jsonify(resp)
    
    abort(HTTPStatus.UNAUTHORIZED)


