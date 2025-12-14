Tony Teaches Tech
### creates new user in ubuntu
### adduser username
### adds root privilages
### usermod -aG sudo username
### ssh username@website.com
ssh-keygen -t ed25519 -C "my website comment"
## will copy public key to remote site
ssh-copy-id username@website.com

### remove root and deactivate password login
sudo vi /etc/ssh/sshd_config
Change from yes to No
PermitRootLogin no
PasswordAuthentication no
PermitEmptyPasswords no
KbdInteractiveAuthentication no
UsePAM no
X11Forwarding no (graphic user interface)
(Add) AuthenticantionMethos publickey
AllowUsers username

### sudo systemctl restart ssh
test
try to login with a fake account
meowmeow@yoursite.com
try to login with root
############################
nltk word relations word clusters
word clusters
Sigmoid Function
{\displaystyle f(x)={\frac {1}{1+e^{-x}}}}

Algorithmic wage discrimination
Keynote Speaker - Cory Doctorow

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

gunicorn
https://www.youtube.com/watch?v=KWIIPKbdxD0

MORPHEMES
Inflectional vs. Derivational Suffixes
https://en.wikipedia.org/wiki/Prefix

https://brm.io/matter-js/demo/#softBody
https://brm.io/matter-js/demo/#airFriction

https://www.youtube.com/watch?v=MCCnka3AycQ


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]
