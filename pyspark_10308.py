# from pyspark.sql import functions as F
# df1 = db_employee
# df2 = db_dept

# df3 = df1.join(df2, df1['department_id'] == df2['id'], 'left')
# df4 = df3.drop(df2['id'])
# df5 = df4.groupBy('department').agg(
#     F.max('salary').alias('max_salary'),
# )

# df5 = df5.toPandas()

# max_salary_mkt = df5.loc[df5['department'] == 'marketing', 'max_salary'].values[0]
# max_salary_eng = df5.loc[df5['department'] == 'engineering', 'max_salary'].values[0]
# abs(max_salary_mkt - max_salary_eng)