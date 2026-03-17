import numpy as np
import pandas as pd

items = [40, 7, 99, -3]
print(np.sum(items))
print(np.mean(items))
print(np.max(items))
print(np.min(items))
print(np.median(items))
print(np.var(items))
print(np.std(items))





# # loop 돌리기
# items = [40, 7, 99, -3]
# items_new = []
# for item in items:
#     items_new.append(item+5)
# print(items_new)

# # map 함수
# items = [40, 7, 99, -3]
# items = list(map(lambda i:i+5, items))
# print(items)

# # numpy 활용
# data1 = np.array([40, 7, 99, -3])
# print(data1 + 5)
# print(data1 * 3)
# print(data1 > 14)


# # 혼자 type이 다른 경우
# # 파이썬에서는 오류는 안남
# # 단, 전부 float으로 바뀜
# # string > float > int
#
# # data1 = np.array([40, 30.0, 20, 10])
# # data1 = np.array([40, 30, 20, 10], dtype=float)
# data1 = np.array([40, 30.0, "INHA", 10])
#
# print(data1)
#
# data2 = np.array([[1, 2], [3, 4]])
# print(data2)
#
# # 3개의 빌딩, 4 x 2
# data3 = np.zeros((3, 4, 2))
# print(data3)
#
# data4 = np.ones((8))
# print(data4)
#
# print(data1.dtype, data2.dtype, data3.dtype, data4.dtype)
# print(data1.ndim, data2.ndim, data3.ndim, data4.ndim)
# print(data1.shape, data2.shape, data3.shape, data4.shape)
#
# # size, T, itemsize, ...
#
#
#
# # arrange, full, linspace, ..., np.random, rand()
# # np.dim => dimension
# # np.dtype => datatype
#
# # data = [10, 20, 30, 40]
# # average = pd.Series(data).mean()
# # print(average)
#
# # data = [10, 20, 30, 40]
# # average = np.mean(data)
# # print(average)
# # 전체 주석 ctrl + /
#
# ## 라이브러리 활용 => 느려서 개발에 안씀
# #import statistics
# #data = [10, 20, 30, 40]
# #average = statistics.average(data)
# #print(average)