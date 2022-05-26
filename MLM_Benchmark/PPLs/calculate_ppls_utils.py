import sentencepiece as spm
from datasets import Dataset
import numpy as np

def prepare_dataset(path, save_dir, spmprocessor):
    """
    prepare custom dataset for evalutating PPLs.
    Note: spmprocessor must include '[MASK]' as a user defined token
    """
    
    mask_id = spmprocessor.encode('[MASK]')[1]
    with open(path, 'r', encoding = 'UTF-8') as inp:
        text_list = [line.strip() for line in inp]
    tokenized_list = spmprocessor.encode(text_list, out_type=int, enable_sampling=True, alpha=0.1, nbest_size=-1)
    data_dict = {'sent_index':[], 'input_ids': [], 'mask': []}
    for i, tokenized_sent in enumerate(tokenized_list):
        sent_index = i
        for j, id in enumerate(tokenized_sent):
            copied_sent = tokenized_sent.copy()
            copied_sent[j] = mask_id
            input_ids = copied_sent
            mask = [False]*len(tokenized_sent)
            mask[j] = True
            
            
            data_dict['sent_index'].append(j)
            data_dict['input_ids'].append(copied_sent)
            data_dict['mask'].append(mask)

    
    new_dataset = Dataset.from_dict(data_dict)
    new_dataset.save_to_disk(save_dir)

def calculate_ppls(sent_logits):
    """
    calculate pseudo-log-likelihood scores
    :param sent_logits: a list in which each position is log probability for each missing token in mask-prediction task. 
    """
    return np.sum(sent_logits)

def calculate_pppl(sent_logits_list):
    """
    calculate psudo perplexity
    """
    return np.exp(-np.average([calculate_ppls(sent) for sent in sent_logits_list]))

def dataset_to_logitsls(res_dataset):
    """
    turn result dataset to logits list
    expecting result dataset to contain 'sent_index', 'target_logit'
    """
    logits_ls = []
    length = 0
    for dt_pt in res_dataset:
        index, logits = dt_pt['sent_index'], dt_pt['target_logit']
        if index >= length:
            logits_ls.append([])
            length += 1
        logits_ls[index].append(logits)

    return logits_ls
