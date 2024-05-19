#List1
myvar = "NEW"
mylist = [100, 200, 300, 400, 500]

print(mylist[0:5]) # 100, 200, 300, 400, 500
print(mylist[1:3]) # 200, 300

mylist.append(myvar) # myvar 추가
print(mylist)

mylist.insert(0, myvar) # 인덱스 2번째 자리에 myvar 삽입
print(mylist)

mylist.remove(myvar)
mylist.remove(myvar) # myvar 변수 값 삭제
print(mylist)

mylist.pop(0) # 맨 마지막 값 삭제
print(mylist)
#print(item_removed)

mylist.reverse() # 역순 출력 500, 400, 300, 200
print(mylist)

mylist.sort()
print(mylist) # 오름차순 정렬





