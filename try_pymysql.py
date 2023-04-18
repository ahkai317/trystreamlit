# -*- coding: utf-8 -*-
# import pymysql
# from setup import Conn_DB as db
import setup

with setup.Conn_DB('sys_db').cursor() as cursor:

    sql = 'SELECT * FROM `sys_db`.`activity_list`'

    cursor.execute(sql)

    setup.Conn_DB('sys_db').commit()

    data = cursor.fetchall() # -> tuple

print(data)

setup.Conn_DB('sys_db').close() # 手動關閉 (使用 with as 可不需要此行)

# conn_db = pymysql.connect(
#                     host='127.0.0.1',
#                     port=3306,
#                     user='root',
#                     passwd='root',
#                     charset='utf8',
#                     db='sys_db'
#             )

# with conn_db.cursor() as cursor:

#     sql = 'SELECT * FROM `sys_db`.`activity_list`'

#     cursor.execute(sql)

#     conn_db.commit()

#     data = cursor.fetchall() # -> tuple

# conn_db.close()