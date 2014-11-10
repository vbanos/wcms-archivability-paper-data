from sqlalchemy import create_engine
import settings
import sys
import ujson

e = create_engine(settings.mysql_connection)

cms = {
    "wordpress": {'id': 1, 'cnt': 0},
    "joomla": {'id': 2, 'cnt': 0},
    "drupal": {'id': 3, 'cnt': 0},
    "blogger": {'id': 4, 'cnt': 0},
    "magento": {'id': 5, 'cnt': 0},
    "typo3": {'id': 6, 'cnt': 0},
    "prestashop": {'id': 7, 'cnt': 0},
    "vbulletin": {'id': 8, 'cnt': 0},
    "bitrix": {'id': 9, 'cnt': 0},
    "datalife": {'id': 10, 'cnt': 0},
    "mediawiki": {'id': 11, 'cnt': 0},
    "dotnetnuke": {'id': 12, 'cnt': 0},
    "movable type": {'id': 13, 'cnt': 0},
    "plone": {'id': 14, 'cnt': 0},
    "microsoft frontpage": {'id': 15, 'cnt': 0},
    "dreamweaver": {'id': 16, 'cnt': 0}
}

results = e.execute("SELECT id FROM websites2 WHERE status=200 AND " + sys.argv[1])
for line in results:
    filename = "json/" + str(line.id)[0] + "/" + str(line.id) + ".json"
    fp = open(filename, 'r')
    json_str = fp.read()
    fp.close()
    data = ujson.loads(json_str)
    for msg in data['messages']:
        #if 'Accessibility' in msg['facets'] and msg['level'] < 100:
        print msg
