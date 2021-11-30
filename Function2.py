# Function2.py
# 함수를 정의
#def change(x):
#    x[0] = "H"

def change(x):
    #복사본을 지역변수로 만들기
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부 : ", x1)
        
#함수를 호출
wordlist = ["3", "A", "M"]
#Pass By Reference
change(wordlist)
print("함수 호출 후 ", wordlist)


#지역변수와 전역변수(이름 충돌)
x = 1
def func(a):
    return a+x

#호출
print(func(1))

def func2(a):
    x = 2
    return x+a

#호출
print(func2(1))


#전역변수를 읽기+쓰기할 경우 불변형식이며 global 키워드 사용
g = 1
def testScope(a):
    global g
    g = 2
    return g+a

#호출
print(testScope(1))
print("함수 호출 후 전역변호 g : ", g)