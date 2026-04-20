import seaborn as sns
import pandas as pd 

# # 유럽 제조 차량 중 연비가 30.0 mpg 이상인 행을 추출하시오.
# # 자동차 모델명, 연비, 제조 국가만 표시하고 연비가 높은 순으로 정리하시오.
# # 위 조건에 맞게 원본 데이터를 업데이트하고 나머지 칼럼들은 삭제하시오.

# mpg = sns.load_dataset('mpg')
# # print(mpg.info())

# mpg = (mpg.drop(columns=['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year'])
#        .query('origin == "europe" and mpg >= 30.0').sort_values('mpg', ascending=False))
# print(mpg)

# print(
#    mpg[['origin', 'mpg', 'name']]
#    .query('origin == "europe" and mpg >= 30.0')
#    .sort_values('mpg', ascending=False))

# print(mpg.iloc[1:4, [0, 2]])
# print(mpg)

# mpg = sns.load_dataset('mpg')
# group_mpg = pd.DataFrame(mpg.groupby(by='origin'))
# print(group_mpg)
# print(mpg['origin'].nunique())
# print(mpg.describe())

# def squares(n):
#     return n*n

# items = [
#     [100, 95, 70],
#     [80, 75, 100],
#     [90, 85, 99]
# ]
# df_items = pd.DataFrame(items, index=[1, 2, 3], columns=['a', 'b', 'c'])
# print(df_items)
# print(df_items.apply(lambda n : n * n))

# 6개의 결측치가 있다 => 1. 마력 컬럼을 날린다. 2. 6개의 값을 채워 넣음 / 6개의 행을 날린다

mpg = sns.load_dataset('mpg')
print(mpg.info())
# mpg.dropna(subset=['horsepower'], inplace=True) # 원본 업데이트
# print(mpg.info())
# mpg_cleean = mpg.dropna(subset=['horsepower']) # 사본 생성
# print(mpg_cleean.info())

hp_median = mpg['horsepower'].median()
mpg_filled = mpg.copy()
mpg_filled['horsepower'] = mpg_filled['horsepower'].fillna(hp_median)
print(mpg_filled.info())