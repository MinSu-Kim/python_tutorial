import requests
from bs4 import BeautifulSoup
import os.path


def web():
    import webbrowser

    url = 'www.naver.com'
    webbrowser.open(url)


def web2():
    html2 = """
    <html>
     <head>
      <title>작품과 작가 모음</title>
     </head>
     <body>
      <h1>책 정보</h1>
      <p id="book_title">토지</p>
      <p id="author">박경리</p>

      <p id="book_title">태백산맥</p>
      <p id="author">조정래</p>

      <p id="book_title">감옥으로부터의 사색</p>
      <p id="author">신영복</p>
     </body>
    </html>
    """

    soup2 = BeautifulSoup(html2, "lxml")
    print("title \n{}\n".format(soup2.title))
    print("body \n{}\n".format(soup2.body))
    print("h1 \n{}".format(soup2.body.h1))
    print("p \n{}".format(soup2.find_all('p')))

    book_titles = soup2.find_all('p', {"id": "author"})
    authors = soup2.find_all('p', {"id": "book_title"})

    print("p : id \n{}".format(book_titles))
    print("p : id \n{}".format(authors))

    for book_title, author in zip(book_titles, authors):
        print(book_title.get_text() + '/' + author.get_text())

    print()
    print()
    print("CSS selector")
    print("body h1 \n{}".format(soup2.select('body h1')))
    print("body p \n{}".format(soup2.select('body p')))
    print("p \n{}".format(soup2.select('p')))
    print("p#author \n{}".format(soup2.select('p#author')))
    print("p#book_title \n{}".format(soup2.select('p#book_title')))
    for book_title in soup2.select('p#book_title'):
        print(book_title.get_text())


def html_write():
    html = """
        <!doctype html>
        <html>
          <head>
            <meta charset="utf-8">
            <title>사이트 모음</title>
          </head>
          <body>
            <p id="title"><b>자주 가는 사이트 모음</b></p>
            <p id="contents">이곳은 자주 가는 사이트를 모아둔 곳입니다.</p>
            <a href="http://www.naver.com" class="portal" id="naver">네이버</a> <br>
            <a href="https://www.google.com" class="search" id="google">구글</a> <br>
            <a href="http://www.daum.net" class="portal" id="danum">다음</a> <br>
            <a href="http://www.nl.go.kr" class="government" id="nl">국립중앙도서관</a>
          </body>
        </html>
        """
    # html_file("D:/workspace_python/python_tutorial/web_scraping/HTML_example_my_site.html", html)
    html_file_write("HTML_example_my_site_linux.html", html)


def html_write2():
    html = """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>줄 바꿈 테스트 예제</title>
      </head>
      <body>
      <p id="title"><b>대한민국헌법</b></p>
      <p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>
      <p id="content">제2조 <br/>①대한민국의 국민이 되는 요건은 법률로 정한다.<br/>②국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다.</p>
      </body>
    </html>
    """
    # html_file("D:/workspace_python/python_tutorial/web_scraping/br_example_constitution.html", html)
    html_file_write("br_example_constitution_linux.html", html)


def html_file_write(file_path, message):
    with open(file_path, 'w') as f:
        f.write(message)
        print(file_path, " write ~!")


def web3():
    # file_exist = os.path.isfile("D:/workspace_python/python_tutorial/web_scraping/HTML_example_my_site.html")
    file_exist = os.path.isfile("HTML_example_my_site_linux.html")
    if file_exist is False:
        html_write()
        print("file write")

    # f = open("D:/workspace_python/python_tutorial/web_scraping/HTML_example_my_site.html", encoding='utf8')
    with open("HTML_example_my_site_linux.html", encoding='utf8') as f:
        html3 = f.read()

    soup3 = BeautifulSoup(html3, 'lxml')
    print('soup3.select(\'a\') {}'.format(soup3.select('a')))
    print('soup3.select(\'a.portal\') {}'.format(soup3.select('a.portal')))
    print(soup3.select('html > body > a'))
    print(soup3.select('html > body > a.portal'))


def web4():
    # file_exist = os.path.isfile("D:/workspace_python/python_tutorial/web_scraping/br_example_constitution.html")
    file_exist = os.path.isfile("br_example_constitution_linux.html")
    if file_exist is False:
        html_write2()
        print("file write")

    # f = open("D:/workspace_python/python_tutorial/web_scraping/br_example_constitution.html", encoding='utf8')
    with open("br_example_constitution_linux.html", encoding='utf8') as f:
        html3 = f.read()

    soup3 = BeautifulSoup(html3, 'lxml')

    title = soup3.find('p', {'id':'title'})
    contents = soup3.find_all('p', {'id':'content'})

    print(title.get_text())
    for content in contents:
        # print(content.get_text())
        content1 = replace_newline(content)
        print(content1.get_text(), '\n')


def replace_newline(soup_html):
    br_to_newlines = soup_html.find_all('br')
    for br_to_line in br_to_newlines:
        br_to_line.replace_with('\n')
    return soup_html


def beautiful_soup():
    html = """<html><body><div><span>\
           <a href=http://www.naver.com>naver</a>\
           <a href=https://www.google.co.kr>google</a>\
           <a href=http://www.daum.net>daum</a>\
           </span></div></body></html>"""
    # BeautifulSoup를 이용하여 HTML 소스파싱
    soup = BeautifulSoup(html, 'lxml')
    # bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml.
    # Do you need to install a parser library? 오류발생하면 lxml 패키지 설치
    print(soup.prettify())
    print(soup.find('a'))
    print(soup.find('a').get_text())

    # print(soup.find_all('a'))
    site_names = soup.find_all('a')
    print("type {} ".format(type(site_names[0])))
    for site_name in site_names:
        print(site_name.get_text())


if __name__ == "__main__":
    # r = requests.get("https://www.google.co.kr")
    # print(r)
    # print(r.text[0:100])
    #
    # html = requests.get("https://www.google.co.kr").text
    # print(html[0:100])
    # beautiful_soup()
    #
    # html_write()
    # web()
    # web2()
    # web3()
    web4()
