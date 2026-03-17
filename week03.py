import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset('mpg')
# print(mpg.head(3))
# print(mpg.tail(3))
# print(mpg.query('mpg > 17'))
mpg_asc = mpg.sort_values('mpg')
print(mpg_asc)

# 'displacement' 날리기
mpg_asx_disp_out = mpg_asc.drop(columns=['displacement'])
print(mpg_asx_disp_out)

# items = {
#     'a': [100, 80, 90],
#     'b': [95, 75, 85],
#     'c': [70, 100, 99]
# }

# items = [
#     [100, 95, 70],
#     [80, 75, 100],
#     [90, 85, 99]
# ]
# df_items = pd.DataFrame(items, index=[1, 2, 3], columns=['a', 'b', 'c'])
# print(df_items)
# df_items_melt = pd.melt(df_items).rename(columns={'variable': 'var', 'value': 'val'}).query('val >= 85')
# print(df_items_melt)

## 값의 변화가 없는 함수가 안전한 것 => 함수형 언어 사용

# scores = np.array([
#     # 국, 영, 수
#     [80, 100, 90], # A학생
#     [85, 70, 95], # B학생
#     [89, 85, 87] # C학생
# ])
#
# # axis: 0 --> 열, 1 --> 행
# print(f"전체 평균 : {np.mean(scores)}")
# print(f"국 영 수 과목별 평균 : {np.mean(scores, axis=0)}") # 열 기준 연산
# print(f"A학생, B학생, C학생 최고 점수 : {np.max(scores, axis=1)}") # 행 기준 연산

# items = [40, 7, 99, -3]
# print(np.sum(items))
# print(np.mean(items))
# print(np.max(items))
# print(np.min(items))
# print(np.median(items))
# print(np.var(items))
# print(np.std(items))
#
#
#


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