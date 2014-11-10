import json
import requests
import sys
from sqlalchemy import create_engine
import settings

e = create_engine(settings.mysql_connection)

with open('inputs/topdrops.txt', 'r') as f:
    for line in f:
        if line:
            tmp = line.split("  ")
            if len(tmp) >= 2:
                if tmp[1]:
                    url = "http://www." + tmp[1].strip() + "/"
                    sql = "INSERT INTO websites VALUES(NULL, 2, '%s', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0)" % url
                    e.execute(sql)
