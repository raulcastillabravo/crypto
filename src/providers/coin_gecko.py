import pathlib
from enum import Enum, unique

import pandas as pd
import requests


@unique
class Coin(Enum):
    BITCOIN = "bitcoin"
    ETHEREUM = "ethereum"


class CoinGecko:
    URL = "https://api.coingecko.com/api/v3"
    DATA_PATH = "storage/data"

    def run(self, days: int = 30):
        for coin in Coin:
            df = self._get_historical_data(coin, days)
            self._save(df, coin)
        return df

    def _get_historical_data(self, coin: Coin, days: int = 30):
        url = f"{self.URL}/coins/{coin.value}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": days,
            "interval": "daily",
        }
        response = requests.get(url, params=params)
        data = response.json()

        df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

        return df

    def _save(self, df: pd.DataFrame, coin: Coin):
        pathlib.Path(self.DATA_PATH).mkdir(parents=True, exist_ok=True)
        path = f"{self.DATA_PATH}/{coin.value}.csv"
        df.to_csv(path, index=False)
