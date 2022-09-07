import pandas as pd


def my_ensemble_fuctn(df_majority_class, df_minority_class, start, end):
    df_train = pd.concat([df_majority_class[start:end], df_minority_class], axis=0)

    X_train = df_train.drop('Churn', axis='columns')
    y_train = df_train.Churn
    
    return X_train, y_train

