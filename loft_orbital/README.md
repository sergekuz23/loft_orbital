##About this program:

This program:
* Initializes 10 arrays of integers of size 10k with random values between 0 and 9
* Counts and outputs the number of occurrences for each digit (0 to 9)
* Sorts the arrays, using a bubble sort algorithm
* Counts and outputs the number of occurrences for each digit once all arrays are sorted
* Counts and sorts all arrays simultaneously using multiprocessing

##Unit tests
* Pytest is used to create and run unit tests for this program

##Multiprocessing 

By using multiprocessing, I was able to reduce the run time from approx 90 seconds to approx 31 seconds. 
The reason why I chose multiprocessing over threading is that a new thread is spawned within the existing process, wherein the multiprocessing a new process is started independently from the first process. Taking into account that we are working with 10 large arrays, with multiprocessing we can divide all that data up for each core and then process it independently.

##How to run

* To run this program, go to the terminal, switch to '/loft_orbital' and run the command 'python loft_orbital.py'.
* To run unit tests, go to the terminal, switch to '/loft_orbital' and run the command 'test_loft_orbital.py'
* For type checking, please, run 'mypy loft_orbital.py'
* Dockerfile is also available in this directory.