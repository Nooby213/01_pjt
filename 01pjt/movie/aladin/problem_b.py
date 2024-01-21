import json
from pprint import pprint


def book_info(book,categories_list):
    categories_Name = []
    for categories_id in book['categoryId']:
        for data in categories_list:
            if int(data['id']) == int(categories_id):
                categories_Name.append(data['name'])
    book_info_dict = {'id' : book['id'],
                      'author' : book['author'],
                      'priceSales' : book['priceSales'],
                      'description' : book['description'],
                      'cover' : book['cover'],
                      'categoryId' : categories_Name,
                      'title' : book['title']}
    return book_info_dict
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
