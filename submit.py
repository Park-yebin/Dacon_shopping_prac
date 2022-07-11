from modeling import prediction
from check import sample_submission

sample_submission['Weekly_Sales']=prediction
sample_submission.to_csv('submission.csv', index=False)