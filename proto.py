# Extensive lists of common Latin and Greek prefixes and suffixes
latin_greek_prefixes = [
    'a', 'ab', 'ad', 'ante', 'anti', 'auto', 'bene', 'bi', 'circum', 'co', 'com', 'con', 'contra',
    'de', 'dis', 'en', 'ex', 'extra', 'in', 'inter', 'ir', 'iso', 'macro', 'micro', 'mono', 'multi', 
    'neo', 'non', 'out', 'over', 'peri', 'post', 'pre', 'pro', 're', 'retro', 'semi', 'sub', 'super', 
    'trans', 'tri', 'un', 'under', 'vice'
]

latin_greek_suffixes = [
    'able', 'age', 'al', 'ance', 'ancy', 'ant', 'arium', 'ary', 'ation', 'cide', 'cy', 'dom', 'ectomy', 
    'en', 'ence', 'ency', 'er', 'ern', 'es', 'esque', 'est', 'ful', 'fy', 'hood', 'ic', 'ical', 'ics', 'id', 
    'ion', 'ism', 'ist', 'ite', 'ity', 'ive', 'ization', 'less', 'let', 'ment', 'ness', 'oid', 'ology', 'oma', 
    'ous', 'pathy', 'phobia', 'scope', 'ship', 'sion', 'th', 'tion', 'tude', 'ure', 'ward', 'wise', 'y'
]

# Function to split the word into prefix, root, and suffix
def split_word(word):
    root = word
    prefix = None
    suffix = None

    # Check for prefix
    for p in latin_greek_prefixes:
        if word.startswith(p):
            prefix = p
            root = word[len(p):]
            break

    # Check for suffix
    for s in latin_greek_suffixes:
        if root.endswith(s):
            suffix = s
            root = root[:-len(s)]
            break

    return prefix, root, suffix

# Example usage
word = input("Enter a word: ").strip().lower()
prefix, root, suffix = split_word(word)

# Output the results
print(f"Prefix: {prefix if prefix else 'None'}")
print(f"Root: {root}")
print(f"Suffix: {suffix if suffix else 'None'}")

