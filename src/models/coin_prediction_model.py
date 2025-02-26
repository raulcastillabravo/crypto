import pathlib

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from src.providers.coin_gecko import Coin


class CoinPredictionModel:
    DATA_PATH = "storage/data"
    MODEL_PATH = "storage/models"

    _coin: Coin = None
    _model: LinearRegression = None

    def __init__(self, coin: Coin):
        self._coin = coin
        self._model = LinearRegression()
        self._load_model()

    def train(self):
        df = self._load_data()
        df_scaled, scaler = self._preprocess_data(df)
        X = df_scaled[:-1]
        y = df_scaled[1:]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        self._model.fit(X_train, y_train)
        self._save_model(scaler)
        return self._model.score(X_test, y_test)

    def predict(self, future_days: int):
        scaler = joblib.load(f"{self.MODEL_PATH}/{self._coin.value}_scaler.pkl")
        df = self._load_data()
        df_scaled, _ = self._preprocess_data(df)
        last_data = df_scaled[-1].reshape(1, -1)
        predictions = []
        for _ in range(future_days):
            next_pred = self._model.predict(last_data)
            predictions.append(next_pred[0])
            last_data = next_pred
        predictions = scaler.inverse_transform(predictions)
        return predictions

    def _load_data(self):
        path = f"{self.DATA_PATH}/{self._coin.value}.csv"
        df = pd.read_csv(path)
        return df

    def _preprocess_data(self, df: pd.DataFrame):
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df.set_index("timestamp", inplace=True)
        scaler = MinMaxScaler()
        df_scaled = scaler.fit_transform(df)
        return df_scaled, scaler

    def _save_model(self, scaler):
        pathlib.Path(self.MODEL_PATH).mkdir(parents=True, exist_ok=True)
        joblib.dump(self._model, f"{self.MODEL_PATH}/{self._coin.value}_model.pkl")
        joblib.dump(scaler, f"{self.MODEL_PATH}/{self._coin.value}_scaler.pkl")

    def _load_model(self):
        model_path = f"{self.MODEL_PATH}/{self._coin.value}_model.pkl"
        if pathlib.Path(model_path).exists():
            self._model = joblib.load(model_path)
