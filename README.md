# IIT_CS330_PROGRAMMING_ASSIGNMENT
Marcel Bieganski; CS 330 Under Virgil Bistriceanu; Uploaded: November 8 2022

Written in Python 3 in Windows 10.

Included are 2 executable files and 2 source code files. : 'security_engine_part1.exe', 'security_engine_part2.exe', 'security_engine_part1.py', and 'security_engine_part2.py'. The first contains the code for section 1 of the assignment, and the second contains the code for section 2. The last 2 are the source code for the 2 previous executables. 

The first executable takes user input (either one character at a time or in phrases), combines all input into one long sequence that filters out any entry besides integers 0-9, and notifies the user when either the Lock or Unlock code has been entered (see below for codes).

The second executable will run 99 simulations of a brute force method of breaking the engine from the first program; outputting the average amount of attempts per simulation, total digits entered, largest sequence with accepted code, and the smallest sequence with accepted code.

to run:

1) git clone https://github.com/splerry/IIT_CS330_PROGRAMMING_ASSIGNMENT.git
2) cd IT_CS330_PROGRAMMING_ASSIGNMENT
3) either ./security_engine_part1.exe or ./security_engine_part2.exe depending on which you are attempting to run. Please run both or run the first and see sample output for the second below for the whole assignment. Output will appear in git bash terminal.



Lock code: 901494
Unlock code: 901491

Sample output of "security_engine_part2.exe":

"
Average time: 58280 attempts/seconds. Total digits (0 - 9) entered: 303132622
Largest value accepted: 991663719699014914829. Smallest value accepted: 3090149122472658670
"
