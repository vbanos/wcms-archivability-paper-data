from sqlalchemy import create_engine
import settings
import sys

e = create_engine(settings.mysql_connection)

def insert(cms_id, url):
    try:
        sql = "INSERT INTO websites VALUES(NULL, %s, '%s', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0)" % (cms_id, url)
        e.execute(sql)
    except:
        pass


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

with file('detect', 'r') as fi:
    for line in fi:
        tmp = line.split("|||")
        if len(tmp) == 2:
            for key, value in cms.iteritems():
                if key in tmp[1]:
                    cms[key]['cnt'] = cms[key]['cnt'] + 1
                    if cms[key]['id'] > 10:
                        insert(cms[key]['id'], tmp[0])
                    break

print cms
