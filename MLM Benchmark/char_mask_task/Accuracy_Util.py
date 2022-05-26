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

def calculate_pred_accuracy(test_path, pred_path):
    refs = []

    with open(test_path, encoding="utf8") as test:
        for line in test: 
            line = line.strip()
            refs.append(line)

    preds = []
    with open(pred_path, encoding="utf8") as test:
        for line in test: 
            line = line.strip()
            preds.append(line)

    accuracy = sentence_predict_accuracy(refs, preds)
    return accuracy