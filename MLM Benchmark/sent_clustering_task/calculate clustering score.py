import sys
from calculate_clustering_utils import calculate_dispersion, calculate_score

cls_output = sys.argv[1]  # json file argument

# Open the test dataset human translation file and detokenize the references


score = calculate_score(cls_output)
print("sent_clustering_task:", score)