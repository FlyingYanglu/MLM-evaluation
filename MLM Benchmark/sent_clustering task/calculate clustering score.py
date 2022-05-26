import sys


target_test = sys.argv[1]  # Test file argument
target_pred = sys.argv[2]  # MTed file argument

# Open the test dataset human translation file and detokenize the references
refs = []

with open(target_test, encoding="utf8") as test:
    for line in test: 
        line = line.strip()
        refs.append(line)

preds = []
with open(target_pred, encoding="utf8") as test:
    for line in test: 
        line = line.strip()
        preds.append(line)

def sentence_predict_accuracy(predicted_sents, original_sents):
    assert len(predicted_sents) == len(original_sents), 'number of predicted sentences does not match original sentences\n' +\
         'length of predicted_sent:' + str(len(predicted_sents)) + '\n' + 'length of original_sents:'+ str(len(original_sents))
    total_tokens = 0
    total_correct = 0
    for i in range(len(predicted_sents)):
        predicted_sent = predicted_sents[i]
        original_sent = original_sents[i]
        assert len(predicted_sent) == len(original_sent), "predicted token length is different"
        sentence_length = len(predicted_sent)
        for j in range(sentence_length):
            if predicted_sent[j] == original_sent[j]:
                total_correct += 1
            total_tokens += 1
    return total_correct / total_tokens

accuracy = sentence_predict_accuracy (refs, preds)
print("Prediction accuracy for MLM task:", accuracy)