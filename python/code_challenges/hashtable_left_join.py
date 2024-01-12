from data_structures.hashtable import Hashtable


def left_join(synonyms: dict, antonyms: dict) -> list[list[str]]:
    if len(synonyms) == 0 or len(antonyms) == 0:
        return None

    outer_list = []

    for key, value in synonyms.items():
        inner_list = list()
        inner_list.append(key)
        inner_list.append(value)

        inner_list.append(antonyms[key]) if key in antonyms.keys() else inner_list.append("NONE")
        outer_list.append(inner_list)

    print(outer_list)
    return outer_list
