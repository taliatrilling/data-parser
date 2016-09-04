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


# print bycondition1.describe()
# print bycondition2.describe()
# print bycondition3.describe()
# print bycondition4.describe()
# print bycondition5.describe()
# print bycondition6.describe()

condition1 = pd.read_csv("condition1.csv",
    usecols = [13, 15])

dfcond1anger = pd.DataFrame(condition1, columns = ["CONDITION", "Q6"])

dfcond1_2anger = dfcond1anger.groupby(by = "CONDITION").get_group("1")

angerbycond1 = dfcond1_2anger["Q6"].str.lower()

angerbycond1_2 = angerbycond1.str.contains("anger", "angry")

#print angerbycond1_2

def anger1():
    anger = 0
    not_anger = 0
    for row in angerbycond1_2:
        if row:
            anger = anger + 1
        else: 
            not_anger = not_anger + 1
    print anger, not_anger


dfcond1envy = pd.DataFrame(condition1, columns = ["CONDITION", "Q6"])

dfcond1_2envy = dfcond1envy.groupby(by = "CONDITION").get_group("1")

envybycond1 = dfcond1_2envy["Q6"].str.lower()

envybycond1_2 = envybycond1.str.contains("envy", "envious")

def envy1():
    envy = 0
    not_envy = 0
    for row in envybycond1_2:
        if row:
            envy = envy + 1
        else: 
            not_envy = not_envy + 1
    print envy, not_envy

condition2 = pd.read_csv("condition1.csv",
    usecols = [13, 17])

dfcond2anger = pd.DataFrame(condition2, columns = ["CONDITION", "Q11"])

dfcond2_2anger = dfcond2anger.groupby(by = "CONDITION").get_group("2")

angerbycond2 = dfcond2_2anger["Q11"].str.lower()

angerbycond2_2 = angerbycond2.str.contains("anger", "angry")

def anger2():
    anger = 0
    not_anger = 0
    for row in angerbycond2_2:
        if row:
            anger = anger + 1
        else: 
            not_anger = not_anger + 1
    print anger, not_anger

dfcond2jealous = pd.DataFrame(condition2, columns = ["CONDITION", "Q11"])

dfcond2_2jealous = dfcond2jealous.groupby(by = "CONDITION").get_group("2")

jealousbycond2 = dfcond2_2jealous["Q11"].str.lower()

jealousbycond2_2 = jealousbycond2.str.contains("jealous", "jealousy")

def jealous2():
    jealous = 0
    not_jealous = 0
    for row in jealousbycond2_2:
        if row:
            jealous = jealous + 1
        else: 
            not_jealous = not_jealous + 1
    print jealous, not_jealous

jealous2()

print jealousbycond2_2


