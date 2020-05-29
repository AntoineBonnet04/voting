# Part 4
# Name: Antoine Bonnet

from a3_helpers import *


def count_plurality(ballots):
    ''' (list) -> dict
    #Input: a list of plurality ballots
    #Return: a dictionary of how many votes each candidate got
    >>> count_plurality(['LIBERAL','LIBERAL','NDP','LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    >>> count_plurality(['GREEN','LIBERAL','NDP'])
    {'GREEN': 1, 'LIBERAL': 1, 'NDP': 1}
    '''
    candidates = get_all_candidates(ballots) #creates list with all candidates
    new_dict = dict.fromkeys(candidates, 0)
    #creates dict with all candidates and value 0
    for element in ballots:
            new_dict[element] += 1 #adds 1 to value for each candidate
    return new_dict

def count_approval(ballots):
    ''' (list) -> dict
    #Input: a list of approval ballots
    #Return: a dictionary of how many votes each candidates got
    >>> count_approval([ ['LIBERAL','NDP'], ['NDP'], \
    ['NDP', 'GREEN','BLOC']])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    '''
    return count_plurality(flatten_lists(ballots))
    #flattens list of ballots and create dicts with votes

def count_rated(ballots):
    '''(list) -> dict
    #Input: a list of rated ballots (dictionaries) with a score out of 5
    #Sum up the scores for each candidate. returns a dictionary
    #of how many points each candidate got
    >>> count_rated([{'LIBERAL': 5, 'NDP': 2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    '''
    flat_list = [] #creates empty list
    for element in ballots: #iterates through all dictionaries in list
        flat_list += flatten_dict(element) #adds flat element
    return count_plurality(flat_list) #counts all elements in flat list

def count_first_choices(ballots):
    '''(list) -> dict
    # Input: a list of ranked ballots. Return: a dictionary storing
    # for every party represented in all the ballots, how many
    # ballots was the first choice.
    >>> count_first_choices([['NDP','LIBERAL'],['GREEN','NDP'],['NDP','BLOC']])
    {'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0}
    '''
   
    if len(ballots) == 0:
        return {}
    
    #initialize a dict with keys all candidates, initial values 0
    list_candidates = get_all_candidates(flatten_lists(ballots))
    first_dict = dict.fromkeys(list_candidates, 0)
    
    #for each first string in each sublist, add 1 to value in dict
    for element in ballots:
        if element == []:
            continue
        else:
            first_dict[element[0]] += 1

    return first_dict
        
        


    
if __name__ == '__main__':
    doctest.testmod()
