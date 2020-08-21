# Exercises section 2 of SLP

#### 2.1 Write regular expressions for the following languages

##### 1. the set of all alphabetic strings;

    [A-Za-z]

##### 2. the set of all lower case alphabetic strings ending in a _b_;

    [a-z]*b
    
##### 3. the set of all strings from the alphabet _a,b_ such that each _a_ is immediately preceded by and immediately followed by a _b_;

    *ab*

#### 2.2 Write regular expressions for the following languages. By “word”, we mean an alphabetic string separated from other words by whitespace, any relevant punctuation, line breaks, and so forth.

##### 1. the set of all strings with two consecutive repeated words (e.g., “Humbert Humbert” and “the the” but not “the bug” or “the big bug”);

    /([^A-Za-z][A-Za-z]*[A-Za-z][^A-Za-z])*/
    % P6
    
##### 2. all strings that start at the beginning of the line with an integer and that end at the end of the line with a word;

    [0-9]*[^A-Za-z][A-Za-z]*[A-Za-z][^A-Za-z]
    
##### 3. all strings that have both the word _grotto_ and the word _raven_ in them (but not, e.g., words like _grottos_ that merely contain the word grotto);
    
    /\bgrotto?\b*\braven?\b | \bbraven?\b*\grotto?\b/
    
##### 4. write a pattern that places the first word of an English sentence in a register. Deal with punctuation.
    
    /^\b[A-Z]\b | \[^A-Za-z] \b[A-Z]\b/
    
#### 2.3 Implement an ELIZA-like program, using substitutions such as those described on page 10. You might want to choose a different domain than a Rogerian psychologist, although keep in mind that you would need a domain in which your program can legitimately engage in a lot of simple repetition.

    s/.* (Customer service | Customer | Hi | Hello | Hey | Yo) .*/HI, I AM HERE, WHAT CAN I DO FOR YOU? \1/
    s/.* The product I bought .*/SORRY FOR HEARING THAT. COULD YOU PLEASE PROVIDE THE NUMBER OF THE ORDER?
    s/.* [0-9]*[0-9] .*/PLEASE DESCRIBE THE PROBLEM AND LEAVE US YOUR TEPHONE NUMBER.
    s/.* ( *@* ) .*/THANK YOU, WE WILL CONTATCT YOU AS SOON AS POSSIBLE.
    
#### 2.4 Compute the edit distance (using insertion cost 1, deletion cost 1, substitutioncost 1) of “leda” to “deal”. Show your work (using the edit distance grid)
    

|   | # | l | e | d | a |
|---|---|---|---|---|---|
| # | 0 | 1 | 2 | 3 | 4 |
| d | 1 | 2 | 2 | 2 | 3 |
| e | 2 | 2 | 2 | 3 | 3 |
| a | 3 | 3 | 3 | 3 | 3 |
| l | 4 | 3 | 4 | 4 | 4 |

#### 2.5 Figure out whether _drive_ is closer to _brief_ or to _divers_ and what the edit distance is to each. You may use any version of distance that you like.

> Levenshtein

|   | # | d | r | i | v | e |
|---|---|---|---|---|---|---|
| # | 0 | 1 | 2 | 3 | 4 | 5 |
| b | 1 | 2 | 3 | 4 | 5 | 6 |
| r | 2 | 3 | 2 | 3 | 4 | 5 |
| i | 3 | 4 | 3 | 2 | 3 | 4 |
| e | 4 | 5 | 4 | 3 | 4 | 3 |
| f | 5 | 6 | 5 | 4 | 5 | 4 |


