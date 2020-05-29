# Part 1
# Name: Antoine Bonnet

import doctest
import random

def flatten_lists(nested):
    '''(list) -> list
    #Input: a list that can contain lists
    #Replaces any lists inside this list with their values.
    #Return the new version of this list, does not modify the input list.
    >>> flatten_lists(['apple', 0, ['banana', 12], 413])
    ['apple', 0, 'banana', 12, 413]
    >>> flatten_lists([[1, 2, 3], 4, [5, 6]])
    [1, 2, 3, 4, 5, 6]
    >>> flatten_lists([[0], [1, 2], 3])
    [0, 1, 2, 3]
    '''
    flat_list = [] #creates empty list
    for element in nested:
        if type(element) == list: #if element is a list
            for index in range(len(element)):
                flat_list.append(element[index]) #adds every element in list
        else:
            flat_list.append(element) #if element is not a list, adds element
    return flat_list

def flatten_dict(d):
    ''' (dict) -> list
    #Input: a dictionary where all values are non-negative integers
    #Returns a list from this dictionary, containing the keys of the
    #dictionary repeated v many times, where v is the value associated
    #with the key in the dictionary. The input dict is not modified
    >>> flatten_dict({'Lucian':1, 'Freud':2, 13:3})
    ['Lucian', 'Freud', 'Freud', 13, 13, 13]
    >>> flatten_dict({'LIBERAL':5,'NDP':2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    '''
    new_list = [] #creates empty list
    for key in d:
        associated_value = d.get(key) #gets associated value of each key
        for index in range(associated_value): #iterates n times for each value n
            new_list.append(key) #appends key in new list
    return new_list


def add_dicts(d1, d2):
    '''(dict, dict) -> dict
    #Input: two dictionaries where all the values are numbers
    #Merges the two dictionaries. If a key is in both dictionaries,
    #adds their values. Returns the resulting dictionary,
    #THe two input dictionaries are not modified
    >>> add_dicts({'a':5, 'b':2, 'd':-1},{'a':7, 'b':1, 'c':5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}
    '''
    new_dict = {} #creates empty dict
    for key_d1 in d1:
        value_d1 = d1.get(key_d1)
        new_dict[key_d1] = value_d1 #adds all entries in first dict
    for key_d2 in d2:
        value_d2 = d2.get(key_d2)
        if key_d2 in new_dict: #if key already in first dict
            corresp_value = new_dict.get(key_d2)
            new_dict[key_d2] = corresp_value + value_d2 #value increased
        else:
            new_dict[key_d2] = value_d2 #adds all new entries
    return new_dict

    
def get_all_candidates(ballots):
    ''' (list) -> list
    #takes a list as input (list of lists of strings, dictionaries
    with string keys or strings). returns all the unique strings 
    #in this list and its nested contents
    >>> get_all_candidates([{'GREEN':3, 'NDP':5},{'NDP':2, 'LIBERAL':4},['CPC','BLOC'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    '''
    new_list = []
    for element in ballots:
        if type(element) == str: #if element is a string
            if element in new_list:
                continue
            else:
                new_list.append(element) #adds all new elements
        elif type(element) == list: #if element is a list
            for list_value in element:
                if list_value in new_list:
                    continue
                else:
                    new_list.append(list_value) #adds all new elements
        elif type(element) == dict: #if element is a dict
            for key in element:
                if key in new_list:
                    continue
                else:
                    new_list.append(key) #adds all new keys
    return new_list

###################################################### winner/loser

def get_candidate_by_place(result, func):
    '''(dict, function) -> str
    #takes as input a dictionary with string keys and nonzero
    #integer values, evaluates the function (min or max) on
    #values and returns the corresponding key. Break ties randomly
    >>> result = {'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4}
    >>> random.seed(0)
    >>> get_candidate_by_place(result, min)
    'GREEN'
    >>> get_candidate_by_place(result, max)
    'CPC'
    >>> random.seed(1)
    >>> get_candidate_by_place(result, min)
    'LIBERAL'
    >>> get_candidate_by_place(result, max)
    'NDP'
    '''
    list_candidate = [] #empty list of candidates
    if len(result) == 0:
        return ''
    elif len(result) == 1:
        return flatten_dict(result)[0]
    else:
        extreme_value = func(result.values()) #gives the max or min value
        
        for key in result: #iterates through all keys in result
            if result[key] == extreme_value:
                list_candidate.append(key)
                #adds key(s) with max or min value to list
    random_index = random.randint(0, len(list_candidate)-1) #random choice
    return list_candidate[random_index]

    
def get_winner(result):
    '''(dict) -> str
    #Takes as input a dictionary with string keys, int values
    #returns the key with the greatest value. Breaks ties randomly
    >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'NDP'
    >>> get_winner({'Hitler': 56, 'Churchill': 90, 'Mussolini':61})
    'Churchill'
    '''
    return get_candidate_by_place(result, max) #gets max candidate

def last_place(result):
    '''(dict) -> str
    #Takes as input a dictionary with string keys, int values
    #returns the key with the least value. Breaks ties randomly
    >>> last_place({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 4})
    'LIBERAL'
    >>> last_place({'Hitler': 56, 'Churchill': 90, 'Mussolini':61})
    'Hitler'
    '''
    return get_candidate_by_place(result, min) #gets min candidate

###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
