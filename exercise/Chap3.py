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
    # print(unigram.smart_generate(15, 1))

    # bigram
    bigram = NGrams(2, customer_service)
    # bigram._counts
    # lower_grams = [x for x in bigram._counts if len(x) == 1]
    # print(lower_grams)
    # print(bigram.smart_generate(15, 2))

    # trigram
    trigram = NGrams(3, customer_service)
    # print(trigram.smart_generate(15, 3))

    # fourgram
    fourgram = NGrams(4, customer_service)
    # print(fourgram.smart_generate(15, 4))


    # Quyuan
    quyuan = ['若', '有', '人', '兮', '山', '之', '阿', '被', '薜', '荔', '兮', '带', '女', '萝', '既', '含', '睇', '兮', '又', '宜', '笑', '子', '慕', '予', '兮', '善', '窈', '窕', '乘', '赤', '豹', '兮', '从', '文', '狸', '辛', '夷', '车', '兮', '结', '桂', '旗', '被', '石', '兰', '兮', '带', '杜', '衡', '折', '芳', '馨', '兮', '遗', '所', '思', '余', '处', '幽', '篁', '兮', '终', '不', '见', '天', '路', '险', '难', '兮', '独', '后', '来', '表', '独', '立', '兮', '山', '之', '上', '云', '容', '容', '兮', '而', '在', '下', '杳', '冥', '冥', '兮', '羌', '昼', '晦', '东', '风', '飘', '兮', '神', '灵', '雨', '留', '灵', '修', '兮', '憺', '忘', '归', '岁', '既', '晏', '兮', '孰', '华', '予', '采', '三', '秀', '兮', '于', '山', '间', '石', '磊', '磊', '兮', '葛', '蔓', '蔓', '怨', '公', '子', '兮', '怅', '忘', '归', '君', '思', '我', '兮', '不', '得', '闲', '山', '中', '人', '兮', '芳', '杜', '若', '饮', '石', '泉', '兮', '荫', '松', '柏', '君', '思', '我', '兮', '然', '疑', '作', '雷', '填', '填', '兮', '雨', '冥', '冥', '猿', '啾', '啾', '兮', '狖', '夜', '鸣', '风', '飒', '飒', '兮', '木', '萧', '萧', '思', '公', '子', '兮', '徒', '离', '忧', '帝', '子', '降', '兮', '北', '渚', '目', '眇', '眇', '兮', '愁', '予', '袅', '袅', '兮', '秋', '风', '洞', '庭', '波', '兮', '木', '叶', '下', '登', '白', '薠', '兮', '骋', '望', '与', '佳', '期', '兮', '夕', '张', '鸟', '何', '萃', '兮', '蘋', '中', '罾', '何', '为', '兮', '木', '上', '沅', '有', '茝', '兮', '醴', '有', '兰', '思', '公', '子', '兮', '未', '敢', '言', '荒', '忽', '兮', '远', '望', '观', '流', '水', '兮', '潺', '湲', '麋', '何', '食', '兮', '庭', '中', '蛟', '何', '为', '兮', '水', '裔', '朝', '驰', '余', '马', '兮', '江', '皋', '夕', '济', '兮', '西', '澨', '闻', '佳', '人', '兮', '召', '予', '将', '腾', '驾', '兮', '偕', '逝', '筑', '室', '兮', '水', '中', '葺', '之', '兮', '荷', '盖', '荪', '壁', '兮', '紫', '坛', '插', '芳', '椒', '兮', '盈', '堂', '桂', '栋', '兮', '兰', '橑', '辛', '夷', '楣', '兮', '药', '房', '罔', '薜', '荔', '兮', '为', '帷', '擗', '蕙', '櫋', '兮', '既', '张', '白', '玉', '兮', '为', '镇', '疏', '石', '兰', '兮', '为', '芳', '芷', '葺', '兮', '荷', '屋', '缭', '之', '兮', '杜', '衡', '合', '百', '草', '兮', '实', '庭', '建', '芳', '馨', '兮', '庑', '门', '九', '嶷', '缤', '兮', '并', '迎', '灵', '之', '来', '兮', '如', '云', '捐', '余', '袂', '兮', '江', '中', '遗', '余', '褋', '兮', '醴', '浦', '搴', '汀', '洲', '兮', '杜', '若', '将', '以', '遗', '兮', '远', '者', '时', '不', '可', '兮', '骤', '得', '聊', '逍', '遥', '兮', '容', '与', '屈', '原', '既', '放', '游', '于', '江', '潭', '行', '吟', '泽', '畔', '颜', '色', '憔', '悴', '形', '容', '枯', '槁', '渔', '父', '见', '而', '问', '之', '曰', '子', '非', '三', '闾', '大', '夫', '与', '何', '故', '至', '于', '斯', '屈', '原', '曰', '举', '世', '皆', '浊', '我', '独', '清', '众', '人', '皆', '醉', '我', '独', '醒', '是', '以', '见', '放', '渔', '父', '曰', '圣', '人', '不', '凝', '滞', '于', '物', '而', '能', '与', '世', '推', '移', '世', '人', '皆', '浊', '何', '不', '淈', '其', '泥', '而', '扬', '其', '波', '众', '人', '皆', '醉', '何', '不', '哺', '其', '糟', '而', '歠', '其', '醨', '何', '故', '深', '思', '高', '举', '自', '令', '放', '为', '屈', '原', '曰', '吾', '闻', '之', '新', '沐', '者', '必', '弹', '冠', '新', '浴', '者', '必', '振', '衣', '安', '能', '以', '身', '之', '察', '察', '受', '物', '之', '汶', '汶', '者', '乎', '宁', '赴', '湘', '流', '葬', '于', '江', '鱼', '之', '腹', '中', '安', '能', '以', '皓', '皓', '之', '白', '而', '蒙', '世', '俗', '之', '尘', '埃', '乎', '渔', '父', '莞', '尔', '而', '笑', '鼓', '枻', '而', '去', '乃', '歌', '曰', '沧', '浪', '之', '水', '清', '兮', '可', '以', '濯', '吾', '缨', '沧', '浪', '之', '水', '浊', '兮', '可', '以', '濯', '吾', '足', '遂', '去', '不', '复', '与', '言', '操', '吴', '戈', '兮', '披', '犀', '甲', '车', '错', '毂', '兮', '短', '兵', '接', '旌', '蔽', '日', '兮', '敌', '若', '云', '矢', '交', '坠', '兮', '士', '争', '先', '凌', '余', '阵', '兮', '躐', '余', '行', '左', '骖', '殪', '兮', '右', '刃', '伤', '霾', '两', '轮', '兮', '絷', '四', '马', '援', '玉', '枹', '兮', '击', '鸣', '鼓', '天', '时', '怼', '兮', '威', '灵', '怒', '严', '杀', '尽', '兮', '弃', '原', '野', '出', '不', '入', '兮', '往', '不', '反', '平', '原', '忽', '兮', '路', '超', '远', '带', '长', '剑', '兮', '挟', '秦', '弓', '首', '身', '离', '兮', '心', '不', '惩', '诚', '既', '勇', '兮', '又', '以', '武', '终', '刚', '强', '兮', '不', '可', '凌', '身', '既', '死', '兮', '神', '以', '灵', '魂', '魄', '毅', '兮', '为', '鬼', '雄', '后', '皇', '嘉', '树', '橘', '徕', '服', '兮', '受', '命', '不', '迁', '生', '南', '国', '兮', '深', '固', '难', '徙', '更', '壹', '志', '兮', '绿', '叶', '素', '荣', '纷', '其', '可', '喜', '兮', '曾', '枝', '剡', '棘', '圆', '果', '抟', '兮', '青', '黄', '杂', '糅', '文', '章', '烂', '兮', '精', '色', '内', '白', '类', '任', '道', '兮', '纷', '缊', '宜', '脩', '姱', '而', '不', '丑', '兮', '嗟', '尔', '幼', '志', '有', '以', '异', '兮', '独', '立', '不', '迁', '岂', '不', '可', '喜', '兮', '深', '固', '难', '徙', '廓', '其', '无', '求', '兮', '苏', '世', '独', '立', '横', '而', '不', '流', '兮', '闭', '心', '自', '慎', '终', '不', '失', '过', '兮', '秉', '德', '无', '私', '参', '天', '地', '兮', '愿', '岁', '并', '谢', '与', '长', '友', '兮', '淑', '离', '不', '淫', '梗', '其', '有', '理', '兮', '年', '岁', '虽', '少', '可', '师', '长', '兮', '行', '比', '伯', '夷', '置', '以', '为', '像', '兮']


    unigram = NGrams(3, quyuan)
    print(unigram.smart_generate(30, 3))

