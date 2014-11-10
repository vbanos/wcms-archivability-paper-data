import requests
from pyquery import PyQuery

def identify_url(url):
    try:
        resp = requests.get(url)
        pq = PyQuery(resp.content)
        for meta in pq("""meta"""):
            meta_name = meta.get('name')
            if meta_name:
                meta_name = meta_name.strip().lower()
                if meta_name == "generator":
                    meta_content = meta.get('content')
                    if meta_content:
                        wfile = open('detect', 'a')
                        wfile.write(url + "|||" + meta_content.lower() + "\n")
                        wfile.close()
    except Exception as exc:
        print str(exc)
