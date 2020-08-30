# Exercises section 3 of SLP

#### 3.1 Write out the equation for trigram probability estimation (modifying Eq. 3.11). Now write out all the non-zero trigram probabilities for the I am Sam corpus on page 33.

    P(w_n|w_n-2, w_n-1) = P(w_n|w_n-1)*P(w_n-1|w_n-2)
    P(I am Sam) = P(am|I)*P(Sam|am) = 1/3
    P(am|I) = 2/3
    P(Sam|am) = 1/2

    P(Sam I am) = P(I|Sam)*P(am|I) = 1/3
    P(I|Sam) = 1/2

    P(I do not) = P(do|I)*P(not|do) = 1/3
    P(do|I) = 1/3
    P(not|do) = 1

    P(do not like) = P(not|do)*P(like|not) = 1
    P(not|do) = 1
    P(like|not) = 1

    P(not like green) = 1
    P(like green eggs) = 1
    P(green eggs and) = 1
    P(eggs and ham) = 1

#### 3.2 Calculate the probability of the sentence *i want chinese food*. Give two probabilities, one using Fig. 3.2 and the ‘useful probabilities’ just below it on page 35, and another using the add-1 smoothed table in Fig. 3.6. Assume the additional add-1 smoothed probabilities P(i|<s>) = 0.19 and P(</s>|food) = 0.40.

    1)
    P(<s> i want chinese food <s>)
    = P(i|<s>)*P(want|i)*P(chinese|want)*P(food|chinese)*P(</s>|food)
    = 0.25*0.33*0.0065*0.52*0.68
    = 0.000189618

    2)
    P(<s> i want chinese food <s>)
    = P(i|<s>)*P(want|i)*P(chinese|want)*P(food|chinese)*P(</s>|food)
    = 0.19*0.21*0.0029*0.052*0.4
    = 0.0000024

#### 3.3 Which of the two probabilities you computed in the previous exercise is higher, unsmoothed or smoothed? Explain why.

> Unsmoothed is higher, as when apply the smooothed algorithm, those grams whose frequency are not zero will be shared to those whose are zero, and thus their smoothed frequency(probability) will be lower. That's why the caluclated result of smoothed is lower than the unsmoothed one.

#### 3.4 We are given the following corpus, modified from the one in the chapter:
    <s> I am Sam </s>
    <s> Sam I am </s>
    <s> I am Sam </s>
    <s> I do not like green eggs and Sam </s>

#### Using a bigram language model with add-one smoothing, what is P(Sam | am)? Include <s> and </s> in your counts just like any other token.

|   |   \<s>| I |am |Sam|do |not|like|green|eggs|and|\</s>|
|---|---|---|---|---|---|---|---|---|---|---|---|
| \<s>  | 0 | 3 | 0 | 1 | 0 | 0 | 0  | 0   | 0 | 0 | 0 |
| I     | 0 | 0 | 3 | 0 | 1 | 0 | 0  | 0   | 0 | 0 | 0 |
| am    | 0 | 0 | 2 | 0 | 0 | 0 | 0  | 0   | 0 | 0 | 1 |
| Sam   | 0 | 1 | 0 | 0 | 0 | 0 | 0  | 0   | 0 | 0 | 3 |
| do    | 0 | 0 | 0 | 0 | 0 | 1 | 0  | 0   | 0 | 0 | 0 |
| not   | 0 | 0 | 0 | 0 | 0 | 0 | 1  | 0   | 0 | 0 | 0 |
| like  | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 1   | 0 | 0 | 0 |
| green | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0   | 1 | 0 | 0 |
| eggs  | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0   | 0 | 1 | 0 |
| and   | 0 | 0 | 0 | 1 | 0 | 0 | 0  | 0   | 0 | 0 | 0 |
| \</s> | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0   | 0 | 0 | 0 |

