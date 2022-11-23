# IIT_CS330_PROGRAMMING_ASSIGNMENT
Marcel Bieganski; CS 330 Under Virgil Bistriceanu; Uploaded: November 8 2022

Written in Python 3 in Windows 10.

Included is an executable file labeled 'security_engine_part1.exe' and 2 source code files. The two python files are not intended to be ran in unit testing, but are there if the code itself is needed.

The executable takes user input (either one character at a time or in phrases), combines all input into one long sequence that filters out any entry besides integers 0-9, and notifies the user when either the Lock or Unlock code has been entered (see below for codes). This executable is the same as the 'security_engine_part1_source.py' file.

The 'security_engine_part2_source.py' file runs 99 simulations of a brute force method of breaking the engine from the first program; outputting the average amount of attempts per simulation, total digits entered, largest sequence with accepted code, and the smallest sequence with accepted code. View the memo for a report on the output of part 2.

to run in git bash, enter:

  git clone https://github.com/splerry/IIT_CS330_PROGRAMMING_ASSIGNMENT.git
  
  cd IIT_CS330_PROGRAMMING_ASSIGNMENT
  
  ./security_engine_part1.exe

to start unit test coverage, enter:

  start unit tests

Output will appear in git bash terminal. Or you may locate the foler which it is stored in and run the executable manually. If so, output will appear in the console.

Lock code: 901494
Unlock code: 901491
