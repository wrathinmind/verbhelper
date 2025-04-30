# A tool to extract your wordlists from vebformen

## build
1. git clone https://github.com/wrathinmind/verbhelper
2. cd verbhelper
3. `docker build . -t verbformen`

## usage
1. Find your jsessionid using Developer Tools -> Application -> Cookies -> JSESSIONID. **e.g. AAAAAAAABBBBBBBCCCCCCC**
2. Find your collection id using https://www.verbformen.de/suche **e.g 2**
3. run `docker run --rm -it verbformen 2 AAAAAAAABBBBBBBCCCCCCC > fav.list`