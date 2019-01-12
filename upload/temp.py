import MySQLdb

def run_sql(sql):
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root123',db='HttpRunner',port=3306)
    cursor = db.cursor()
    print('开始执行sql：' + sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    data = cursor.fetchone()
    print('sql执行结果为：' + str(data))
    db.close()


#un_sql('select username from auth_user where is_active = 0')