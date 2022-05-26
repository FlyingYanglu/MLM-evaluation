import numpy as np
import random

def mask_sentence(jsentence, mask_token, mask_ratio):
    """
    function that used to mask one string of japanese sentence, replacing each character inside the sentence by mask token with mask ratio probability

    :param jsentence: japanese sentence in string
    :param mask_token: mask token used to mask character
    :param mask_ratio: probability to mask each individual character within the sentence

    """
    # generate mask
    sent_length = len(jsentence)
    mask = np.array(np.random.uniform(size=sent_length) < mask_ratio)
    
    # mask the jsentence with mask_token
    js_array = np.array(list(jsentence), dtype="<U"+str(len(mask_token)))
    original_token = js_array[mask]
    
    for i, mask_boolean in enumerate(mask):
        if mask_boolean:
            rand_num = random.random()
            if rand_num <= 0.8:
                js_array[i] = mask_token
            elif 0.8 < rand_num <= 0.9:
                js_array[i] = character_generator(1, RANGES)
            else:
                continue

    return js_array, original_token, mask

RANGES  =  [(0x4e00, 0x4f80),\
            (0x5000, 0x9fa0),\
            (0x3400, 0x4db0),\
            (0x30a0, 0x30f0) ]

def character_generator(length, ranges):
    res = ''
    for i in range(length):
        random_index = random.randint(0, len(ranges)-1)
        uni_range = ranges[random_index]
        res += chr(random.randint(uni_range[0], uni_range[1]))
    return res
