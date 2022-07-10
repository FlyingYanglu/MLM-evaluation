import numpy as np
import random
from random_word import RandomWords

def default_concat(masked_sent, ori_sent):
    concatenated_sent = masked_sent + " <LM> " + ori_sent
    return concatenated_sent

def mask_sentence(sentence, mask_token, mask_ratio, lang="jp", sentence_as_list=None):
    """
    function that used to mask one string of japanese sentence, replacing each character inside the sentence by mask token with mask ratio probability

    :param sentence: sentence as string
    :param mask_token: mask token used to mask character
    :param mask_ratio: probability to mask each individual character in the sentence
    :param lang: "jp" or "en"
    :param sentence_as_list: 
    """
    if sentence_as_list is not None:
        assert type(sentence_as_list) == list
        
    if lang == "jp":
        # generate mask
        sentence_as_list = list(sentence)
        sent_length = len(sentence_as_list)
        mask = np.array(np.random.uniform(size=sent_length) < mask_ratio)
        
        # mask the sentence with mask_token
        original_token = []
        for i, word in enumerate(sentence_as_list):
            mask_rand = random.random()
            if mask_rand < mask_ratio:
                mask[i] = 1
                original_token.append(word)
                rand_num = random.random()
                if rand_num <= 0.8:
                    sentence_as_list[i] = mask_token
                elif 0.8 < rand_num <= 0.9:
                    sentence_as_list[i] = character_generator(1, RANGES)
                else:
                    continue

    elif lang == "en":
        sentence_as_list = sentence.split(" ")
        sent_length = len(sentence_as_list)
        mask = np.array(np.random.uniform(size=sent_length) < mask_ratio)
        original_token = []
        
        for i, word in enumerate(sentence_as_list):
            mask_rand = random.random()
            if mask_rand < mask_ratio:
                mask[i] = 1
                original_token.append(word)
                rand_num = random.random()
                if rand_num <= 0.8:
                    sentence_as_list[i] = mask_token
                elif 0.8 < rand_num <= 0.9:
                    
                    new_word = random_word(r)

                    sentence_as_list[i] = new_word
                    #print("this is new_word:", new_word)
                    #print("a")
                    #print(sentence_as_list[i])
                else:
                    continue

                
    

    return sentence_as_list, original_token, mask

RANGES  =  [(0x4e00, 0x4f80),\
            (0x5000, 0x9fa0),\
            (0x3400, 0x4db0),\
            (0x30a0, 0x30f0) ]

r = RandomWords()
def random_word(random_generator):
    new_word = None
    while not new_word:
        new_word = random_generator.get_random_word()
    return new_word

def character_generator(length, ranges):
    res = ''
    for i in range(length):
        random_index = random.randint(0, len(ranges)-1)
        uni_range = ranges[random_index]
        res += chr(random.randint(uni_range[0], uni_range[1]))
    return res
