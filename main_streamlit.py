import pandas as pd
import streamlit as st

from src.models.coin_prediction_model import CoinPredictionModel
from src.providers.coin_gecko import Coin


def main():
    # Selector for choosing the coin
    coin_option = st.selectbox(
        "Select a coin to plot", options=[Coin.BITCOIN, Coin.ETHEREUM]
    )

    future_days = 10
    model = CoinPredictionModel(coin_option)
    predictions = model.predict(future_days)

    # Load historical data for plotting
    real_data = pd.read_csv(f"{CoinPredictionModel.DATA_PATH}/{coin_option.value}.csv")
    st.write(f"### {coin_option.value.upper()} Price Prediction")
    plot_predictions(real_data, predictions, future_days)


def plot_predictions(real_data, predictions, future_days):
    real_data["timestamp"] = pd.to_datetime(real_data["timestamp"])
    real_data.set_index("timestamp", inplace=True)

    # Create a DataFrame for predictions
    last_date = real_data.index[-1]
    prediction_dates = pd.date_range(start=last_date, periods=future_days + 1)[1:]
    prediction_df = pd.DataFrame(
        predictions, index=prediction_dates, columns=["Predicted Price"]
    )

    # Combine real data and predictions for plotting
    combined_df = pd.concat([real_data["price"], prediction_df], axis=1)
    combined_df.columns = ["Real Price", "Predicted Price"]

    # Plotting using st.line_chart
    st.line_chart(combined_df)

    # Display the combined data as a table
    st.write("### Detailed Data")
    st.dataframe(combined_df, use_container_width=True)


if __name__ == "__main__":
    main()
