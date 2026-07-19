def has_at_symbol(s:str) -> bool :
    i = 0;
    while i < len(s):
        if(s[i] == '@'):
            return True
        i += 1
    return False