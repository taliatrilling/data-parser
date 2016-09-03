import pandas as pd
import numpy as np
import openpyxl as op

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#above 4 lines of code via http://stackoverflow.com/questions/11707586/python-pandas-widen-output-display

condition_sex_age = pd.read_csv("condition1.csv",
    usecols = [13, 85, 172])

df = pd.DataFrame(condition_sex_age, columns = ["CONDITION", "Sex:", "ACTUAL AGE"])


#data sorted by condition: 

bycondition1 = df.groupby(by = "CONDITION").get_group("1")

bycondition2 = df.groupby(by = "CONDITION").get_group("2")

bycondition3 = df.groupby(by = "CONDITION").get_group("3")

bycondition4 = df.groupby(by = "CONDITION").get_group("4")

bycondition5 = df.groupby(by = "CONDITION").get_group("5")

bycondition6 = df.groupby(by = "CONDITION").get_group("6")


#data sorted by condition and gender 

bycondition1gender1 = df.groupby(by = "CONDITION").get_group("1").groupby(by = "Sex:").get_group("1")

bycondition1gender2 = df.groupby(by = "CONDITION").get_group("1").groupby(by = "Sex:").get_group("2")

bycondition2gender1 = df.groupby(by = "CONDITION").get_group("2").groupby(by = "Sex:").get_group("1")

bycondition2gender2 = df.groupby(by = "CONDITION").get_group("2").groupby(by = "Sex:").get_group("2")

bycondition3gender1 = df.groupby(by = "CONDITION").get_group("3").groupby(by = "Sex:").get_group("1")

bycondition3gender2 = df.groupby(by = "CONDITION").get_group("3").groupby(by = "Sex:").get_group("2")

bycondition4gender1 = df.groupby(by = "CONDITION").get_group("4").groupby(by = "Sex:").get_group("1")

bycondition4gender2 = df.groupby(by = "CONDITION").get_group("4").groupby(by = "Sex:").get_group("2")

bycondition5gender1 = df.groupby(by = "CONDITION").get_group("5").groupby(by = "Sex:").get_group("1")

bycondition5gender2 = df.groupby(by = "CONDITION").get_group("5").groupby(by = "Sex:").get_group("2")

bycondition6gender1 = df.groupby(by = "CONDITION").get_group("6").groupby(by = "Sex:").get_group("1")

bycondition6gender2 = df.groupby(by = "CONDITION").get_group("6").groupby(by = "Sex:").get_group("2")


#data sorted by condition and age

bycondition1age = pd.DataFrame(bycondition1, columns = ["ACTUAL AGE"]).apply(pd.to_numeric)

bycondition2age = pd.DataFrame(bycondition2, columns = ["ACTUAL AGE"]).apply(pd.to_numeric)

bycondition3age = pd.DataFrame(bycondition3, columns = ["ACTUAL AGE"]).apply(pd.to_numeric)

bycondition4age = pd.DataFrame(bycondition4, columns = ["ACTUAL AGE"]).apply(pd.to_numeric)

bycondition5age = pd.DataFrame(bycondition5, columns = ["ACTUAL AGE"]).apply(pd.to_numeric)

bycondition6age = pd.DataFrame(bycondition6, columns = ["ACTUAL AGE"]).apply(pd.to_numeric)


#functions that indicate the distribution of age bands per condition

def age_bands1():
    countband1 = 0
    countband2 = 0
    countband3 = 0
    countband4 = 0
    countband5 = 0
    countband6 = 0
    for row in bycondition1age["ACTUAL AGE"]:
        if row >= 18 and row <= 29:
            countband1 = countband1 + 1
        elif row >= 30 and row <= 39:
            countband2 = countband2 + 1
        elif row >= 40 and row <= 49:
            countband3 = countband3 + 1
        elif row >= 50 and row <= 59:
            countband4 = countband4 + 1
        elif row >= 60 and row <= 69:
            countband5 = countband5 + 1
        elif row >=70:
            countband6 = countband6 + 1 
    print "Ages 18-29 =", countband1, "Ages 30-39 =", countband2, "Ages 40-49 =", countband3, "Ages 50-59 =", countband4, "Ages 60-69 =", countband5, "Ages 70+ =", countband6

