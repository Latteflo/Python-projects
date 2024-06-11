import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
from scipy.stats import randint
from sklearn.model_selection import RandomizedSearchCV

# Load the dataset
df = pd.read_csv(
    'D:/CyberSec/python-projects/Flight-Price-Guess-ML/Clean_Dataset.csv')

# Data Exploration
df.airline.value_counts()
df.source_city.value_counts()
df.destination_city.value_counts()
df.departure_time.value_counts()
df.arrival_time.value_counts()
df.stops.value_counts()
df['duration'].min()
df['duration'].median()
df['duration'].max()
df.price.value_counts()
df['class'].value_counts()

# Data Cleaning
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

# Convert the class column to binary
df['class'] = df['class'].apply(lambda x: 1 if x == 'Economy' else 0)

# Drop unnecessary columns
df.stops = pd.factorize(df.stops)[0]

# Drop unnecessary columns
df = df.join(pd.get_dummies(df.airline, prefix='airline')
             ).drop('airline', axis=1)
df = df.join(pd.get_dummies(df.source_city, prefix='source')
             ).drop('airline', axis=1)
df = df.join(pd.get_dummies(df.destination_city, prefix='destination')
             ).drop('airline', axis=1)
df = df.join(pd.get_dummies(df.arrival_time, prefix='arrival')
             ).drop('airline', axis=1)
df = df.join(pd.get_dummies(df.departure_time, prefix='departure')
             ).drop('airline', axis=1)

# Split dataset into features and target variable
X, y = df.drop('price', axis=1).df.price

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Split the data into training and test sets
reg = RandomForestRegressor()
reg.fit(x_train, y_train)
reg.score(x_test, y_test)

# Predict the test set
Y_pred = reg.predict(x_test)

# Evaluate the model
print('R2 Score:', r2_score(y_test, Y_pred))
print('Mean Absolute Error:', mean_absolute_error(y_test, Y_pred))
print('Mean Squared Error:', mean_squared_error(y_test, Y_pred))
print('Root Mean Squared Error:', math.sqrt(
    mean_squared_error(y_test, Y_pred)))

# Plot the results
plt.scatter(y_test, Y_pred)
plt.xlabel('Actual Flight Price')
plt.ylabel('Predicted Flight Price')
plt.title('Actual Price vs Predicted Price')

# Feature Importance
df.price.describe()

# Feature Importance
importances = dict(zip(reg.feature_names_in_, reg.feature_importances_))
sorted_importances = sorted(
    importances.items(), key=lambda x: x[1], reverse=True)

# Plot the feature importances
df.days_left.describe()
plt.figure(figsize=(10, 6))
plt.bar([x[0] for x in sorted_importances[:10]], [x[1]
        for x in sorted_importances[:10]])

# Hyperparameter Tuning with Grid Search
reg = RandomForestRegressor(n_jobs=1)

param_grid = {
    'n_estimators': [100, 200, 300, 1000],
    'max_depth': [None, 5, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt']
}

grid_search = GridSearchCV(reg, param_grid, cv=5)
grid_search.fit(x_train, y_train)

best_params = grid_search.best_params_

# Hyperparameter tuning using RandomizedSearchCV
param_dist = {
    'n_estimators': randint(100, 300),
    'max_depth': [None, 5, 10, 20, 30, 40, 50],
    'min_samples_split': randint(2, 11),
    'min_samples_leaf': randint(2, 5),
    'max_features': [1.0, 'auto', 'sqrt']
}

reg = RandomForestRegressor(n_jobs=1)

random_search = RandomizedSearchCV(
    estimator=reg, param_distributions=param_dist, n_iter=100, cv=3,
    scoring='neg_mean_squared_error', verbose=1, random_state=10, n_jobs=1)

random_search.fit(x_train, y_train)

# Best model from RandomizedSearchCV
best_regressor = random_search.best_estimator_

best_regressor.score(x_test, y_test)
