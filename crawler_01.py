"""
크롤러 : 웹 사이트에서 정보를 수집하는 프로그램
- 웹 브라우저를 흉내내는 프로그램

웹 브라우저 : HTML을 서버로 부터 받아와서
해석해서 화면에 보여주는 것

크롤러 : HTML을 서버로 부터 받아와서
해석해서 내가 원하는 텍스트, 이미지 등을 찾아내는 것

1) HTML을 서버로부터 받아오는 것 : requests
2) HTML을 해석해서 내가 원하는 텍스트를 찾는 것 : BeautifulSoup
2-1) 내가 원하는 텍스트를 찾으려면 그 텍스트를 담고있는 HTML 태그를 찾아야 한다.
2-2) HTML 태그를 찾으려면 CSS Selector

"""

import requests
# pip install requests
from bs4 import BeautifulSoup

# pip install BeautifulSoup4

# 1. 네이버.com 에 접속해서 html을 얻어오기
url = "https://www.naver.com/"

req = requests.get(url)  # 헤더 정보, 실제 컨텐츠

if req.status_code == requests.codes.ok:
    print("접속 성공")
    # print(req.text)
    html = BeautifulSoup(req.text, "html.parser")
    # html.select("")
    # 검색어에 해당하는 모든 요소를 - 단일 html객체들이 담긴 리스트
    # html.select_one("")
    # 검색어에 해당하는 요소 중 제일 첫번째 - 단일 html객체

    span = html.select(".PM_CL_realtimeKeyword_list_base span.ah_k")
    for item in span:
        # print(item['class']) # 태그의 속성 값은 dictionary라고 생각하고 다룬다
        print(item.text)  # 텍스트값은 .text로 접근
else:
    print("접속 실패")

    """
    셀렉터??? html요소를 선택하는 문자열
    html이 어떻게 구성되어 있느냐?
    html은 컨테이너 태그와 엠티 태그 - 태그안에 내용이 있느냐 없느냐
    container : <span data-title="대선">기사 제목</span>
    empty : <img src="이미지주소">

    html에서 얻고자하는 내용이 어디있느냐?
    1. 컨테이너 태그가 품고있는 내용
    2. 엠티태그나 컨테이너 태그의 속성값

    셀렉터는 3가지
    <p data-rel="http://www.naver.com" id="cont" class="text_mid">본문내용</p>
    tag : p
    id : #cont
    class : .text_mid

    다중 셀렉터
    1) p.text_mid span.contents : 붙여서 쓰면 ~인데 ~인것
    2) div p .content : 경로를 나열한다. 중간 경로 생략 가능
    3) div > p > .content : 경로를 나열한다. 중간 경로 생략 불가

    <a class="as_btn_press _PM_newsstand_total_type is_selected" href="#" role="tab" aria-selected="true" data-clk="nsd.all">전체 언론사</a>
    a.as_btn_press
    a._PM_newsstand_total_type
    a.as_btn_press._PM_newsstand_total_type
    """


