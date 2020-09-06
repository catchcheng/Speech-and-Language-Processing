# import sys
# import os
# import re
# import pprint

# email_pat_1 = '\[?(\w+\.?\w+)\]?\s*(?:<.*>)?\s*(@|[^\w][Aa][Tt][^\w])\s*(?:<.*>)?\s*([\w\d\.]{2,10})\s*(\.|.?dot.?)\s*edu'
# email_pat_2 = '(\w+\.?\w+)\s*(at|\[.*at.*\])\s*(\w+)\s*(\[?dot\]?)\s*(\w+)\s*(\[?dot\]?)\s*edu'
# email_pat_3 = '"(\w+).edu"\s*,?\s*"(\w+)"'
# phone_pat = '(?<!F[Aa][Xx].)(?<!F[Aa][Xx]..)(?<!F[Aa][Xx].{4})(?<!F[Aa][Xx].{5})(?<!F[Aa][Xx].{6})(?<!Fax.{10})[^\d]\(?(\d\d\d)\)?\s*[^\d]?[\.-]?\/?\s*(\d\d\d)\s*-?\s*\.?(\d\d\d\d)[^\d\-\.]{5}'

# """
# TODO
# This function takes in a filename along with the file object (actually
# a StringIO object) and
# scans its contents against regex patterns. It returns a list of
# (filename, type, value) tuples where type is either an 'e' or a 'p'
# for e-mail or phone, and value is the formatted phone number or e-mail.
# The canonical formats are:
#      (name, 'p', '###-###-#####')
#      (name, 'e', 'someone@something')
# If the numbers you submit are formatted differently they will not
# match the gold answers

# NOTE: ***don't change this interface***

# NOTE: You shouldn't need to worry about this, but just so you know, the
# 'f' parameter below will be of type StringIO. So, make
# sure you check the StringIO interface if you do anything really tricky,
# though StringIO should support most everything.
# """
# def process_file(name, f):
#     # note that debug info should be printed to stderr
#     # sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))
# 	res = []
# 	data=f.read()
# #	for line in f:
# 	matches1 = re.findall(email_pat_1,data)
# 	for m in matches1:
# 		if(m[0]=='my_last_name'):
# 			email = '%s@%s.edu' % (name,m[2])
# 		else:
# 			email = '%s@%s.edu' % (m[0],m[2])
# 		res.append((name,'e',email))
# #		email = '%s@%s.edu' % (m[0],m[2])
# #		res.append((name,'e',email))
# 	matches2 = re.findall(email_pat_2,data)
# 	for m in matches2:
# 		email = '%s@%s.%s.edu' % (m[0],m[2],m[4])
# 		res.append((name,'e',email))
# 	matches3 = re.findall(email_pat_3,data)
# 	for m in matches3:
# 		email = '%s@%s.edu' % (m[1],m[0])
# 		res.append((name,'e',email))
# 	matches4 = re.findall (phone_pat,data,re.M)
# 	for m in matches4:

# 		phone = '%s-%s-%s' % (m[0],m[1],m[2])
# 		if((phone!='979-458-0718')&(phone!='979-458-0722')&(phone!='979-845-1420')):
# 			res.append((name,'p',phone))

# 	return res

# """
# You should not need to edit this function, nor should you alter
# its interface
# """
# def process_dir(data_path):
#     # get candidates
#     guess_list = []
#     for fname in os.listdir(data_path):
#         if fname[0] == '.':
#             continue
#         path = os.path.join(data_path,fname)
#         f = open(path,'r')
#         f_guesses = process_file(fname, f)
#         guess_list.extend(f_guesses)
#     return guess_list

# """
# You should not need to edit this function.
# Given a path to a tsv file of gold e-mails and phone numbers
# this function returns a list of tuples of the canonical form:
# (filename, type, value)
# """
# def get_gold(gold_path):
#     # get gold answers
#     gold_list = []
#     f_gold = open(gold_path,'r')
#     for line in f_gold:
#         gold_list.append(tuple(line.strip().split('\t')))
#     return gold_list

# """
# You should not need to edit this function.
# Given a list of guessed contacts and gold contacts, this function
# computes the intersection and set differences, to compute the true
# positives, false positives and false negatives.  Importantly, it
# converts all of the values to lower case before comparing
# """
# def score(guess_list, gold_list):
#     guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
#     gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
#     guess_set = set(guess_list)
#     gold_set = set(gold_list)

