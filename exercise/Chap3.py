### 3.8, 3.9, 3.10, 3.11 ###
from __future__ import division
from collections import defaultdict as ddict
# import itertools
# import math
# import random

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
            return ngram_count / prefix_count
        else:
            return 0.0


if __name__ == '__main__':
    words = ['i', 'am', 'sam']
    unigram = NGrams(1, words)
    unigram.update(['hey', 'yo'])
    # print(unigram._counts)
    # print(unigram._probability(['o']))
    # print(unigram.probability(['yo']))

    # bigram = NGrams(2, words)
    # print(bigram._counts)
    # print(bigram.probability(['i', 'am']))

    romeo_and_juliet = ['enter', 'sampson', 'and', 'gregory', 'with', 'swords', 'and', 'bucklers', 'of', 'the', 'houseof', 'capulet', 'samp', 'gregory', 'on', 'my', 'word', "we'll", 'not', 'carry', 'coals', 'greg', 'no', 'for', 'then', 'we', 'should', 'be', 'colliers', 'samp', 'i', 'mean', 'an', 'we', 'be', 'in', 'choler', "we'll", 'draw', 'greg', 'ay', 'while', 'you', 'live', 'draw', 'your', 'neck', 'out', 'of', 'collar', 'samp', 'i', 'strike', 'quickly', 'being', 'moved', 'greg', 'but', 'thou', 'art', 'not', 'quickly', 'moved', 'to', 'strike', 'samp', 'a', 'dog', 'of', 'the', 'house', 'of', 'montague', 'moves', 'me', 'greg', 'to', 'move', 'is', 'to', 'stir', 'and', 'to', 'be', 'valiant', 'is', 'to', 'stand', 'therefore', 'if', 'thou', 'art', 'moved', 'thou', "runn'st", 'away', 'samp', 'a', 'dog', 'of', 'that', 'house', 'shall', 'move', 'me', 'to', 'stand', 'i', 'will', 'takethe', 'wall', 'of', 'any', 'man', 'or', 'maid', 'of', "montague's", 'greg', 'that', 'shows', 'thee', 'a', 'weak', 'slave', 'for', 'the', 'weakest', 'goes', 'to', 'the', 'wall', 'samp', "'tis", 'true', 'and', 'therefore', 'women', 'being', 'the', 'weaker', 'vessels', 'are', 'ever', 'thrust', 'to', 'the', 'wall', 'therefore', 'i', 'will', 'push', "montague's", 'men', 'from', 'the', 'wall', 'and', 'thrust', 'his', 'maids', 'to', 'the', 'wall', 'greg', 'the', 'quarrel', 'is', 'between', 'our', 'masters', 'and', 'us', 'their', 'men', 'samp', "'tis", 'all', 'one', 'i', 'will', 'show', 'myself', 'a', 'tyrant', 'when', 'i', 'havefought', 'with', 'the', 'men', 'i', 'will', 'be', 'cruel', 'with', 'the', 'maids', 'i', 'will', 'cut', 'off', 'their', 'heads', 'greg', 'the', 'heads', 'of', 'the', 'maids', 'samp', 'ay', 'the', 'heads', 'of', 'the', 'maids', 'or', 'their', 'maidenheads', 'take', 'it', 'in', 'what', 'sense', 'thou', 'wilt', 'greg', 'they', 'must', 'take', 'it', 'in', 'sense', 'that', 'feel', 'it', 'samp', 'me', 'they', 'shall', 'feel', 'while', 'i', 'am', 'able', 'to', 'stand', 'and', "'tisknown", 'i', 'am', 'a', 'pretty', 'piece', 'of', 'flesh', 'greg', "'tis", 'well', 'thou', 'art', 'not', 'fish', 'if', 'thou', 'hadst', 'thou', 'hadstbeen', 'poor', 'john', 'draw', 'thy', 'tool', 'here', 'comes', 'two', 'of', 'the', 'house', 'of', 'montagues', 'enter', 'two', 'other', 'servingmen', 'abram', 'and', 'balthasar', 'samp', 'my', 'naked', 'weapon', 'is', 'out', 'quarrel', 'i', 'will', 'back', 'thee', 'greg', 'how', 'turn', 'thy', 'back', 'and', 'run', 'samp', 'fear', 'me', 'not', 'greg', 'no', 'marry', 'i', 'fear', 'thee', 'samp', 'let', 'us', 'take', 'the', 'law', 'of', 'our', 'sides', 'let', 'them', 'begin', 'greg', 'i', 'will', 'frown', 'as', 'i', 'pass', 'by', 'and', 'let', 'them', 'take', 'it', 'as', 'theylist', 'samp', 'nay', 'as', 'they', 'dare', 'i', 'will', 'bite', 'my', 'thumb', 'at', 'them', 'which', 'is', 'disgrace', 'to', 'them', 'if', 'they', 'bear', 'it', 'abr', 'do', 'you', 'bite', 'your', 'thumb', 'at', 'us', 'sir', 'samp', 'i', 'do', 'bite', 'my', 'thumb', 'sir', 'abr', 'do', 'you', 'bite', 'your', 'thumb', 'at', 'us', 'sir', 'samp', 'aside', 'to', 'gregory', 'is', 'the', 'law', 'of', 'our', 'side', 'if', 'i', 'say', 'ay', 'greg', 'aside', 'to', 'sampson', 'no', 'samp', 'no', 'sir', 'i', 'do', 'not', 'bite', 'my', 'thumb', 'at', 'you', 'sir', 'but', 'i', 'bitemy', 'thumb', 'sir', 'greg', 'do', 'you', 'quarrel', 'sir', 'abr', 'quarrel', 'sir', 'no', 'sir', 'samp', 'but', 'if', 'you', 'do', 'sir', 'am', 'for', 'you', 'i', 'serve', 'as', 'good', 'a', 'man', 'asyou', 'abr', 'no', 'better', 'samp', 'well', 'sir', 'enter', 'benvolio', 'greg', 'aside', 'to', 'sampson', 'say', "'better", "'", 'here', 'comes', 'one', 'of', 'my', "master's", 'kinsmen', 'samp', 'yes', 'better', 'sir', 'abr', 'you', 'lie', 'samp', 'draw', 'if', 'you', 'be', 'men', 'gregory', 'remember', 'thy', 'swashing', 'blow', 'they', 'fight', 'ben', 'part', 'fools', 'beats', 'down', 'their', 'swords', 'put', 'up', 'your', 'swords', 'you', 'know', 'not', 'what', 'you', 'do', 'enter', 'tybalt', 'tyb', 'what', 'art', 'thou', 'drawn', 'among', 'these', 'heartless', 'hinds', 'turn', 'thee', 'benvolio', 'look', 'upon', 'thy', 'death', 'ben', 'i', 'do', 'but', 'keep', 'the', 'peace', 'put', 'up', 'thy', 'sword', 'or', 'manage', 'it', 'to', 'part', 'these', 'men', 'with', 'me', 'tyb', 'what', 'drawn', 'and', 'talk', 'of', 'peace', 'i', 'hate', 'the', 'word', 'as', 'i', 'hate', 'hell', 'all', 'montagues', 'and', 'thee', 'have', 'at', 'thee', 'coward', 'they', 'fight']
    unigram.update(romeo_and_juliet)
    print(sorted(unigram._counts.items(), key=lambda k_v:k_v[1], reverse=True))
    # print(unigram.probability(['yo']))