import numpy as np
import json

def calculate_dispersion(all_cls):
    """
    Used to calcuate group dispersion

    :param all_cls: list of cls embeddings. Each list of embeddings should come from different class.
    """

    gim_list = []
    Am = 0
    for field in all_cls:
        gim = np.average(field, axis=0)
        gim_list.append(gim)
        sigma = 0
        for cls_pt in field:
            sigma += np.linalg.norm((cls_pt - gim), 2)
        Am += sigma
    gm = np.average(gim_list, axis=0)
    Bm = 0
    for gim in gim_list:
        Bm += np.linalg.norm((gm-gim), 2)
    Mm = Am/Bm

    return Mm

def calculate_score(path):
    with open(path, encoding="utf8") as file:
        data = json.load(file)

    all_cls = []
    for key in data['Fields'].keys():
        cls_list = data['Fields'][key]['cls_token']
        all_cls.append(np.array(cls_list))
    return calculate_dispersion(all_cls)