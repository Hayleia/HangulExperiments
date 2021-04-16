from hangulcompose import *

print(typeSeq('ㄸㅏㄹㄱ'))
print(typeSeq('ㄸㅏㄹㄱㅣ'))
print(typeSeq('ㅅㅏㄱ'))
print(typeSeq('ㅅㅏㄱㅗㅏ'))
print(typeSeq('ㅅㅏ_'))

# combining jamos
print(f'{chr(0x1112)}{chr(0x119E)}{chr(0x11AB)}')
