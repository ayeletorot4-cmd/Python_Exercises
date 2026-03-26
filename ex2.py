def star_odd(word: str) -> bool:
    return all(x=="*" for x in word[1::2])
print(star_odd("1*2*") )
print(star_odd("a*y*u*i*o*"))
print(star_odd("hello"))