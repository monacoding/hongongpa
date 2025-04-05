def say_hi() :
    print("Hi from hello.py")

print(f"hello.py실행 중 / __name__ ={__name__}")

if __name__ =="__main__" :
    print("hello.py 가 직접 실행 중이므로, 이 코드도 실행 됩니다.")
    say_hi

