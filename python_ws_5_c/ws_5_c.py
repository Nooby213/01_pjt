def restructure_word(word, arr):
    for char in word:
        if char.isdecimal() == True:
            a = int(char)
            while a:
                arr.pop()
                a -= 1
        else:
            arr.remove(char)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(list(map(str,original_word)))
print(arr)
result = restructure_word(word, arr)
print(result)
print(''.join(arr))
