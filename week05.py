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
# Open-Closed Principle : 확장에는 열려있고, 수정에는 닫혀있어야 한다. (기존 코드를 수정하지 않고 기능을 추가할 수 있어야 한다.)
# 클로져 => 데코레이터에 필수
# 클래스가 있어야 유지보수가 쉬움


# 연관 > 의존
# 의존
# [has a 관계](포함  관계) => 자동차 has a 엔진, 자동차 has a 바퀴, 자동차 has a 핸들
# compoosition => 같이 감 => 라이프 사이클
    # composition은 main에서 class가 들어가지 않음. orderProcessor has a menu
# aggregation => 따로 감(자동차 & 엔진은 has a 관계지만 약한 결합 관계)
# 생각하기에 따라 다름
# [is a 관계] => 자동차 is a 탈것, 자동차 is a 이동수단 => 상속 관계
# Menu 객체를 OrderProcessor 객체가 포함하는 경우 => composition
# Menu 객체를 OrderProcessor 객체가 참조하는 경우 => aggregation