|   | # | d | r | i | v | e | * | * |
|---|---|---|---|---|---|---|---|---|
| # | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| d | 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| r | 2 | 1 | 0 | 1 | 2 | 3 | 4 | 5 |
| i | 3 | 2 | 1 | 0 | 1 | 2 | 3 | 4 |
| v | 4 | 3 | 2 | 1 | 0 | 1 | 2 | 3 |
| e | 5 | 4 | 3 | 2 | 1 | 0 | 1 | 2 |
| r | 6 | 5 | 4 | 3 | 2 | 1 | 2 | 3 |
| s | 7 | 6 | 5 | 4 | 3 | 2 | 3 | 4 |
    
    
#### 2.6 Now implement a minimum edit distance algorithm and use your hand-computed results to check your code.


    import numpy as np # matrix operation

    def meDis(str1, str2):
        # del-cost
        del_cost = 1
        # ins-cost
    	ins_cost = 1
    	# sub-cost
    	sub_cost = 2
    
    	m = len(str1)
    	n = len(str2)
    
    	# initialization of the distance matrix
    	k = max(m,n)
    	D = np.zeros((k+1,k+1))
    	D[0,:] = range(0,k+1)
    	D[:,0] = range(0,k+1)
    
    	if k == m: # str1 longer
        	str2 = str2 + " "*(m-n)
    	else:
        	str1 = str1 + " "*(n-m)
    
    	for i in range(1,k+1):
        	for j in range(1,k+1):
            	if str1[i-1] == str2[j-1]:
                	sub_cost = 0
            	else:
                	sub_cost = 2
            	D[i,j] = min(D[i-1,j] + del_cost, D[i,j-1] + ins_cost, D[i-1,j-1] + sub_cost)
    
    	print(D)


	meDis("drive", "brief")
	meDis("drive", "drivers")
   
    
#### 2.7 Augment the minimum edit distance algorithm to output an alignment; you will need to store pointers and add a stage to compute the backtrace.

```
def meDisbacktrace(str1, str2):
    # del-cost
    del_cost = 1
    # ins-cost
    ins_cost = 1
    # sub-cost
    sub_cost = 2
    
    m = len(str1)
    n = len(str2)
    
    # initialization of the distance matrix
    k = max(m,n)
    D = np.zeros((k+1,k+1))
    D[0,:] = range(0,k+1)
    D[:,0] = range(0,k+1)
    
    d_trace = D.astype(np.str)
    
    if k == m: # str1 longer
        str2 = str2 + " "*(m-n)
    else:
        str1 = str1 + " "*(n-m)
    
    for i in range(1,k+1):
        for j in range(1,k+1):
            if str1[i-1] == str2[j-1]:
                sub_cost = 0
            else:
                sub_cost = 2
            D[i,j] = min(D[i-1,j] + del_cost, D[i,j-1] + ins_cost, D[i-1,j-1] + sub_cost)
            d_trace[i,j] = np.str(D[i,j])
            if D[i,j] == D[i-1,j] + del_cost:
                d_trace[i,j] = "↑"+d_trace[i,j]
            if D[i,j] == D[i,j-1] + ins_cost:
                d_trace[i,j] = "←"+d_trace[i,j]
            if D[i,j] == D[i-1,j-1] + sub_cost:
                d_trace[i,j] = "↖"+d_trace[i,j]
    print(d_trace)
    
meDisbacktrace("drive", "drivers")

[['0.0' '1.0' '2.0' '3.0' '4.0' '5.0' '6.0' '7.0']
 ['1.0' '↖0.0' '←1.0' '←2.0' '←3.0' '←4.0' '←5.0' '←6.0']
 ['2.0' '↑1.0' '↖0.0' '←1.0' '←2.0' '←3.0' '↖←4.0' '←5.0']
 ['3.0' '↑2.0' '↑1.0' '↖0.0' '←1.0' '←2.0' '←3.0' '←4.0']
 ['4.0' '↑3.0' '↑2.0' '↑1.0' '↖0.0' '←1.0' '←2.0' '←3.0']
 ['5.0' '↑4.0' '↑3.0' '↑2.0' '↑1.0' '↖0.0' '←1.0' '←2.0']
 ['6.0' '↑5.0' '↑4.0' '↑3.0' '↑2.0' '↑1.0' '↖←↑2.0' '↖←↑3.0']
 ['7.0' '↑6.0' '↑5.0' '↑4.0' '↑3.0' '↑2.0' '↖←↑3.0' '↖←↑4.0']]


```