|   |   \<s>| I |am |Sam|do |not|like|green|eggs|and|\</s>|
|---|---|---|---|---|---|---|---|---|---|---|---|
| \<s>  | 1 | 4 | 1 | 2 | 1 | 1 | 1  | 1   | 1 | 1 | 1 |
| I     | 1 | 1 | 4 | 1 | 2 | 1 | 1  | 1   | 1 | 1 | 1 |
| am    | 1 | 1 | 3 | 1 | 1 | 1 | 1  | 1   | 1 | 1 | 2 |
| Sam   | 1 | 2 | 1 | 1 | 1 | 1 | 1  | 1   | 1 | 1 | 4 |
| do    | 1 | 1 | 1 | 1 | 1 | 2 | 1  | 1   | 1 | 1 | 1 |
| not   | 1 | 1 | 1 | 1 | 1 | 1 | 2  | 1   | 1 | 1 | 1 |
| like  | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 2   | 1 | 1 | 1 |
| green | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1   | 2 | 1 | 1 |
| eggs  | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1   | 1 | 2 | 1 |
| and   | 1 | 1 | 1 | 2 | 1 | 1 | 1  | 1   | 1 | 1 | 1 |
| \</s> | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1   | 1 | 1 | 1 |

|   |   \<s>| I |am |Sam|do |not|like|green|eggs|and|\</s>|
|---|---|---|---|---|---|---|---|---|---|---|---|
| \<s>  | 1/15 | 4/15 | 1/15 | 2/15 | 1/15 | 1/15 | 1/15  | 1/15   | 1/15 | 1/15 | 1/15 |
| I     | 1/15 | 1/15 | 4/15 | 1/15 | 2/15 | 1/15 | 1/15  | 1/15   | 1/15 | 1/15 | 1/15 |
| am    | 1/14 | 1/14 | 3/14 | 1/14 | 1/14 | 1/14 | 1/14  | 1/14   | 1/14 | 1/14 | 2/14 |
| Sam   | 1/15 | 2/15 | 1/15 | 1/15 | 1/15 | 1/15 | 1/15  | 1/15   | 1/15 | 1/15 | 4/15 |
| do    | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 2/12 | 1/12  | 1/12   | 1/12 | 1/12 | 1/12 |
| not   | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 2/12  | 1/12   | 1/12 | 1/12 | 1/12 |
| like  | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 1/12  | 2/12   | 1/12 | 1/12 | 1/12 |
| green | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 1/12  | 1/12   | 2/12 | 1/12 | 1/12 |
| eggs  | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 1/12 | 1/12  | 1/12   | 1/12 | 2/12 | 1/12 |
| and   | 1/12 | 1/12 | 1/12 | 2/12 | 1/12 | 1/12 | 1/12  | 1/12   | 1/12 | 1/12 | 1/12 |
| \</s> | 1/11 | 1/11 | 1/11 | 1/11 | 1/11 | 1/11 | 1/11  | 1/11   | 1/11 | 1/11 | 1/11 |

    P(Sam | am) = 0.1333

#### 3.5 Suppose we didn’t use the end-symbol </s>. Train an unsmoothed bigram grammar on the following training corpus without using the end-symbol </s>:
    <s> a b
    <s> b b
    <s> b a
    <s> a a
#### Demonstrate that your bigram model does not assign a single probability distribution across all sentence lengths by showing that the sum of the probability of the four possible 2 word sentences over the alphabet {a,b} is 1.0, and the sum of the probability of all possible 3 word sentences over the alphabet {a,b} is also 1.0.

    P(a,b) = P(a) * P(b|a) = 1/4
    P(b,b) = P(b) * P(b|b) = 1/4
    P(b,a) = P(a) * P(b|a) = 1/4
    P(a,a) = P(a) * P(a|a) = 1/4

    P(<s>,a,b) = P(<s>) * P(a|<s>) * P(b|a) = 1/2 * 1/2 = 1/4
    P(<s>,b,b) = P(<s>) * P(b|<s>) * P(b|b) = 1/2 * 1/2 = 1/4
    P(<s>,b,a) = P(<s>) * P(b|<s>) * P(a|b) = 1/2 * 1/2 = 1/4
    P(<s>,a,a) = P(<s>) * P(a|<s>) * P(a|a) = 1/2 * 1/2 = 1/4

