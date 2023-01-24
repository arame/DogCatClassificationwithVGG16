
def get_perc(amount, total_size):
    perc = round(amount / total_size * 100, 2)
    return perc

def get_dictionaries_from_list(list):
    dict_rev=dict(enumerate(list))
    new_dict = dict([(value, key) for key, value in dict_rev.items()])
    return new_dict, dict_rev
    