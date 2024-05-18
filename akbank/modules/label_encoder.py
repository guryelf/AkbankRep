from sklearn.preprocessing import LabelEncoder
from sklearn.base import BaseEstimator, TransformerMixin

class LabelEncoderWrapper(BaseEstimator,TransformerMixin):
    def __init__(self, handle_missing='error'):
        self.label_encoder = LabelEncoder()
        self.handle_missing = handle_missing

    def fit(self, data):
        if self.handle_missing == 'error' and data.isnull().any():
            raise ValueError("DEBUG: Missing values are not allowed.")
        self.label_encoder.fit(data)

    def transform(self, data):
        if self.handle_missing == 'error' and data.isnull().any():
            raise ValueError("DEBUG: Missing values are not allowed.")
        return self.label_encoder.transform(data)
