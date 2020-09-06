### 3.8, 3.9, 3.10, 3.11 ###
from __future__ import division
from collections import defaultdict as ddict
import itertools
import math
import random

class NGrams(object):
    def __init__(self, max_n, words=None):
        self._max_n = max_n
        self._n_range = range(1, max_n + 1)
        self._counts = ddict(lambda: 0)
        # if words were supplied, update the counts
        if words is not None:
            self.update(words)

    def update(self, words):
        # increment the total word count, storing this under # the empty tuple - storing it this way simplifies # the _probability() method
        self._counts[()] += len(words)

        # count ngrams of all the given lengths
        for i, word in enumerate(words):
            for n in self._n_range:
                if i + n <= len(words):
                    ngram_range = range(i, i + n)
                    ngram = [words[j] for j in ngram_range]
                    self._counts[tuple(ngram)] += 1

    def probability(self, words):
        if len(words) <= self._max_n:
            return self._probability(words)
        else:
            prob = 1

            for i in range(len(words) - self._max_n + 1):
                ngram = words[i:i + self._max_n]
                prob *= self._probability(ngram)
            return prob

    def _probability(self, ngram):
        # get count of ngram and its prefix
        ngram = tuple(ngram)
        ngram_count = self._counts[ngram]
        prefix_count = self._counts[ngram[:-1]]
        # divide counts (or return 0.0 if not seen)
        if ngram_count and prefix_count:
            # print(ngram_count, prefix_count)
            return ngram_count / prefix_count
        else:
            return 0.0

    def generate(self, n_words):
        # select unigrams
        ngrams = iter(self._counts)
        unigrams = [x for x in ngrams if len(x) == 1]
        # keep trying to generate sentences until successful
        while True:
            try:
                return self._generate(n_words, unigrams)
            except RuntimeError:
                pass

    def _generate(self, n_words, unigrams):
        # add the requested number of words to the list
        words = []
        for i in itertools.repeat(self._max_n):
            # the prefix of the next ngram
            if i == 1:
                prefix = ()
            else:
                prefix = tuple(words[-i + 1:])
            # select a probability cut point, and then try
            # adding each unigram to the prefix until enough # probability has been seen to pass the cut point
            threshold = random.random()
            total = 0.0
            for unigram in unigrams:
                total += self._probability(prefix + unigram)
                if total >= threshold:
                    words.extend(unigram)
                    break
            # return the sentence if enough words were found
            if len(words) == n_words:
                return words
            # exit if it was impossible to find a plausible # ngram given the current partial sentence
            if total == 0.0:
                raise RuntimeError('impossible sequence')

    def smart_generate(self, n_words, gram_number):
        grams = [x for x in self._counts if len(x) == gram_number]
        lower_grams = [x for x in self._counts if len(x) == gram_number-1]
        # print('lower grams', lower_grams)
        threshold = random.random()
        qualified_grams = [x for x in lower_grams if self.probability(x) >= threshold]
        # print('test', threshold, qualified_grams)
        while len(qualified_grams) == 0:
            threshold = random.random()
            qualified_grams = [x for x in lower_grams if self.probability(x) >= threshold]
        # print('qualified grams', qualified_grams)
        sentence = []
        if gram_number > 1:
            sentence += list(qualified_grams[random.randint(0, len(qualified_grams) - 1)])
        # print('aaaa',sentence)
        while len(sentence) < n_words:
            self._smart_generate(sentence, grams, gram_number)
        return sentence

    def _smart_generate(self, sentence, grams, gram_number):
        # print(sentence, grams)
        prefix = sentence[len(sentence)-gram_number+1:len(sentence)]
        # print('sentence', sentence)
        # print('prefix', prefix)
        # print('grams', grams)
        with_prefix = [x for x in grams if list(x[0:gram_number-1]) == prefix]
        # for x in grams:
        #     print(list(x[0:gram_number-1]), prefix)
        #     if list(x[0:gram_number-1]) == prefix:
        #         print('YYYYYYYYEEEEEEEESSSSSSSS')

        # print('with_prefix', with_prefix)
        threshold = random.random()
        qualified_grams = [x for x in with_prefix if self.probability(x) >= threshold]
        while len(qualified_grams) == 0:
            threshold = random.random()
            qualified_grams = [x for x in with_prefix if self.probability(x) >= threshold]
        sentence.append(qualified_grams[random.randint(0, len(qualified_grams) - 1)][gram_number-1])

    def perplexity(self, words):
        prob = self.probability(words)
        return math.pow(prob, -1/len(words))