#### 3.6 Suppose we train a trigram language model with add-one smoothing on a given corpus. The corpus contains V word types. Express a formula for estimating P(w3|w1,w2), where w3 is a word which follows the bigram (w1,w2), in terms of various N-gram counts and V. Use the notation c(w1,w2,w3) to denote the number of times that trigram (w1,w2,w3) occurs in the corpus, and so on for bigrams and unigrams.

    P*(w_3|w_1,w_2)
    = P(w_3|w_2)*P(w_2|w_1)
    = (c(w_2,w_3)+1)/(c(w_2)+v) * (c(w_1,w_2)+1)/(c(w_1)+v)

#### 3.7 We are given the following corpus, modified from the one in the chapter:
    <s> I am Sam </s>
    <s> Sam I am </s>
    <s> I am Sam </s>
    <s> I do not like green eggs and Sam </s>

#### If we use linear interpolation smoothing between a maximum-likelihood bigram model and a maximum-likelihood unigram model with λ1 = 1/2 and λ2 = 1/2, what is P(Sam|am)? Include <s> and </s> in your counts just like any other token.

    P(Sam|am) = \lambda_1 * P(Sam|am) + \lambda_2 * P(Sam)
              = 1/2 * 1 + 1/2 * 1
              = 1

#### 3.8 Write a program to compute unsmoothed unigrams and bigrams.
```
import re # string processing
# n: regulate the order of the gram
# aim_string the string that you want to estimate
def n_gram(corpora, n, aim_string):
    # split the corpora by '.' ****Escape character is needed*****
    lines = re.split('\. |\.', corpora)
    lines = list(filter(None, lines))
    pro_str = []
    pro_str.append((aim_string,pro(lines,aim_string,n)))
    return pro_str

def pro(words, string, n):
    p = 1
    str_list = string.split()
    k = len(str_list)
    for i in range(k-n+1):
        #if k == 2:
        #    p = p*words.count(str_list[n-1+i])/words.count(" ".join(str_list[0:1]))
        #else:
        count_1 = 0
        count_2 = 0
        # calculate the frequency of the aimed string; depends on the regulated n
        for j in range(len(words)):
            if n+i == i+1:
                words_single = words[j].split()
                count_1 = count_1 + words_single.count(" ".join(str_list[i:n+i]))
            else:
                count_1 = count_1 + words[j].count(" ".join(str_list[i:n+i]))
            if n+i-1 == i+1:
                words_single = words[j].split()
                count_2 = count_2 + words_single.count(" ".join(str_list[i:n+i-1]))
            else:
                count_2 = count_2 + words[j].count(" ".join(str_list[i:n+i-1]))
        print(" ".join(str_list[i:n+i]))
        print("count_1",count_1)
        print("count_2",count_2)
        p = p*count_1/count_2
        #k = k - 1
    return p
n_gram('I am Sam. Sam I am. I do not like Sam', 2 , "am Sam")
n_gram('I am Sam. Sam I am. I do not like Sam', 2 , "I am")
n_gram('I am Sam. Sam I am. I do not like Sam', 2 , "I am Sam")
```

#### 3.9 Run your n-gram program on two different small corpora of your choice (you might use email text or newsgroups). Now compare the statistics of the two corpora. What are the differences in the most common unigrams between the two? How about interesting differences in bigrams?

> 先要规定窗宽，窗宽的大小是n，然后遍历算出每n个词成为词组出现的频率。随机选取一个或者两个词作为开始，然后后面接可能性最大的词。
