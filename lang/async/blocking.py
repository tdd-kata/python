import time


def blocking_function():
    print("Starting blocking function")
    time.sleep(3)  # 3초 동안 코드 실행을 멈춥니다.
    print("Ending blocking function")


print("Before calling blocking function")
blocking_function()
print("After calling blocking function")
