# IIT_CS330_PROGRAMMING_ASSIGNMENT
Marcel Bieganski; CS 330 Under Virgil Bistriceanu; Uploaded: November 8 2022

Written in Python 3 in Windows 10 (PyCharm IDE).

2 pieces of code included. "security_engine_part1" will prompt the user for a code (either to lock or unlock the engine). After this code is entered, it will output either "Locked" or "Unlocked" depending on which code the user entered, or "Invalid seqeunce" for an incorrect code. The program will continue to ask for for input until closed to let the user view output.

The second program "security_engine_part2" will begin generating random integer sequences and test each sequence against the engine (with the key being the unlock code given below). The output includes the generated sequence, the current attempt, and whether or not that attempt was successful. Once a correct sequence is generated, the program will stop generating new sequences, however will stay open to let the user inspect outputs.

Download the attached ZIP file. Inside will be 2 programs labelled "security_engine_part1" and "security_engine_part2", the first contains the code responding to part 1 of the assignment and the second contains the code responding to part 2. To run, first have Python 3 installed. Then either open either program in an IDE or load from desktop (output should appear in command prompt window). Please run both, as either one ONLY contains the answer to its respective part.

Lock code: 901494
Unlock code: 901491

Sample output of Option 1 in program:
"
Average time: 58280 attempts/seconds. Total digits (0 - 9) entered: 303132622
Largest value accepted: 991663719699014914829. Smallest value accepted: 3090149122472658670
"