if __name__ == '__main__':
    words = ['i', 'am', 'sam', 'sam', 'i', 'am', 'i', 'do', 'not', 'like']
    # unigram = NGrams(1, words)
    # unigram.update(['hey', 'yo'])
    # print(unigram._counts)
    # print(unigram._probability(['sam']))
    # print(unigram.probability(['i']))

    # bigram = NGrams(2, words)
    # print(bigram._counts)
    # print(bigram.probability(['i', 'am']))

    ## TRY OTHER CORPORA
    romeo_and_juliet = ['enter', 'sampson', 'and', 'gregory', 'with', 'swords', 'and', 'bucklers', 'of', 'the', 'houseof', 'capulet', 'samp', 'gregory', 'on', 'my', 'word', "we'll", 'not', 'carry', 'coals', 'greg', 'no', 'for', 'then', 'we', 'should', 'be', 'colliers', 'samp', 'i', 'mean', 'an', 'we', 'be', 'in', 'choler', "we'll", 'draw', 'greg', 'ay', 'while', 'you', 'live', 'draw', 'your', 'neck', 'out', 'of', 'collar', 'samp', 'i', 'strike', 'quickly', 'being', 'moved', 'greg', 'but', 'thou', 'art', 'not', 'quickly', 'moved', 'to', 'strike', 'samp', 'a', 'dog', 'of', 'the', 'house', 'of', 'montague', 'moves', 'me', 'greg', 'to', 'move', 'is', 'to', 'stir', 'and', 'to', 'be', 'valiant', 'is', 'to', 'stand', 'therefore', 'if', 'thou', 'art', 'moved', 'thou', "runn'st", 'away', 'samp', 'a', 'dog', 'of', 'that', 'house', 'shall', 'move', 'me', 'to', 'stand', 'i', 'will', 'takethe', 'wall', 'of', 'any', 'man', 'or', 'maid', 'of', "montague's", 'greg', 'that', 'shows', 'thee', 'a', 'weak', 'slave', 'for', 'the', 'weakest', 'goes', 'to', 'the', 'wall', 'samp', "'tis", 'true', 'and', 'therefore', 'women', 'being', 'the', 'weaker', 'vessels', 'are', 'ever', 'thrust', 'to', 'the', 'wall', 'therefore', 'i', 'will', 'push', "montague's", 'men', 'from', 'the', 'wall', 'and', 'thrust', 'his', 'maids', 'to', 'the', 'wall', 'greg', 'the', 'quarrel', 'is', 'between', 'our', 'masters', 'and', 'us', 'their', 'men', 'samp', "'tis", 'all', 'one', 'i', 'will', 'show', 'myself', 'a', 'tyrant', 'when', 'i', 'havefought', 'with', 'the', 'men', 'i', 'will', 'be', 'cruel', 'with', 'the', 'maids', 'i', 'will', 'cut', 'off', 'their', 'heads', 'greg', 'the', 'heads', 'of', 'the', 'maids', 'samp', 'ay', 'the', 'heads', 'of', 'the', 'maids', 'or', 'their', 'maidenheads', 'take', 'it', 'in', 'what', 'sense', 'thou', 'wilt', 'greg', 'they', 'must', 'take', 'it', 'in', 'sense', 'that', 'feel', 'it', 'samp', 'me', 'they', 'shall', 'feel', 'while', 'i', 'am', 'able', 'to', 'stand', 'and', "'tisknown", 'i', 'am', 'a', 'pretty', 'piece', 'of', 'flesh', 'greg', "'tis", 'well', 'thou', 'art', 'not', 'fish', 'if', 'thou', 'hadst', 'thou', 'hadstbeen', 'poor', 'john', 'draw', 'thy', 'tool', 'here', 'comes', 'two', 'of', 'the', 'house', 'of', 'montagues', 'enter', 'two', 'other', 'servingmen', 'abram', 'and', 'balthasar', 'samp', 'my', 'naked', 'weapon', 'is', 'out', 'quarrel', 'i', 'will', 'back', 'thee', 'greg', 'how', 'turn', 'thy', 'back', 'and', 'run', 'samp', 'fear', 'me', 'not', 'greg', 'no', 'marry', 'i', 'fear', 'thee', 'samp', 'let', 'us', 'take', 'the', 'law', 'of', 'our', 'sides', 'let', 'them', 'begin', 'greg', 'i', 'will', 'frown', 'as', 'i', 'pass', 'by', 'and', 'let', 'them', 'take', 'it', 'as', 'theylist', 'samp', 'nay', 'as', 'they', 'dare', 'i', 'will', 'bite', 'my', 'thumb', 'at', 'them', 'which', 'is', 'disgrace', 'to', 'them', 'if', 'they', 'bear', 'it', 'abr', 'do', 'you', 'bite', 'your', 'thumb', 'at', 'us', 'sir', 'samp', 'i', 'do', 'bite', 'my', 'thumb', 'sir', 'abr', 'do', 'you', 'bite', 'your', 'thumb', 'at', 'us', 'sir', 'samp', 'aside', 'to', 'gregory', 'is', 'the', 'law', 'of', 'our', 'side', 'if', 'i', 'say', 'ay', 'greg', 'aside', 'to', 'sampson', 'no', 'samp', 'no', 'sir', 'i', 'do', 'not', 'bite', 'my', 'thumb', 'at', 'you', 'sir', 'but', 'i', 'bitemy', 'thumb', 'sir', 'greg', 'do', 'you', 'quarrel', 'sir', 'abr', 'quarrel', 'sir', 'no', 'sir', 'samp', 'but', 'if', 'you', 'do', 'sir', 'am', 'for', 'you', 'i', 'serve', 'as', 'good', 'a', 'man', 'asyou', 'abr', 'no', 'better', 'samp', 'well', 'sir', 'enter', 'benvolio', 'greg', 'aside', 'to', 'sampson', 'say', "'better", "'", 'here', 'comes', 'one', 'of', 'my', "master's", 'kinsmen', 'samp', 'yes', 'better', 'sir', 'abr', 'you', 'lie', 'samp', 'draw', 'if', 'you', 'be', 'men', 'gregory', 'remember', 'thy', 'swashing', 'blow', 'they', 'fight', 'ben', 'part', 'fools', 'beats', 'down', 'their', 'swords', 'put', 'up', 'your', 'swords', 'you', 'know', 'not', 'what', 'you', 'do', 'enter', 'tybalt', 'tyb', 'what', 'art', 'thou', 'drawn', 'among', 'these', 'heartless', 'hinds', 'turn', 'thee', 'benvolio', 'look', 'upon', 'thy', 'death', 'ben', 'i', 'do', 'but', 'keep', 'the', 'peace', 'put', 'up', 'thy', 'sword', 'or', 'manage', 'it', 'to', 'part', 'these', 'men', 'with', 'me', 'tyb', 'what', 'drawn', 'and', 'talk', 'of', 'peace', 'i', 'hate', 'the', 'word', 'as', 'i', 'hate', 'hell', 'all', 'montagues', 'and', 'thee', 'have', 'at', 'thee', 'coward', 'they', 'fight']
    romeo_and_juliet1 = ['enter', 'sampson', 'and', 'gregory', 'with', 'swords', 'and', 'bucklers', 'of', 'the']

    # most common ngrams
    # unigram
    # unigram = NGrams(1, romeo_and_juliet)
    # print(sorted(unigram._counts.items(), key=lambda k_v:k_v[1], reverse=True))
    # print(unigram.probability(['on']))
    # [((), 574), (('i',), 23), (('the',), 20), (('samp',), 20), (('of',), 16), (('greg',), 15), (('to',), 15), (('and',), 12)]
    # 0.020905923344947737

    # bigram
    # bigram = NGrams(2, romeo_and_juliet)
    # print(bigram.probability(['on', 'my']))

    # generate random sentence
    # unigram = NGrams(1, romeo_and_juliet)
    # print(unigram.generate(8))
    # ["master's", 'a', 'quarrel', 'choler', 'bucklers', 'i', 'am', 'the']

    # generate smart sentence with random beginning words
    # unigram
    # unigram = NGrams(1, romeo_and_juliet)
    # print(unigram.smart_generate(9, 1))
    # bigram
    # bigram = NGrams(2, romeo_and_juliet)
    # print(bigram.smart_generate(7, 2))




    # bigram = NGrams(2, romeo_and_juliet)
    # print(bigram.generate(9))

    ## TRY OTHER CORPORA
    customer_service = ['hi', 'firstname', 'thanks', 'for', 'opting', 'in', 'for', 'sms', 'updates', 'from', 'companyname', 'please', 'reply', 'with', 'y', 'to', 'confirm', 'you', 'can', 'text', 'stop', 'at', 'any', 'time', 'to', 'unsubscribe', 'hi', 'there', 'our', 'sms', 'customer', 'service', 'hours', 'are', 'monday', 'through', 'friday', 'from', '9am', 'pst', 'to', '5pm', 'pst', 'we', 'look', 'forward', 'to', 'responding', 'then', 'thanks', 'for', 'texting', 'companyname', 'it', 'will', 'take', 'about', '2', '5', 'minutes', 'for', 'a', 'team', 'member', 'to', 'respond', 'talk', 'to', 'you', 'soon', 'i', 'enjoyed', 'talking', 'with', 'you', 'today', 'firstname', 'would', 'you', 'consider', 'leaving', 'our', 'team', 'some', 'feedback', 'if', 'so', 'please', 'take', 'this', '2', 'question', 'survey', 'reply', 'with', 'stop', 'at', 'any', 'time', 'to', 'unsubscribe', 'from', 'sms', 'notifications', 'hi', 'firstname', 'we', 'are', 'at', 'companyname', 'hope', 'you’re', 'doing', 'well', 'today', 'as', 'a', 'rewards', 'customer', 'would', 'you', 'be', 'interested', 'in', 'spreading', 'the', 'news', 'about', 'our', 'services', 'if', 'so', 'please', 'leave', 'a', 'yelp', 'review', 'here', 'reply', 'with', 'stop', 'at', 'any', 'time', 'to', 'unsubscribe', 'from', 'sms', 'notifications', 'hi', 'firstname', 'it', 'looks', 'like', 'you', 'had', 'an', 'issue', 'with', 'your', 'order', 'sorry', 'about', 'that', 'we’re', 'working', 'on', 'it', 'right', 'now', 'and', 'will', 'send', 'you', 'a', 'msg', 'once', 'it’s', 'resolved', 'dear', 'vip', 'customer', 'show', 'this', 'sms', 'to', 'your', 'waiter', 'to', 'receive', 'a', 'complimentary', 'drink', 'with', 'your', 'next', '3', 'meals', 'be', 'the', 'first', 'to', 'know', 'about', 'discounts', 'and', 'offers', 'at', 'companyname', 'click', 'here', 'to', 'subscribe']
    # bigram = NGrams(2, customer_service)
    # print(bigram._counts)
    # print(bigram.probability(['for', 'opting']))
    # print(bigram.perplexity(['hi', 'firstname']))

    # unigram
    unigram = NGrams(1, customer_service)
    print(unigram.smart_generate(15, 1))

    # bigram
    bigram = NGrams(2, customer_service)
    # bigram._counts
    # lower_grams = [x for x in bigram._counts if len(x) == 1]
    # print(lower_grams)
    print(bigram.smart_generate(15, 2))

    # trigram
    trigram = NGrams(3, customer_service)
    print(trigram.smart_generate(15, 3))

    # fourgram
    fourgram = NGrams(4, customer_service)
    print(fourgram.smart_generate(15, 4))




