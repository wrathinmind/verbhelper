import requests
import sys
from bs4 import BeautifulSoup

collection = sys.argv[1]
session = sys.argv[2]

page = 1
cookies = {
    'JSESSIONID': session
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
def extract_words(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [q.get_text().replace('·', '').replace('\u200b', '') for q in soup.select('div.bTrf span[style="font-size: 1.44em;"] q')]

out = []

while True:
    params = {
        'p': page,
        'c': collection
    }
    res = requests.get('https://www.verbformen.de/suche/e/', params=params, cookies=cookies, headers=headers)
    if "maximal anz" in res.text.lower():
        print("you need to solve captcha in browser")
        exit()
    chunks = extract_words(res.text)
    ol = len(out)
    out = list(set(out + chunks))
    page += 1
    if len(chunks) < 20 or len(out) == ol:
        break

for w in out:
    print(w)