# Project: Crypto Price Prediction with Dev Containers

## Overview

This project leverages **Dev Containers** to create a reproducible development environment for fetching cryptocurrency data from the **CoinGecko API**, applying **linear regression**, and visualizing results using **Streamlit**.

## Features

- **Dev Containers**: Ensures a consistent development environment.
- **CoinGecko API Integration**: Retrieves real-time cryptocurrency data.
- **Linear Regression Model**: Analyzes historical price trends.
- **Streamlit Dashboard**: Interactive visualization of predictions.

## Requirements

- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/raulcastillabravo/crypto.git
   cd crypto
   ```
2. Open the project in VS Code.
3. If prompted, reopen in Dev Container, or manually select **Remote-Containers: Reopen in Container** from the command palette.

## Usage

1. **Fetch cryptocurrency data and train models**:
   ```bash
   python main.py
   ```
2. **Run the Streamlit dashboard**:
   ```bash
   streamlit run main_streamlit.py
   ```

## License

This project is licensed under the [MIT License](LICENSE).
