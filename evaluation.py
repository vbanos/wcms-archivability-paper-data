import json
import requests
from sqlalchemy import create_engine
import sys
import settings

e = create_engine(settings.mysql_connection)
# sql = """SELECT id, url FROM websites WHERE checked=0 AND id %% 2 = 1 ORDER BY id DESC"""
# sql = """SELECT id, url FROM websites WHERE cms_id>=5 AND checked=0 AND id %% 2 = 0 ORDER BY id DESC"""
sql = """SELECT id, url FROM websites WHERE checked=0 AND """ + sys.argv[1]
print sql
for r in e.execute(sql):
    try:
        print "evaluating", r.id, r.url
        response = requests.get("http://archiveready.com/api?url=%s" % r.url, timeout=720)
        print "done"
        if response.status_code == 200:
            obj = response.json()
            ac = obj['test']['Accessibility']
            st = obj['test']['Standards_Compliance']
            co = obj['test']['Cohesion']
            me = obj['test']['Metadata']
            wa = obj['test']['website_archivability']

            sql = """UPDATE websites SET status=%d, accessibility=%d, cohesion=%d, metadata=%d, standards=%d, wa=%d, checked=1 WHERE id=%d""" % (response.status_code, ac, co, me, st, wa, r.id)
            e.execute(sql)

            json_filename = "json/%d.json" % r.id
            with open(json_filename, 'w') as f:
                f.write(response.text)
                f.close()
        else:
            e.execute("UPDATE websites SET status=500, checked=1 WHERE id=%d" % r.id)
    except Exception as ex:
        print ex
        e.execute("""UPDATE websites SET status=-1, checked=1 WHERE id=%d""" % r.id)

