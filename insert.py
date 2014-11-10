import json
import requests
import sys
from sqlalchemy import create_engine
import settings

e = create_engine(settings.mysql_connection)

url = sys.argv[1]
cms_id = sys.argv[2]
sql = "INSERT INTO websites VALUES(NULL, %s, '%s', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0)" % (cms_id, url)
e.execute(sql)
