import numpy as np
from datasets import Dataset
from Mask_Util import mask_sentence, default_concat
import os
import json
import csv
from tqdm import tqdm

def generate_data(data_loc, output_dir, generate_txt = False, generate_dataset = False, generate_json = True, combine = True, lang = "jp", concat_method=default_concat):
    '''
    Generate dataset for the mask filling task.
    :param data_loc: data_loc to the original japanese text file. Each line should contain exactly one japanses sentence.
    :param output_dir: directory to which you want to save the generated dataset
    :param generate_txt: default to True, return the masked japanese text file and a file containing the original tokens.
    :param generate_dataset: whether to turn the masked sentences into a dataset using datasets lib
    :param generate_json: whether to generate a json file to hold all generated data, default to True
    :param combine: whether to combine the masked and ori_sentence
    :param lang: currently support "jp" and "en"
    :param concat_method: func that takes in masked_sent, original_sent, and return concatenated sentence, default to our method, which is masked_sent + " <LM> " + original_sent 
    '''
    with open(data_loc, 'r', encoding = 'UTF-8') as inp:
        text_list = [line.strip() for line in inp]

    masked_c_list = []
    original_tokens = []
    mask_list = []

    # TODO: need to incorporate tokenizer 
    for line in tqdm(text_list):
        
        masked, original_token, mask = mask_sentence(line, '[MASK]', 0.15, lang=lang)
        masked_c_list.append(masked)
        original_tokens.append(original_token)
        mask_list.append(mask)

    if generate_dataset:
        # Put everything into dictionay and use dataset lib to convert it to dataset.
        res_dict = {"Masked_sentence": masked_c_list, "original_tokens":original_tokens, "mask": mask_list}
        visual_novel_dataset = Dataset.from_dict(res_dict)

        new_dir_name = "Generated_Dataset"
        target_path = os.path.join(output_dir, new_dir_name)
        print('generating dataset under: ' + target_path)
        if not os.path.isdir(target_path):
            os.mkdir(target_path)
        visual_novel_dataset.save_to_disk(target_path)

    if generate_json:
        
        mask_tolist = list(map(np.ndarray.tolist, mask_list))
        res_dict = {"Masked_sentence": masked_c_list, "original_tokens":original_tokens, "mask": mask_tolist}
        res_dict = {"data": [{"Masked_sentence": masked, "original_tokens":original, "mask":mask} for masked, original, mask in zip(masked_c_list, original_tokens, mask_tolist)]}
        new_dir_name = "json_info"
        target_path = os.path.join(output_dir, new_dir_name)
        print('generating json file under: ' + target_path)
        if not os.path.isdir(target_path):
            os.mkdir(target_path)
        with open(os.path.join(target_path, "data_info.json"), "w", encoding="utf-8") as f:
            json.dump(res_dict, f)

    masked_list_s =  [" ".join(line) for line in masked_c_list]
    original_tokens_s = [" ".join(line) for line in original_tokens]

    if generate_txt:
        print('generating txt file under: ' + os.path.join(output_dir, "masked_sentence.txt"))
        textfile = open(os.path.join(output_dir, "masked_sentence.txt"), "w", encoding="utf-8")
        for element in masked_list_s:
            textfile.write(element + "\n")
        
        print('generating txt file under: ' + os.path.join(output_dir, "original_character.csv"))
        textfile = open(os.path.join(output_dir, "original_character.txt"), "w", encoding="utf-8")
        for element in original_tokens_s:
            textfile.write(element + "\n")

        print('generating txt file under: ' + os.path.join(output_dir, "mask.csv"))
        with open(os.path.join(output_dir, "mask.csv"), "w", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            for element in mask_list:
                writer.writerow(element)

    if combine:
        print('generating combined file under: ' + os.path.join(output_dir, "concatenated.txt"))
        textfile = open(os.path.join(output_dir, "concatenated.txt"), "w", encoding="utf-8")
        
        for masked_sent, ori_sent in zip(masked_list_s, text_list):
            concatenated_sent = concat_method(masked_sent, ori_sent)
            textfile.write(concatenated_sent + "\n")

