#import cmudict
import pyphen
dic = pyphen.Pyphen(lang='fr_FR')
word = dic.inserted('fromage')
print(word)
dic = pyphen.Pyphen(lang='en_US')
word = dic.inserted('Hendecasyllable')
word1 = dic.inserted('synchronised')
word2 = dic.inserted('geosynchronous')
word3 = dic.inserted('glottochronology')
print(word)
print(word1)
print(word2)
print(word3)
