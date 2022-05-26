import sys
from Accuracy_Util import calculate_pred_accuracy

target_test = sys.argv[1]  # Test file argument
target_pred = sys.argv[2]  # MTed file argument

# Open the test dataset human translation file and detokenize the references


accuracy = calculate_pred_accuracy(target_test, target_pred)
print("Prediction accuracy for MLM task:", accuracy)