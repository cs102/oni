Fucking magic!
In vim this will select add "" around all words selected
:%s/\w\+/"&"/gc

Python Environment
cd to project
First time  -> python -m venv projectName
source projectName/bin/activate
https://www.w3schools.com/python/python_virtualenv.asp

python3 -m venv .venv
.. venv/bin/activate

# NLTK View all available corpus
import os
import nltk
print(os.listdir(nltk.data.find("corpora")))


##
List of Greek and Latin roots
https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/R

List of Base Words
https://simple.wikipedia.org/w/index.php?title=Category:Basic_English_850_words&pageuntil=Head#mw-pages

Python NLTK
Natural Language ToolKit

MORPHEMES
Inflectional vs. Derivational Suffixes
https://en.wikipedia.org/wiki/Prefix

https://brm.io/matter-js/demo/#softBody
https://brm.io/matter-js/demo/#airFriction

https://www.youtube.com/watch?v=MCCnka3AycQ


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]
