# DemoStr.py
#print( dir(str) )

names = ["전우치", "홍길동", "이순신"]
for name in names:
    print("안녕하세요 {0}님 추운 겨울입니다.".format(name))
    print("="*40)
    
strA = "python is very powerful"
print( len(strA) )
print( strA.capitalize() )
print( strA.count("p") )
print( strA.count("p", 7) )
print( "demo.ppt".endswith("ppt") )
print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )

strB = "<<<  spam and ham  >>>"
print(strB)
result = strB.strip("<> ")
print(result)
result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print("---다시 합치기---")
print(" ".join(lst))




#정규표현식
import re

string = "<<< data << data2"
#서브스티링("패턴", "", 데이터)
result = re.sub("<<<", "", string)
print(result)

#특정 문자열 패턴 : 숫자가 0번에서 N번 th
result = re.match("[0-9]*th", "35th")
result2 = re.search("[0-9]*th", "35th")
#매칭 오브젝트
print(result)
print(result2)

#약간 가동
print( result.group() )

#함정을 추가 : match는 정확하게 일치
#특정한 규칙을 정의(패턴)
result = re.match("[0-9]*th", "  35th")
#search는 내부에 있으면 
result2 = re.search("[0-9]*th", "  35th")
print(result)
print(result2)



#년도를 검색
result = re.match("\d{4}", "올해는 2021년입니다.")
result2 = re.search("\d{4}", "올해는 2021년입니다.")
print(result)
print(result2.group())

#우편번호를 검색
result = re.search("\d{5}", "우리 동네는 52300입니다.")
print(result.group())