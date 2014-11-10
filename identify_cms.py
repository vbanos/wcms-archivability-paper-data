from redis import Redis
from rq import Queue

from identify import identify_url

# MAIN
if __name__ == "__main__":
    with open('top-1m.csv', 'r') as csv_file:
        i = 1

        queue = Queue(
            'identify',
            connection=Redis(),
            default_timeout=999999
        )
        for line in csv_file:
            tmp = line.split(",")
            url = "http://www." + tmp[1].strip()
            print i, url
            i = i+1
            queue.enqueue(identify_url, url)
            #if i == 10000:
            #    break
