import csv
import utility, conf, psycopg2, tollapi

dbconn = utility.getPGConnection()
cur = dbconn.cursor()

with open(conf.filepath, 'rt') as f:
    ty = next(f)
    x = ty.split(',')
    header_params = (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
    cur.execute(conf.insert_etc_toll_file, header_params)
    dbconn.commit()
    readecsv = csv.reader(f)
    count = 0
    for line in readecsv:
        try:
            body_params = (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18], line[19], line[20], line[21], line[22], line[23], line[24], line[25], line[26], line[27], line[28], line[29], line[30], line[31], line[32], line[33], line[34], line[35], line[36], line[37], line[38], line[39], x[7])
            cur.execute(conf.insert_etc_toll_tran, body_params)
            dbconn.commit()
            count += 1
        except psycopg2.IntegrityError as error:
            cur.execute("ROLLBACK")
            cur.execute(conf.insert_etc_toll_tran_exp, body_params)
            dbconn.commit()
            count += 1
            tollapi.write_log(error)
            tollapi.write_log("Get these Transactions from Exception Table...")
        except Exception as identifier:
            tollapi.write_log(identifier)
    tollapi.write_log(str(count) + " Transactions are being processing...")

try:                     
    tollapi.NETC_reqDetail()
    tollapi.NETC_reqPay()
except Exception as error:
    tollapi.write_log(error)
finally:
    dbconn.close()
