def concatenate(s1: str, s2: str) -> str:
    fstr = s1 + s2
    if len(fstr) > 10:
        return "Too long!"
    else:
        return fstr




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
