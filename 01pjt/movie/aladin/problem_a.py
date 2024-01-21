import json
from pprint import pprint


def book_info(book):
    book_info_dict = {'id' : book['id'],
                      'author' : book['author'],
                      'priceSales' : book['priceSales'],
                      'description' : book['description'],
                      'cover' : book['cover'],
                      'categoryId' : book['categoryId'],
                      'title' : book['title']}
    return book_info_dict
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
