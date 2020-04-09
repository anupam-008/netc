import requests, sys, logging, utility, conf
from datetime import datetime
from flask import json
from simplejson import JSONDecodeError

dbconn = utility.getPGConnection()
cur = dbconn.cursor()


def write_log(error):
    logging.basicConfig(filename=datetime.now().strftime(conf.error_log), level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
    logging.error(error)


def transaction_dump(transaction_id, request, response):
    sql = conf.insert_etc_sql
    param = (transaction_id, request, response)
    cur.execute(sql, param)


def requesthandler(req_url, count, data_json):
    try:
        res = requests.post(url=req_url, json=json.loads(json.dumps(data_json[count])))
        res.raise_for_status()
        transaction_dump(data_json[count]['transaction_id'], json.dumps(data_json[count]), json.dumps([res.json()][0]))
        dbconn.commit()
    except requests.exceptions.HTTPError as error:
        write_log(error)
        sys.exit(1)
    except JSONDecodeError as error:
        err = (res.text[:30] + '...Error Occured While Parsing into JSON')
        write_log(err)
        sys.exit(1)


def NETC_reqDetail():
    try:    
        cur.execute(conf.reqdetail_sql)
        data_json = []
        header = [i[0] for i in cur.description]
        rows = cur.fetchall()
        if not rows:
            write_log(conf.notfound)
        count = 0
        for i in rows:
            data_json.append(dict(zip(header, i)))
            requesthandler(conf.reqdetail_api_url, count, data_json)
            count = count + 1
        print("---NETC_reqDetail Executed Sucessfully---")
    except Exception as identifier:
        write_log(identifier)


def NETC_reqListParticipant():
    try:
        cur.execute(conf.reqlistpartipant_sql)
        data_json = []
        header = [i[0] for i in cur.description]
        rows = cur.fetchall()
        if not rows:
            write_log(conf.notfound)
        count = 0
        for i in rows:
            data_json.append(dict(zip(header, i)))
            requesthandler(conf.reqlistparticipant_api_url, count, data_json)
            count = count + 1
        print("---NETC_reqListParticipant Executed Sucessfully---")
    except Exception as identifier:
        write_log(identifier)
    

def NETC_reqPay():
    try:
        cur.execute(conf.reqpay_sql)
        data_json = []
        header = [i[0] for i in cur.description]
        rows = cur.fetchall()
        if not rows:
            write_log(conf.notfound)
        count = 0
        for i in rows:
            data_json.append(dict(zip(header, i)))
            requesthandler(conf.reqpay_api_url, count, data_json)
            count = count + 1
        print("---NETC_reqPay Executed Sucessfully---")
    except Exception as identifier:
        write_log(identifier)
    


