# Part 2
# Name: Antoine Bonnet
# ID: 260928321

from single_winner import *

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''(list, int) -> int
    #Input: a list of ballots and an integer number of winners
    #Return: the integer number of votes a candidate would need to
    #win using the Droop Quota: RoundDown(totalvotes/(winners+1))+1
    >>> votes_needed_to_win([{'CPC':3, 'NDP':5},{'NDP':2,'CPC':4},\
    {'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    '''
    total_votes = len(ballots) #the number of votes in total = number of ballots
    droop_quota = int(total_votes/(num_winners + 1)) + 1 #computes droop quota
    return droop_quota

def has_votes_needed(result, votes_needed):
    ''' (dict, int) -> bool
    #input: a dict of election results and integer votes needed
    #return: a boolean representing whether the candidate with the
    #most votes in this election has at least votes_needed votrs.
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True
    '''
    if result == {}:
        return False
    else:
        votes_winner = result[get_winner(result)] #Gets number of votes of winner
    return votes_winner >= votes_needed #tests if number of votes winner are enough

################################################################################

def eliminate_candidate(ballots, to_eliminate):
    ''' (list, list) -> list
    #input: a list of ranked ballots, a list of candidates to eliminate
    #return: a new list of ranked ballots where all the candidates in
    #to_eliminate have been removed. The input list is not modified.
    #If all candidates on a ballot have been eliminated, becomes an empty list
    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'],\
    ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    '''
    #temporary list, since mutable objects and input not modified
    new_list = []
    
    #edge cases
    if to_eliminate == []:
        if new_list.count([]) == len(new_list):
            return []
        else:
            return new_list
    
#new list of ranked ballots where all candidates in to_eliminate have been removed
    for sublist in ballots:
        if sublist == []: 
            new_list.append([])
        else:
            sublist_copy = []
            for party in sublist:
                if party in to_eliminate:
                    continue
                else: 
                    sublist_copy.append(party)
#append each copy of the sublist with parties removed
            new_list.append(sublist_copy) 

        
    if new_list.count([]) == len(new_list):
        return []

    return new_list

################################################################################


def count_irv(ballots):
    ''' (list) -> dict
    #Input: a list of ranked ballots. Return: a dict of how many
    #votes each candidate ends with after counting with IRV
    #Every candidate in the input list should be in returned dict
    >>> count_irv([['NDP'], ['GREEN','NDP','BLOC'], ['LIBERAL','NDP'], \
    ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC','GREEN','NDP'], ['BLOC', 'CPC'],\
    ['LIBERAL','GREEN'], ['NDP']])
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}   
    '''
    #counting up all the voters' first choices:
    first_choices = count_first_choices(ballots)
    
    #keeps record of all candidates at the start:
    list_candidates = get_all_candidates(first_choices)
    first_place = get_winner(first_choices)
    votes_needed = votes_needed_to_win(ballots, 1)
    
    #a boolean which is True when the 1st candidate has enough votes:
    majority = has_votes_needed(first_choices, votes_needed)
    
    while not majority:
        first_choices = count_first_choices(ballots)
        first_place = get_winner(first_choices)
        #deletes all items in first_choices dict with value 0
        for key in list(first_choices):
            if first_choices[key] == 0:
                del first_choices[key]
                
        #If no majority, identify which candidate came in last:
        last_candidate = last_place(first_choices)   
        #eliminate last place candidate by finding all ballots with
        #last candidate as top choice:
        for element in ballots:
            if element == []:
                continue
            elif element[0] == last_candidate:
                del(element[0])
        first_choices[last_candidate] = 0
        
        #check majority before reiteration (if majority, stops)
        majority = has_votes_needed(first_choices, votes_needed)
        
    #adds back candidates who were deleted from first_choices (with value 0)
    
    for element in list_candidates:
        if element not in first_choices:
            first_choices[element] = 0
            
    return first_choices

################################################################################
    
if __name__ == '__main__':
    doctest.testmod()
