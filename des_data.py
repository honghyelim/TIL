# 백화점 고객의 구매 데이터
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, RobustScaler,MinMaxScaler
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from imblearn.under_sampling import *
import warnings
warnings.filterwarnings("ignore")

x_train = pd.read_csv('C:/Users/hyelim/Desktop/X_train.csv',encoding='cp949')
x_test = pd.read_csv('C:/Users/hyelim/Desktop/X_test.csv',encoding='cp949')
y_train = pd.read_csv('C:/Users/hyelim/Desktop/y_train.csv',encoding='cp949')

df = pd.merge(x_train,y_train, how='inner',on='cust_id')
#0이 여자, 1이 남자
sns.countplot('gender',data=y_train)
df.info()

df.isnull().sum()
df['환불금액'] = df['환불금액'].fillna(0)
df.loc[df['환불금액'] != 0, '환불금액'] = 1

x_test['환불금액'] = x_test['환불금액'].fillna(0)
x_test.loc[x_test['환불금액'] != 0, '환불금액'] = 1

fig, ax = plt.subplots(figsize=(10,5))
sns.countplot(x='환불금액',data = df, hue = df['gender'],palette='GnBu',ax=ax)
plt.show()

t_list = df['주구매상품'].unique().tolist()
df['주구매상품'] = df['주구매상품'].map(lambda x : t_list.index(x))
t_list = df['주구매지점'].unique().tolist()
df['주구매지점'] = df['주구매지점'].map(lambda x : t_list.index(x))

t_list = x_test['주구매상품'].unique().tolist()
x_test['주구매상품'] = x_test['주구매상품'].map(lambda x : t_list.index(x))
t_list = x_test['주구매지점'].unique().tolist()
x_test['주구매지점'] = x_test['주구매지점'].map(lambda x : t_list.index(x))

x = df.drop(['gender'],axis=1)
y = df['gender']
x = RobustScaler().fit_transform(x)
features = ['cust_id', '총구매액', '최대구매액', '환불금액', '주구매상품', '주구매지점', '내점일수', '내점당구매건수','주말방문비율', '구매주기']
x = pd.DataFrame(x, columns=features)
y = pd.DataFrame(y,columns=['gender'])
df_train = pd.concat([x,y],axis=1)
df_train.head()

X=df_train.drop(['gender'],axis=1)
y=df_train['gender']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=10,shuffle=True)

print(X_train.shape)
print(X_test.shape)

#모델링 함수
def modeling(model,X_train,X_test,y_train,y_test):
    model.fit(X_train,y_train)
    pred = model.predict(X_test)
    metrics(y_test,pred)

#정확도, 정밀도, 재현율, f1-score, auroc 확인
def metrics(y_test,pred):
    accuracy = accuracy_score(y_test,pred)
    precision = precision_score(y_test,pred)
    recall = recall_score(y_test,pred)
    f1 = f1_score(y_test,pred)
    roc_score = roc_auc_score(y_test,pred,average='macro')
    print('정확도 : {0:.2f}, 정밀도 : {1:.2f}, 재현율 : {2:.2f}'.format(accuracy,precision,recall))
    print('f1-score : {0:.2f}, auc : {1:.3f}'.format(f1,roc_score))


#랜덤포레스트
rfc = RandomForestClassifier(n_estimators=500,random_state=30, max_depth=10,n_jobs=-1)
modeling(rfc,X_train,X_test,y_train,y_test)
#lightgbm
lgb = LGBMClassifier(n_estimators=1000,num_leaves=64,n_jobs=-1,boost_from_average=False,random_state=10)
modeling(lgb,X_train,X_test,y_train,y_test)

y_pred = xgb.predict(x_test)
r = rfc.predict_proba(x_test)[:,1]
ids = x_test['cust_id']

output = pd.DataFrame({'cust_id' : ids, 'gender': r})
output.to_csv('C:/Users/hyelim/Desktop/test_predictions.csv', index = False)
output.head()