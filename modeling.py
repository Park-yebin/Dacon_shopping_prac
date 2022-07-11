from sklearn.linear_model import LinearRegression
from check import train, test

lr=LinearRegression()

train=train.drop(columns=['id','Date','IsHoliday'])
test=test.drop(columns=['id','Date','IsHoliday'])

x_train=train.drop(columns=['Weekly_Sales'])
y_train=train[['Weekly_Sales']]

lr.fit(x_train, y_train)
prediction=lr.predict(test)
print(prediction[:10])