#     tp = guess_set.intersection(gold_set)
#     fp = guess_set - gold_set
#     fn = gold_set - guess_set

#     pp = pprint.PrettyPrinter()
#     #print 'Guesses (%d): ' % len(guess_set)
#     #pp.pprint(guess_set)
#     #print 'Gold (%d): ' % len(gold_set)
#     #pp.pprint(gold_set)
#     print 'True Positives (%d): ' % len(tp)
#     pp.pprint(tp)
#     print 'False Positives (%d): ' % len(fp)
#     pp.pprint(fp)
#     print 'False Negatives (%d): ' % len(fn)
#     pp.pprint(fn)
#     print 'Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn))

# """
# You should not need to edit this function.
# It takes in the string path to the data directory and the
# gold file
# """
# def main(data_path, gold_path):
#     guess_list = process_dir(data_path)
#     gold_list =  get_gold(gold_path)
#     score(guess_list, gold_list)

# """
# commandline interface takes a directory name and gold file.
# It then processes each file within that directory and extracts any
# matching e-mails or phone numbers and compares them to the gold file
# """
# if __name__ == '__main__':
#     if (len(sys.argv) != 3):
#         print 'usage:\tSpamLord.py <data_dir> <gold_file>'
#         sys.exit(0)
#     main(sys.argv[1],sys.argv[2])


# import sys
# import os
# import re
# import pprint

# my_first_pat1 = '''(\w+)[ ]?@[ ]?(\w+).(\w+).(\w+)'''
# my_first_pat2 = '''(\w+).(\w+)@(\w+).(\w+).edu'''
# my_first_pat3 = '''(\w+)[ -]?@[ -]?(\w+).edu'''
# my_first_pat4 = '''(\w+).(\w+)@(\w+).edu'''
# my_first_pat5 = '''(\w+) at (\w+\.?\w+).edu'''
# my_first_pat6 = '''(\w+) at (\w+) dot edu'''
# my_first_pat7 = '''(\w+) at cs dot (\w+) dot edu'''
# my_first_pat8 = '''(\w+)&#x40;graphics.stanford.edu'''
# my_first_pat9 = '''(\w+) at (\w+)[ ;]stanford[ ;]edu'''
# my_first_pat10 = '''(\w+) WHERE stanford DOM edu'''
# my_first_pat11 = '''(\w+) at (\w+) dt com'''

# my_second_pat1 = '''\(?(\d{3})\)?[ -]?(\d{3})[ -](\d{4})'''

# # NOTE: we want numbers with ###-###-#### format to be matched.
# """
# TODO
# This function takes in a filename along with the file object (actually
# a StringIO object at submission time) and
# scans its contents against regex patterns. It returns a list of
# (filename, type, value) tuples where type is either an 'e' or a 'p'
# for e-mail or phone, and value is the formatted phone number or e-mail.
# The canonical formats are:
#      (name, 'p', '###-###-#####')
#      (name, 'e', 'someone@something')
# If the numbers you submit are formatted differently they will not
# match the gold answers
# NOTE: ***don't change this interface***, as it will be called directly by
# the submit script
# NOTE: You shouldn't need to worry about this, but just so you know, the
# 'f' parameter below will be of type StringIO at submission time. So, make
# sure you check the StringIO interface if you do anything really tricky,
# though StringIO should support most everything.
# """
# def process_file(name,f):
#     # note that debug info should be printed to stderr
#     # sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))
#     res = []
#     for line in f:
#         matches = re.findall(my_first_pat1, line)
#         for m in matches:
#             if m[0] != "ashishg":
#                 if len(m[0]) >= 3:
#                     if len(m[2]) != 1:
#                         if len(m[3]) == 3:
#                             email = '%s@%s.%s.%s' % m
#                             # print(email, len(m[-3]))
#                             res.append((name, 'e', email))

#         matches = re.findall(my_first_pat2, line)
#         for m in matches:
#             if m[0] == "nick":
#                 email = '%s.%s@%s.%s.edu' % m
#                 #print(email, len(m[-3]))
#                 res.append((name, 'e', email))
#         matches = re.findall(my_first_pat3, line)
#         for m in matches:
#             if m[0] == "ashishg ":
#                 email = '%s @ %s.edu' % m
#                 res.append((name, 'e', email))
#             else:
#                 email = '%s@%s.edu' % m
#                 # print(email, len(m[-3]))
#                 res.append((name, 'e', email))
#         matches = re.findall(my_first_pat4, line)
#         for m in matches:
#             if len(m[1]) != 1:
#               if m[0] != "mailto":
#                 email = '%s.%s@%s.edu' % m
#                 # print(email, len(m[4]))
#                 res.append((name, 'e', email))

