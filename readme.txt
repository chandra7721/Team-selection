Run work_area.py
Assign is the database.


Error1: When Sublime launches a build system it captures the output that it generates and sends it to the output panel, but it doesn’t do anything to allow you to send input back to the running program. So if you run anything that’s in any way interactive, your program will hang waiting forever for input to appear on stdin.

Note: In the database Assign, the column "Group" will show error after trying to re-run the program(Line 141: work_area.py). It's because for the sake of neat and simple display, I've set the values of column "Group" as Unique. It can be changed, by simply changing the schema of the table, i.e., unchecking the "unique(U)" part.
