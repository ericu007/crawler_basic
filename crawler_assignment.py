import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=UME&t__" \
      "nil_searchbox=suggest&sug=&sugo=16&sq=%EB%A1%9C%EB%" \
      "98%90&o=2&q=%EB%A1%9C%EB%98%90+%EB%8B%B9%EC%B2%A8+%EB%B2%88%ED%98%B8"

req = requests.get(url)

if req.status_code == requests.codes.ok:
    print("접속 성공")
    html = BeautifulSoup(req.text, "html.parser")

    span = html.select(".lottonum > span")
    for item in span:
        print(item.text)
else:
    print("접속 실패")
