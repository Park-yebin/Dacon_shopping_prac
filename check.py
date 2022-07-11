import pandas as pd

train=pd.read_csv('dataset/train.csv')
test=pd.read_csv('dataset/test.csv')
sample_submission=pd.read_csv('dataset/sample_submission.csv')

#change NA
train=train.fillna(0)

#add month column
def get_month(date):
    month=date[3:5]
    month=int(month)
    return month

train['Month']=train['Date'].apply(get_month)

#check holiday
def holiday_to_num(isholiday):
    if isholiday==True:
        num=1
    else:
        num=0
    return num

train['NumHoliday']=train['IsHoliday'].apply(holiday_to_num)
