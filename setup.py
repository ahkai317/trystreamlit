# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pymysql

setup(
    name='trystreamlit',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'streamlit',
    ],
    entry_points={
        'console_scripts': [
            'trystreamlit = trystreamlit.__main__:main'
        ]
    },
)

def Conn_DB(db_string) -> str:
    if db_string == 'sys_db':
        db_name = 'sys_db'

    elif db_string == 'finance_db':
        db_name = 'finance_db'

    elif db_string == 'account_db':
        db_name = 'account_db'

    elif db_string == 'game_db':
        db_name = 'game_db'

    else:
        print("Input Error: Illgal DB name.")
        return

    return pymysql.connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='root',
                    charset='utf8',
                    db=db_name
            )