from generate_dataset import generate_data
import sys
import os

target_location = sys.argv[1]  # json file argument

# Open the test dataset human translation file and detokenize the references


generate_data(target_location, os.getcwd())
print('dataset stored under', os.getcwd())