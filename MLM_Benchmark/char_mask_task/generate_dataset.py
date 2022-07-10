import numpy as np
from datasets import Dataset
from Mask_Util import mask_sentence
import os

def generate_data(path, target_dir, generate_txt = True, generate_dataset = False, lang = "jp"):
    '''
    Generate dataset for the mask filling task.
    :param path: path to the original japanese text file. Each line should contain exactly one japanses sentence.
    :param target_dir: directory to which you want to save the generated dataset
    :param generate_txt: default to True, return the masked japanese text file and a file containing the original tokens.
    :param generate_dataset: whether to turn the masked sentences into a dataset using datasets lib
    :param lang: currently support "jp" and "en"
    '''
    with open(path, 'r', encoding = 'UTF-8') as inp:
        text_list = [line.strip() for line in inp]

    masked_c_list = []
    original_tokens = []
    mask_list = []

    # TODO: need to incorporate tokenizer 
    for line in text_list:
        
        masked, original_token, mask = mask_sentence(line, '[MASK]', 0.15, lang=lang)
        masked_c_list.append(masked)
        original_tokens.append(original_token)
        mask_list.append(mask)

    if generate_dataset:
        # Put everything into dictionay and use dataset lib to convert it to dataset.
        res_dict = {"Masked_sentence": masked_c_list, "original_tokens":original_tokens, "mask": mask_list}
        visual_novel_dataset = Dataset.from_dict(res_dict)

        new_dir_name = "Generated_Dataset"
        target_path = os.path.join(target_dir, new_dir_name)
        os.mkdir(target_path)
        visual_novel_dataset.save_to_disk(target_path)

    if generate_txt:
        masked_list_s =  ["".join(line) for line in masked_c_list]
        original_tokens_s = ["".join(line) for line in original_tokens]

        textfile = open(os.path.join(target_path, "masked_sentence.txt"), "w", encoding='UTF-8')
        for element in masked_list_s:
            textfile.write(element + "\n")
        textfile = open(os.path.join(target_path, "original_character.txt"), "w", encoding='UTF-8')
        for element in original_tokens_s:
            textfile.write(element + "\n")

