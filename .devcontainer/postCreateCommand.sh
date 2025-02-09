#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install git-flow
git flow init -d

# Add aliases
cp .devcontainer/.bash_aliases ~/.bash_aliases
source ~/.bashrc

# Install dependencies
mkdir .venv/
pipenv install --dev