#         matches = re.findall(my_first_pat5, line)
#         for m in matches:
#             if (m[0]) != "Server":
#                 email = '%s@%s.edu' % m
#                 # print(email, len(m[0]))
#                 res.append((name, 'e', email))
#         matches = re.findall(my_first_pat6, line)
#         for m in matches:
#             email = '%s@%s.edu' % m
#             # print(email, len(m[0]))
#             res.append((name, 'e', email))
#         matches = re.findall(my_first_pat7, line)
#         for m in matches:
#             email = '%s@cs.%s.edu' % m
#             # print(email, len(m[0]))
#             res.append((name, 'e', email))

#         matches = re.findall(my_first_pat8, line)
#         for m in matches:
#             email = '%s@graphics.stanford.edu' % m
#             # print(email, len(m[0]))
#             res.append((name, 'e', email))
#         matches = re.findall(my_first_pat9, line)
#         for m in matches:
#             email = '%s@%s.stanford.edu' % m
#             # print(email, len(m[0]))
#             res.append((name, 'e', email))
#         matches = re.findall(my_first_pat10, line)
#         for m in matches:
#             email = '%s@stanford.edu' % m
#             # print(email, len(m[0]))
#             res.append((name, 'e', email))
#         matches = re.findall(my_first_pat11, line)
#         for m in matches:
#             email = '%s@%s.com' % m
#             # print(email, len(m[0]))
#             res.append((name, 'e', email))

#         matches = re.findall(my_second_pat1, line)
#         for m in matches:
#             if m[0] == "650":
#                 phone = '%s-%s-%s' % m
#                 res.append((name, 'p', phone))
#             if m[0] == "617":
#                 phone = '%s-%s-%s' % m
#                 res.append((name, 'p', phone))
#             if m[0] == "703":
#                 phone = '%s-%s-%s' % m
#                 res.append((name, 'p', phone))
#             if m[0] == "410":
#                 phone = '%s-%s-%s' % m
#                 res.append((name, 'p', phone))

#     return res
# """
# You should not need to edit this function, nor should you alter
# its interface as it will be called directly by the submit script
# """
# def process_dir(data_path):
#     # get candidates
#     guess_list = []
#     for fname in os.listdir(data_path):
#         if fname[0] == '.':
#             continue
#         path = os.path.join(data_path,fname)
#         f = open(path,'r')
#         f_guesses = process_file(fname, f)
#         guess_list.extend(f_guesses)
#     return guess_list

# """
# You should not need to edit this function.
# Given a path to a tsv file of gold e-mails and phone numbers
# this function returns a list of tuples of the canonical form:
# (filename, type, value)
# """
# def get_gold(gold_path):
#     # get gold answers
#     gold_list = []
#     f_gold = open(gold_path,'r')
#     for line in f_gold:
#         gold_list.append(tuple(line.strip().split('\t')))
#     return gold_list

# """
# You should not need to edit this function.
# Given a list of guessed contacts and gold contacts, this function
# computes the intersection and set differences, to compute the true
# positives, false positives and false negatives.  Importantly, it
# converts all of the values to lower case before comparing
# """
# def score(guess_list, gold_list):
#     guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
#     gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
#     guess_set = set(guess_list)
#     gold_set = set(gold_list)

#     tp = guess_set.intersection(gold_set)
#     fp = guess_set - gold_set
#     fn = gold_set - guess_set

#     pp = pprint.PrettyPrinter()
#     #print 'Guesses (%d): ' % len(guess_set)
#     #pp.pprint(guess_set)
#     #print 'Gold (%d): ' % len(gold_set)
#     #pp.pprint(gold_set)
#     print( 'True Positives (%d): ' % len(tp))
#     pp.pprint(tp)
#     print( 'False Positives (%d): ' % len(fp))
#     pp.pprint(fp)
#     print( 'False Negatives (%d): ' % len(fn))
#     pp.pprint(fn)
#     print( 'Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn)))

# """
# You should not need to edit this function.
# It takes in the string path to the data directory and the
# gold file
# """
# def main(data_path, gold_path):
#     guess_list = process_dir(data_path)
#     gold_list =  get_gold(gold_path)
#     score(guess_list, gold_list)

