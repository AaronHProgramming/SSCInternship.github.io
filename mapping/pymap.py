import os
import csv
from datetime import datetime
import dbconnect


def csv_to_list(path, csv_name):
    lst = []
    with open(os.path.join(path, csv_name), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            lst.append(row)
    return lst


def make_query_str(table, filters):
    """

    :param table: name of table in database
    :param filters: dictionary where the key is the column name and the value is a tuple of strings to be combined into a SQL condition
    :return: a string that is valid SQL syntax to act on a database
    """

    s = 'SELECT unixtime, lat, lon, crs, spd, MMSI, SHIPNAME'

    def make_sql(conditions):
        string = ''
        for k, v in conditions.iteritems():
            string += " AND {col} {oper} '{val1}' {_and} '{val2}'".format(
                col=k, oper=v[0], val1=v[1], _and=v[2], val2=v[3])
        return string

    s += " FROM {table} WHERE 1{filt}".format(table=table, filt=make_sql(filters))
    return s


def db_to_list(host, user, pwd, dbname, table, sql=''):
    if not sql:
        sql = 'SELECT unixtime, lat, lon, crs, spd, MMSI, SHIPNAME FROM {0}.{1};'.format(dbname, table)

    lst = dbconnect.complete_command(host, user, pwd, sql, dbname)
    return lst


def geolist_to_jsvar(lst):
    # Takes lst argument from csv_to_list() or db_to_list()
    s = []
    for l in lst:
        s.append([float(l[2]), float(l[1]), "NAME: {}, Time: {}, CRS: {}, SPD: {}, MMSI: {}"
                  .format(l[6], datetime.fromtimestamp(int(l[0])).strftime('%Y-%m-%d %H:%M:%S'), l[3], l[4], l[5])])
    js_var = "var dataPoints = "+str(s)+";"
    with open(os.path.join('js/', 'aisData.js'), 'w') as js:
        js.write(js_var)
    return js_var


if __name__ == '__main__':

    # TO RUN WITH AISDATA.CSV FILE:
    # p = 'csv/'
    # csvname = 'aisdata.csv'
    # lst = csv_to_list(p, csvname)[1:]
    # geolist_to_jsvar(lst)

    # TO RUN THROUGH AISDB:
        # SELECT SQL COMMAND:

    host = "localhost"
    user = "root"
    pwd = "aaron"
    dbname = "aisdb"
    table = "obs"
    '''
    sql = dbconnect.select_with_shipname(dbname, table, "TIE-FIGHTER")
    time1 = datetime.fromtimestamp(1403708746L).strftime("%Y-%m-%d %H:%M:%S")
    time2 = datetime.fromtimestamp(1403708784L).strftime("%Y-%m-%d %H:%M:%S")
    '''
    d = dict()
    d['SHIPNAME'] = ('=', 'TIE-FIGHTER', '', '')
    d['unixtime'] = ('BETWEEN', '0', 'and', '1403709097')
    # columns = ['unixtime', 'lat', 'lon']

    sql = make_query_str(table, d)
    print sql
    '''dbconnect.select_with_shipname(dbname, table, "TIE-FIGHTER",
                                         dbconnect.select_between_coords(dbname, table, 0, 50, -140, 4,
                                                                         dbconnect.select_between_times(dbname, time1, time2, table)))
    '''
    lst = db_to_list(host, user, pwd, dbname, table, sql)
    print lst
    geolist_to_jsvar(lst)
