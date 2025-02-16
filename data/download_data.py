import kaggle
import os

# Set up Kaggle API (you need to get your Kaggle API key)
os.system("kaggle competitions download -c GiveMeSomeCredit -p data/")

print("Dataset downloaded successfully!")

