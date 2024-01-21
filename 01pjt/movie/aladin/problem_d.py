import json
from pprint import pprint
def best_book(books_):
    for book in books_:
        bb = books_[0]
        if book['customerReviewRank'] >= bb['customerReviewRank']:
            bb = book
        else:
            pass
    return bb

    # 여기에 코드를 작성합니다.
book = open('data/books/*.json', encoding='utf-8')
book_detail = json.load(book)

pprint(book_detail)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    # print(best_book(books_list))
