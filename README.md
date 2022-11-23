# IIT_CS330_PROGRAMMING_ASSIGNMENT
Marcel Bieganski; CS 330 Under Virgil Bistriceanu; Uploaded: November 8 2022

Written in Python 3 in Windows 10.

Included are executables file labeled 'security_engine_part1.exe', 'security_engine_part2.exe' and 2 source code files. The two python files are not intended to be ran in unit testing, but are there if the code itself is needed.

The security_engine_part1.exe executable takes user input (either one character at a time or in phrases), combines all input into one long sequence that filters out any entry besides integers 0-9, and notifies the user when either the Lock or Unlock code has been entered (see below for codes). This executable is the same as the 'security_engine_part1_source.py' file. When launched, the file can be used as intended with user input, or unit tests may be ran, see instructions below.

The security_engine_part2_source.exe executable runs a 10 trial test against the security engine using a brute force method. Simple launching the file as instructed above will activate its tests.

NOTE BEFORE RUNNING: THE FILES ARE AUTOMATICALLY IN EXE FORM FOR CONVENIENCE

to run in git bash, enter:

  git clone https://github.com/splerry/IIT_CS330_PROGRAMMING_ASSIGNMENT.git
  
  cd IIT_CS330_PROGRAMMING_ASSIGNMENT
  
  ./security_engine_part1.exe
  
  start unit tests  <- type this out as literally as possible
 
  #BELOW EXECUTABLE NEED NOT BE LAUNCHED, AS SAMPLE OUTPUT IS CONTAINED IN THE MEMO. THIS FILE TAKES TIME TO RUN
 
  ./security_engine_part2.exe

to start unit test coverage, enter:

  start unit tests

Output will appear in git bash terminal. Or you may locate the foler which it is stored in and run the executable manually. If so, output will appear in the console.

Lock code: 901494
Unlock code: 901491
