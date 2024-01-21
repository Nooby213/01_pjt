import json
from pprint import pprint


def books_info(books,categories_list):
    top_20books = []
    for book in books:
        categories_Name = []
        book_info_dict = {}
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
        top_20books.append(book_info_dict)
    return top_20books


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
