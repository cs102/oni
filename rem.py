def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

print(remove_prefix("corruptible", "rupt"))
