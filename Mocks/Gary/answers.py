'''
For n deliveries, how many valid route combinations exist?

Solution

This is basically a pure combinatorics reasoning problem. T
he main intuition is that for n deliveries, there are n pickup actions and n drop off actions. 
Thus, the total number of sequence permutations (including invalid ones) is (2n)!. 
To get rid of the invalid sequences, need to divide by 2 for each delivery to remove all the cases where Di is before Pi 
(should be half the time for each delivery by symmetry). 
Thus, overall valid route combinations is (2n)! / 2n. Not necessarily looking for a rigorous proof 
(although a proof by induction is actually quite easy), just looking for good intuition. 
If the candidate cannot get the answer, one possibility is tell them the answer and ask to see if they can prove it.

Proof by induction

For i = 1, the only possibility is P1, D1 so the equation holds.

Assume the number of valid routes for i = n deliveries is (2n)! / 2^n.

Then for i = n + 1, 
we note there are 2n + 1 spaces between the previous 2n routes where a space is shown as _ in the below example: 
_ , p1, _ , d1, … , dn, _ For the newly added delivery, 
if it’s pickup (p) is placed at the first space, 
the number of possibilities for it’s drop off (d) is any of the spaces yielding 2n + 1 possibilities. 
If p is placed on the second space, then d has 2n possibilities and 
so on until the case where p is placed on the last space in which d only has one possibility (on the last space, after p). Thus, the total permutations of valid insertions of p and d is (2n + 1) + (2n) + … + 1 = (2n + 2)(2n + 1) / 2 and therefore the total number of valid route sequences is (2n)! / 2^n * (2n + 2)(2n + 1) / 2 = (2(n+1))! / 2^(n+1) thus completing the induction.
'''
