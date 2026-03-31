import time

# 한 함수에 시간 측정 두 번 넣으면 단일 책임 원칙 위반
def time_measure_decorator(f): # f : 데코레이터가 적용될 함수
    def wrapper(*args): # *args: 가변인자, 함수의 인자 개수가 정해지지 않았을 때 사용
                        # "kwargs": dictionary로 받아라(key, value)   
        s = time.time() # 이 안에는 외부에서 안보임
        result = f(*args)  
        e = time.time()
        print(f"Time taken to execute {f.__name__}: {e - s} seconds")
        return result
    return wrapper

# @time_measure_decorator
def one_to_n_loop(m):
    total = 0
    for i in range(1, m+1):
        total += i
    return total

# @time_measure_decorator
def one_to_n_formula(m):
    return m * (m + 1) // 2

n = 10000000
# print(one_to_n_loop(n))
# print(one_to_n_formula(n))

NUMBER = int(input("Enter a number: "))
func = time_measure_decorator(one_to_n_formula)
print(func(NUMBER))