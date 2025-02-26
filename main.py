from src.models.coin_prediction_model import CoinPredictionModel
from src.providers.coin_gecko import Coin, CoinGecko


def main():
    # Get historical data from CoinGecko
    coin_gecko = CoinGecko()
    coin_gecko.run(days=30)

    # Train the prediction model for Bitcoin
    bitcoin_model = CoinPredictionModel(Coin.BITCOIN)
    bitcoin_score = bitcoin_model.train()
    print(f"Bitcoin model trained with score: {bitcoin_score}")

    # Predict future values for Bitcoin
    future_days = 10
    bitcoin_predictions = bitcoin_model.predict(future_days)
    print(f"Bitcoin predictions for the next {future_days} days: {bitcoin_predictions}")

    # Train the prediction model for Ethereum
    ethereum_model = CoinPredictionModel(Coin.ETHEREUM)
    ethereum_score = ethereum_model.train()
    print(f"Ethereum model trained with score: {ethereum_score}")

    # Predict future values for Ethereum
    ethereum_predictions = ethereum_model.predict(future_days)
    print(
        f"Ethereum predictions for the next {future_days} days: {ethereum_predictions}"
    )


if __name__ == "__main__":
    main()
