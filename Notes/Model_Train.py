# ADJUST DATASET

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('upANDdown.csv')

X = df.drop('class', axis=1) # features
y=df['class'] #target value

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

# now we train
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

pipelines = {
    'lr': make_pipeline(StandardScaler(), LogisticRegression()),
    'rc': make_pipeline(StandardScaler(), RidgeClassifier()),
    'rf': make_pipeline(StandardScaler(), RandomForestClassifier()),
    'gb': make_pipeline(StandardScaler(), GradientBoostingClassifier()),
}

fitted_models = {}
for algo, pipeline in pipelines.items():
    model = pipeline.fit(X_train, y_train)
    fitted_models[algo] = model

# choosing the best model through an accuracy analysis
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pickle

for algo, model in fitted_models.items():
    yhat = model.predict(X_test)
    print(algo, accuracy_score(y_test.values, yhat),
          precision_score(y_test.values, yhat, average='binary', pos_label='up'),
          recall_score(y_test.values, yhat, average='binary', pos_label='up'))

#yhat = fitted_models['rf'].predict(X_test)
model = fitted_models['rf']





#################################################

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/coords.csv')

X = df.drop('class', axis=1) # features
y=df['class'] #target value

print(df.head())
print(df.tail())
print(df[df['class']=='up'])
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pickle

pipelines = {
    'lr': make_pipeline(StandardScaler(), LogisticRegression()),
    'rc': make_pipeline(StandardScaler(), RidgeClassifier()),
    'rf': make_pipeline(StandardScaler(), RandomForestClassifier()),
    'gb': make_pipeline(StandardScaler(), GradientBoostingClassifier()),
}

fit_models = {}
for algo, pipeline in pipelines.items():
    model = pipeline.fit(X_train, y_train)
    fit_models[algo] = model

for algo, model in fit_models.items():
    yhat = model.predict(X_test)
    print(algo, accuracy_score(y_test.values, yhat),
          precision_score(y_test.values, yhat, average='binary', pos_label='up'),
          recall_score(y_test.values, yhat, average='binary', pos_label='up'))
    
yhat = fit_models['rf'].predict(X_test)

with open('deadliftt.pkl', 'wb') as f:
    pickle.dump(fit_models['rf'], f)