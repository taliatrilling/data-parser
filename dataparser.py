import pandas as pd
import numpy as np
import openpyxl as op

condition_sex_age = pd.read_csv("condition1.csv",
    usecols = [13, 85, 172])

df = pd.DataFrame(condition_sex_age, columns = ["CONDITION", "Sex:", "ACTUAL AGE"])

bycondition1 = df.groupby(by = "CONDITION").get_group("1").apply(pd.to_numeric)

bycondition2 = df.groupby(by = "CONDITION").get_group("2").apply(pd.to_numeric)

bycondition3 = df.groupby(by = "CONDITION").get_group("3").apply(pd.to_numeric)

bycondition4 = df.groupby(by = "CONDITION").get_group("4").apply(pd.to_numeric)

bycondition5 = df.groupby(by = "CONDITION").get_group("5").apply(pd.to_numeric)

bycondition6 = df.groupby(by = "CONDITION").get_group("6").apply(pd.to_numeric)

print bycondition1.describe()
print bycondition2.describe()
print bycondition3.describe()
print bycondition4.describe()
print bycondition5.describe()
print bycondition6.describe()
