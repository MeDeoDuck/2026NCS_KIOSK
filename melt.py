import seaborn as sns

mpg = sns.load_dataset("mpg")
print(mpg.head(3))
mpg_melt = mpg.head(3).melt().rename(columns={"variable": "column_name", "value": "value"}).drop(columns=['value'])
print(mpg_melt)