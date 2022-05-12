from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
import pandas as pd
from cassandra.data.trasformations.trasformations import create_model
from cassandra.model.modelEvaluation.plot import show_rsquared, show_mape, show_nrmse, show_rssd
import numpy as np


def logLog(df, X_trasformations_columns, X_columns, target, name_model, model_regression='linear', medias=[],
           organic=[], metric=None, return_metric=False, size=0.2, positive=False, random_state=42, force_coeffs=False, coeffs=[], intercept=0):
    if metric is None:
        metric = ['rsq_train', 'rsq_test', 'nrmse_train', 'nrmse_test', 'mape_train', 'mape_test', 'rssd']
    X_trasformations = df[X_trasformations_columns]
    X = df[X_columns]
    y = df[target]

    X_log = np.log(abs(X_trasformations) + 1)
    X_all = pd.merge(X_log, X, left_index=True, right_index=True)
    y_log = np.log(y + 1)

    X_train, X_test, y_train, y_test = train_test_split(X_all, y_log, test_size=size, random_state=random_state)

    if model_regression == 'linear':
        if medias or organic:
            model = create_model(medias, organic, LinearRegression(positive=positive))
        else:
            model = LinearRegression(positive=positive)
    elif model_regression == 'ridge':
        if medias or organic:
            ridge_number = len(medias + organic)
            model = create_model(medias, organic, Ridge(alpha=ridge_number, positive=positive))
        else:
            ridge_number = len(X.columns)
            model = Ridge(alpha=ridge_number, positive=positive)

    model.fit(X_train, y_train)

    if force_coeffs:
        model.intercept_ = intercept
        if coeffs:
            model.coef_ = np.array(coeffs)

    # Ask the model to predict on X_test without having Y_test
    # This will give you exact predicted values

    # We can use our NRMSE and MAPE functions as well

    # Create new DF not to edit the original one
    result = df

    # Create a new column with predicted values
    if medias or organic:
        # TODO
        result['prediction'] = np.exp(model.predict(np.log(abs(result) + 1))) - 1
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
    else:
        result['prediction'] = np.exp(model.predict(X_all)) - 1
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

    metrics_values = {}

    # Score returns the accuracy of the above prediction or R^2
    if 'rsq_train' in metric:
        try:
            rsq_train = show_rsquared(np.array(y_train), np.array(y_train_pred))
        except:
            rsq_train = -100
        if return_metric:
            metrics_values[name_model + '_rsq_train'] = rsq_train
        print(name_model, 'RSQ train: ', rsq_train)

    if 'rsq_test' in metric:
        try:
            rsq_test = show_rsquared(np.array(y_test), np.array(y_test_pred))
        except:
            rsq_test = -100
        if return_metric:
            metrics_values[name_model + '_rsq_test'] = rsq_test
        print(name_model, 'RSQ test: ', rsq_test)

    # Get the NRMSE values
    if 'nrmse_train' in metric:
        try:
            nrmse_train_val = show_nrmse(np.array(y_train), np.array(y_train_pred))
        except:
            nrmse_train_val = 100
        if return_metric:
            metrics_values[name_model + '_nrmse_train'] = nrmse_train_val
        print(name_model, 'NRMSE train: ', nrmse_train_val)

    if 'nrmse_test' in metric:
        try:
            nrmse_test_val = show_nrmse(np.array(y_test), np.array(y_test_pred))
        except:
            nrmse_test_val = 100
        if return_metric:
            metrics_values[name_model + '_nrmse_test'] = nrmse_test_val
        print(name_model, 'NRMSE test: ', nrmse_test_val)

    # Get the MAPE values
    if 'mape_train' in metric:
        try:
            mape_train_val = show_mape(np.array(y_train), np.array(y_train_pred))
        except:
            mape_train_val = 100
        if return_metric:
            metrics_values[name_model + '_mape_train'] = mape_train_val
        print(name_model, 'MAPE train: ', mape_train_val)

    if 'mape_test' in metric:
        try:
            mape_test_val = show_mape(np.array(y_test), np.array(y_test_pred))
        except:
            mape_test_val = 100
        if return_metric:
            metrics_values[name_model + '_mape_test'] = mape_test_val
        print(name_model, 'MAPE test: ', mape_test_val)

    if 'rssd' in metric:
        try:
            rssd_val = show_rssd(X, model.coef_)
        except:
            rssd_val = 100
        if return_metric:
            metrics_values[name_model + '_rssd'] = rssd_val
        print(name_model, 'RSSD: ', rssd_val)

    if metrics_values:
        return result, model, metrics_values
    else:
        return result, model