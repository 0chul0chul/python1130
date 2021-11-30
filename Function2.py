# Function2.py
# 함수를 정의
def change(x):
    x[0] = "H"
    
#함수를 호출
wordlist = ["3", "A", "M"]
change(wordlist)
print("함수 호출 후 ", wordlist)