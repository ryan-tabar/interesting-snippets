# RDS Team Member Interview - Coding Challange


In this zip archive you will find templates for solutions to two of the problems implemented in the first part of your interview.  
We would like you to use either Javascript, Python or VB.net to create implementions to those problems.


Each template contains three sections:

1. An empty function definition with inputs and outputs defined
2. A collection with a single test case
3. A 'for loop' that will iterate over the collection of test cases and execute the code in the function definition


We would like you to implement your code in the empty function definition.  If you would like to import standard libraries or write additional helper functions or classes, 
that is OK.



The problem specifications are:


1. PANGRAM

Problem definition:

A pangram is a sentence using every letter of a given alphabet at least once.  A common English example is 'The quick brown fox jumps over the lazy dog'. 
Given any string as an input, find which letters must be added for it to become a pangram. 

Input: String

Preconditions:
- All letters are from the English alphabet
- All letters in text are lowercase

Output: String 

Postconditions:
- The letters from a to z that don't occur in the input text, in alphabetical order



2. END OF THE LINE

Problem definition:  
A train formed of wagons numbered 1, 2, 3, ..., n comes from the west branch line into the station 
and needs to leave it to the east with the wagons possibly in a different order.  
Each wagon can be detached from the others and the station has capacity for all n wagons. 
Once a wagon is in the station, it can't be moved back to the west.

Given a number of wagons, and a permutation of wagons to test, check if the permutation is possible.

Inputs: 
number_of_wagons: integer, permutaion_to_test: sequence

Preconditions: 
number_of_wagons > 0
permutaion_to_test is a permutation of the numbers from 1 to number_of_wagons

Output: 
permutation_is_possible: boolean
