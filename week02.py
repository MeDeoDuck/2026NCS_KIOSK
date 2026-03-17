data = [10, 20, 30, 40]
hap, count = 0, 0
for d in data:
    hap += d
    count += 1
average = hap/count
print(average)

# 파이썬 자체 함수 사용
data = [10, 20, 30, 40]
average = sum(data) / len(data)
print(average)

# 라이브러리 활용
import statistics
data = [10, 20, 30, 40]
average = statistics.average(data)
print(average)