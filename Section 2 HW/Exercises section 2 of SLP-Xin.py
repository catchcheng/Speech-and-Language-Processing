# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:00:30 2020

@author: Cinker
"""

# 2.6 Now implement a minimum edit distance algorithm and use your 
# hand-computed results to check your code.

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

# Assignment: https://github.com/sambartika/SpamLord/blob/master/PA_%231/spamLord.pdf
# start code
import sys
import os
import re
import pprint

#The regex for email address
email_pat_1 = '([\w-]+)\s*(@|\(at\)|WHERE|\s+at\s+|&#x40;|\(followed by &ldquo;@)\s*(([\w-]+\s*(\.|;|dot|DOM|at)\s*)+)(-?[eE]-?[dD]-?[uU]|com)'
# \w: any alphanumeric/underscore
# -: Hyphen
# +: one or more occurrences of the previous char or expression
# \s*: optional whitespace(space,tab)
# (@|\(at\)|WHERE|\s+at\s+|&#x40;|\(followed by &ldquo;@) find "@"
# &#x40: the special symbol in keyboard
# -----------------------------------------------------------------------------
# \(followed by &ldquo;@ ???\( ???? followed by ?????? &ldquo;@
# -----------------------------------------------------------------------------
# ?: exactly zero or one occurrence of the previous char or expression


email_pat_2 = 'obfuscate\(\'(([\w-]+\s*(\.|;|dot|DOM)\s*)+)(-?[eE]-?[dD]-?[uU]|com)\',\'(\w+)\'\)'
# aim at the example: <script type="text/javascript">obfuscate('cse.tamu.edu','huangrh')</script>

# The regex for phone number
phone_pat_1 = '\(?(\d{3})(\)\s*|\s|-|\&thinsp;|\.|\/)(\d{3})(\s|-|\&thinsp;|\.|\/)(\d{4})\D+'
# \(: Escape character
# \(?: exactly zero or one occurrence
# (\d{3}): match the pattern that 3 digits show together. {n,m} specifies from n to m occurrences of the previous char or expression
# ----------------------------------------------------------
#(\) ??????????????????????????????????????
# ----------------------------------------------------------
# \s*: optional whitespace
# &thinsp;: thing space. Aims at the example: <a href="contact.html">TEL</a> +1&thinsp;979&thinsp;862&thinsp;2908
# \.: a period
# \D+: one or more occurrences of any non-digit

""" 
TODO
This function takes in a filename along with the file object (actually
a StringIO object) and scans its contents against regex patterns. 
It returns a list of (filename, type, value) tuples where type is either an 
'e' or a 'p' for e-mail or phone, and value is the formatted phone number or e-mail.
The canonical formats are:
     (name, 'p', '###-###-#####')
     (name, 'e', 'someone@something')
If the numbers you submit are formatted differently they will not
match the gold answers
NOTE: ***don't change this interface***
NOTE: You shouldn't need to worry about this, but just so you know, the
'f' parameter below will be of type StringIO. So, make
sure you check the StringIO interface if you do anything really tricky,
though StringIO should support most everything.
"""
def process_file(name, f):
    # note that debug info should be printed to stderr
    res = []
    for line in f:
        matches = re.findall(email_pat_1,line, re.IGNORECASE) # match all the emails in the file and save them in matches
		#Extract email address from the string
        for m in matches: # for each matched email
            ls = list(m) # convert tuples to lists
            email=""
            for i in range(len(ls)): # The amount of elemants in one match
                if i == 0: # this is the first part of the email: dhfzkud@jdhfa.edu.cn
                    email=email+ls[i] 
                elif i == 1: # this is the second part of the email address: @
                    email=email+"@" # add @ to the output
                elif (i-2)%3 ==0: # i = 2, if i = 2, then, it is the third part
                    email=email+ls[i] # add this to the end of the mail address
                elif i==(len(ls)-1): # this is the last part of the email
                    email=email+ls[i] # add it to the end
            email=email.replace("-","").replace(";",".").replace(" dot ",".").replace(" DOM ", ".").replace(" ","")
            if ls[0]!="Server": #---------------------------------------------
                res.append((name,'e',email)) # append the email address to the end of list 'res'
            
        matches = re.findall(email_pat_2,line)
		#Extract email address from the string
        for m in matches:
            ls = list(m)
            email=""
            for i in range(len(ls)):
                if i%3 == 0:
                    email=email+ls[i]
                elif i==(len(ls)-1):
                    email=ls[i]+"@"+email
            email=email.replace("-","").replace(";",".").replace(" dot ",".").replace(" DOM ", ".").replace(" ","")
            res.append((name,'e',email))
        
		#Extract phone number from the string
        matches = re.findall(phone_pat_1,line)
        for m in matches:
            phone=m[0]+"-"+m[2]+"-"+m[4]
            res.append((name,'p',phone))
    return res

"""
You should not need to edit this function, nor should you alter
its interface
"""
def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r')
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

"""
You should not need to edit this function.
Given a path to a tsv file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""
def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""
def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    #print 'Guesses (%d): ' % len(guess_set)
    #pp.pprint(guess_set)
    #print 'Gold (%d): ' % len(gold_set)
    #pp.pprint(gold_set)
    print ('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print ('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print ('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print ('Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn)))

"""
You should not need to edit this function.
It takes in the string path to the data directory and the
gold file
"""
def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)

"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print ('usage:\tSpamLord.py <data_dir> <gold_file>')
        sys.exit(0)
    main(sys.argv[1],sys.argv[2])


