def age_bands2():
    countband1 = 0
    countband2 = 0
    countband3 = 0
    countband4 = 0
    countband5 = 0
    countband6 = 0
    for row in bycondition2age["ACTUAL AGE"]:
        if row >= 18 and row <= 29:
            countband1 = countband1 + 1
        elif row >= 30 and row <= 39:
            countband2 = countband2 + 1
        elif row >= 40 and row <= 49:
            countband3 = countband3 + 1
        elif row >= 50 and row <= 59:
            countband4 = countband4 + 1
        elif row >= 60 and row <= 69:
            countband5 = countband5 + 1
        elif row >=70:
            countband6 = countband6 + 1 
    print "Ages 18-29 =", countband1, "Ages 30-39 =", countband2, "Ages 40-49 =", countband3, "Ages 50-59 =", countband4, "Ages 60-69 =", countband5, "Ages 70+ =", countband6         

def age_bands3():
    countband1 = 0
    countband2 = 0
    countband3 = 0
    countband4 = 0
    countband5 = 0
    countband6 = 0
    for row in bycondition3age["ACTUAL AGE"]:
        if row >= 18 and row <= 29:
            countband1 = countband1 + 1
        elif row >= 30 and row <= 39:
            countband2 = countband2 + 1
        elif row >= 40 and row <= 49:
            countband3 = countband3 + 1
        elif row >= 50 and row <= 59:
            countband4 = countband4 + 1
        elif row >= 60 and row <= 69:
            countband5 = countband5 + 1
        elif row >=70:
            countband6 = countband6 + 1 
    print "Ages 18-29 =", countband1, "Ages 30-39 =", countband2, "Ages 40-49 =", countband3, "Ages 50-59 =", countband4, "Ages 60-69 =", countband5, "Ages 70+ =", countband6         

def age_bands4():
    countband1 = 0
    countband2 = 0
    countband3 = 0
    countband4 = 0
    countband5 = 0
    countband6 = 0
    for row in bycondition4age["ACTUAL AGE"]:
        if row >= 18 and row <= 29:
            countband1 = countband1 + 1
        elif row >= 30 and row <= 39:
            countband2 = countband2 + 1
        elif row >= 40 and row <= 49:
            countband3 = countband3 + 1
        elif row >= 50 and row <= 59:
            countband4 = countband4 + 1
        elif row >= 60 and row <= 69:
            countband5 = countband5 + 1
        elif row >=70:
            countband6 = countband6 + 1 
    print "Ages 18-29 =", countband1, "Ages 30-39 =", countband2, "Ages 40-49 =", countband3, "Ages 50-59 =", countband4, "Ages 60-69 =", countband5, "Ages 70+ =", countband6         

def age_bands5():
    countband1 = 0
    countband2 = 0
    countband3 = 0
    countband4 = 0
    countband5 = 0
    countband6 = 0
    for row in bycondition5age["ACTUAL AGE"]:
        if row >= 18 and row <= 29:
            countband1 = countband1 + 1
        elif row >= 30 and row <= 39:
            countband2 = countband2 + 1
        elif row >= 40 and row <= 49:
            countband3 = countband3 + 1
        elif row >= 50 and row <= 59:
            countband4 = countband4 + 1
        elif row >= 60 and row <= 69:
            countband5 = countband5 + 1
        elif row >=70:
            countband6 = countband6 + 1 
    print "Ages 18-29 =", countband1, "Ages 30-39 =", countband2, "Ages 40-49 =", countband3, "Ages 50-59 =", countband4, "Ages 60-69 =", countband5, "Ages 70+ =", countband6         

def age_bands6():
    countband1 = 0
    countband2 = 0
    countband3 = 0
    countband4 = 0
    countband5 = 0
    countband6 = 0
    for row in bycondition6age["ACTUAL AGE"]:
        if row >= 18 and row <= 29:
            countband1 = countband1 + 1
        elif row >= 30 and row <= 39:
            countband2 = countband2 + 1
        elif row >= 40 and row <= 49:
            countband3 = countband3 + 1
        elif row >= 50 and row <= 59:
            countband4 = countband4 + 1
        elif row >= 60 and row <= 69:
            countband5 = countband5 + 1
        elif row >=70:
            countband6 = countband6 + 1 
    print "Ages 18-29 =", countband1, "Ages 30-39 =", countband2, "Ages 40-49 =", countband3, "Ages 50-59 =", countband4, "Ages 60-69 =", countband5, "Ages 70+ =", countband6         