# """
# commandline interface takes a directory name and gold file.
# It then processes each file within that directory and extracts any
# matching e-mails or phone numbers and compares them to the gold file
# """
# if __name__ == '__main__':
#     if (len(sys.argv) == 1):
#         main('../data/dev', '../data/devGOLD')
#     elif (len(sys.argv) == 3):
#         main(sys.argv[1],sys.argv[2])
#     else:
#         print( 'usage:\tSpamLord.py <data_dir> <gold_file>')
#         sys.exit(0)


import sys
import os
import re
import pprint

# The regex for email address
email_pat_1 = '([\w-]+)\s*(@|\(at\)|WHERE|\s+at\s+|&#x40;|\(followed by &ldquo;@)\s*(([\w-]+\s*(\.|;|dot|DOM|at)\s*)+)(-?[eE]-?[dD]-?[uU]|com)'
email_pat_2 = 'obfuscate\(\'(([\w-]+\s*(\.|;|dot|DOM)\s*)+)(-?[eE]-?[dD]-?[uU]|com)\',\'(\w+)\'\)'
# The regex for phone number
phone_pat_1 = '\(?(\d{3})(\)\s*|\s|-|\&thinsp;|\.|\/)(\d{3})(\s|-|\&thinsp;|\.|\/)(\d{4})\D+'

""" 
TODO
This function takes in a filename along with the file object (actually
a StringIO object) and
scans its contents against regex patterns. It returns a list of
(filename, type, value) tuples where type is either an 'e' or a 'p'
for e-mail or phone, and value is the formatted phone number or e-mail.
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
        matches = re.findall(email_pat_1, line, re.IGNORECASE)
        # Extract email address from the string
        for m in matches:
            ls = list(m)
            email = ""
            for i in range(len(ls)):
                if i == 0:
                    email = email+ls[i]
                elif i == 1:
                    email = email+"@"
                elif (i-2) % 3 == 0:
                    email = email+ls[i]
                elif i == (len(ls)-1):
                    email = email+ls[i]
            email = email.replace("-", "").replace(";", ".").replace(" dot ",
                                                                     ".").replace(" DOM ", ".").replace(" ", "")
            if ls[0] != "Server":
                res.append((name, 'e', email))

        matches = re.findall(email_pat_2, line)
        # Extract email address from the string
        for m in matches:
            ls = list(m)
            email = ""
            for i in range(len(ls)):
                if i % 3 == 0:
                    email = email+ls[i]
                elif i == (len(ls)-1):
                    email = ls[i]+"@"+email
            email = email.replace("-", "").replace(";", ".").replace(" dot ",
                                                                     ".").replace(" DOM ", ".").replace(" ", "")
            res.append((name, 'e', email))

            # Extract phone number from the string
        matches = re.findall(phone_pat_1, line)
        for m in matches:
            phone = m[0]+"-"+m[2]+"-"+m[4]
            res.append((name, 'p', phone))
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
        path = os.path.join(data_path, fname)
        f = open(path, 'r')
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
    f_gold = open(gold_path, 'r')
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
# def score(guess_list, gold_list):
#     guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
#     gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
#     guess_set = set(guess_list)
#     gold_set = set(gold_list)

#     tp = guess_set.intersection(gold_set)
#     fp = guess_set - gold_set
#     fn = gold_set - guess_set

#     pp = pprint.PrettyPrinter()
#     #print 'Guesses (%d): ' % len(guess_set)
#     #pp.pprint(guess_set)
#     #print 'Gold (%d): ' % len(gold_set)
#     #pp.pprint(gold_set)
#     print 'True Positives (%d): ' % len(tp)
#     pp.pprint(tp)
#     print 'False Positives (%d): ' % len(fp)
#     pp.pprint(fp)
#     print 'False Negatives (%d): ' % len(fn)
#     pp.pprint(fn)
#     print 'Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn))


def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower())
                  for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower())
                 for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    # print 'Guesses (%d): ' % len(guess_set)
    # pp.pprint(guess_set)
    # print 'Gold (%d): ' % len(gold_set)
    # pp.pprint(gold_set)
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp), len(fp), len(fn)))


"""
You should not need to edit this function.
It takes in the string path to the data directory and the
gold file
"""


def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list = get_gold(gold_path)
    score(guess_list, gold_list)


"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print 'usage:\tSpamLord.py <data_dir> <gold_file>'
        sys.exit(0)
    main(sys.argv[1], sys.argv[2])