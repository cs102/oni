'''
SPLIT SYLLABLES
Jeff Thompson | 2016 | jeffreythompson.org
Requires this modified version of the CMU Pronouncing
dictionary by Susan Bartlett, Grzegorz Kondrak and Colin Cherry: 
https://webdocs.cs.ualberta.ca/~kondrak/cmudict.html
Download and save to your project directory, or somewhere you can
easily reference it.
'''

dict_filename = 'cmudict.rep'

syllable_dict = {}
with open(dict_filename) as f:
    for line in f:
        line = line.strip()
        line = line.lower()

        # ignore comments
        if line.startswith('##'):
            continue
        
        try:
            word, phones = line.split('  ')
            syll = phones.split(' - ')
            syllable_dict[word] = syll
        except:
            print('error parsing word ' + word)

print ('the',  syllable_dict['the']) 
print ('beautiful', syllable_dict['beautiful'])

print ('serious',syllable_dict['serious'])
print ('seriously',syllable_dict['seriously'])
