import seaborn as sns
# 유럽 제조 차량 중 연비가 30.0 mpg 이상인 행을 추출하시오.
# 자동차 모델명, 연비, 제조 국가만 표시하고 연비가 높은 순으로 정리하시오.
# 위 조건에 맞게 원본 데이터를 업데이트하고 나머지 칼럼들은 삭제하시오.

mpg = sns.load_dataset('mpg')
#print(mpg.info())

mpg = (mpg.drop(columns=['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year'])
       .query('origin == "europe" and mpg >= 30.0').sort_values('mpg', ascending=False))

#print(
#    mpg[['origin', 'mpg', 'name']]
#    .query('origin == "europe" and mpg >= 30.0')
#    .sort_values('mpg', ascending=False))

print(mpg)
print(mpg.info())