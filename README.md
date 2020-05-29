# voting
Running simulated elections with different voting systems

This program is designed to simulate Canadian federal elections with single-winner couting
elections with 4 types of ballots: plurality, approval, rated and ranked. 
It compares the result of a simulated elections with different voting systems, including 
the popular vote, plurality vote, approval vote, Instant Run-Off vote (IRV), Single Transferable Vote (STV)
and the Saint-Laguë method (popular representation).

It is divided into 4 sections: 

1. helpers.py : Flatten lists, flatten dicts, add dictionaries, get all candidates,
get min/max candidate, get winner, get last place

2. single_winner.py : Count all 4 types of ballots

3. instant_run_off.py: Votes needed to win, eliminate candidate, count IRV

4. proportional_representation.py: (multiwinner systems): Single transferable vote,
IRV to STV ballot, count STV, Saint-Laguë method

5. simulate_elections.py, read_votes.py, votes.txt: takes as input the voting data from
votes.txt, prints a graph of election results with the different voting systems. 
