from sklearn.neighbors import LocalOutlierFactor
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class LocalOutlierDetection(BaseEstimator,TransformerMixin):
    
    def __init__(self, contamination=0.1, algorithm='auto', n_neighbors=20):
        self.contamination = contamination
        self.algorithm = algorithm
        self.n_neighbors = n_neighbors
        self._update_model()

    def fit_predict(self, data):
        return self.lof_model.fit_predict(data.reshape(-1, 1))

    def set_contamination(self, contamination):
        self.contamination = contamination
        self._update_model()
    
    def set_neighbors(self,n_neighbors):
        self.n_neighbors = n_neighbors
        self._update_model()

    def _update_model(self):
        self.lof_model = LocalOutlierFactor(contamination=self.contamination, algorithm=self.algorithm, n_neighbors=self.n_neighbors)


    def remove_outliers(self, df, column_name):
        df_temp = df[[column_name]].reset_index()
        df_temp = df_temp.dropna()

        #LOF modelini uygulama
        outlier_scores = self.lof_model.fit_predict(df_temp)

        # Outlier değerlerin indexlerini bulma
        outliers_index = df_temp.index[outlier_scores == -1]

        # Outlier değerleri mean ile doldurma
        df_corrected = df_temp.copy()
        mean_value = df_temp[column_name].mean()
        df_corrected.loc[outliers_index, column_name] = mean_value

        # Düzeltilmiş değerleri görüntüleme
        print("DEBUG: Aykırı Değerleri Düzeltildi:")
        print(df_corrected.loc[outliers_index])

        return df_corrected
