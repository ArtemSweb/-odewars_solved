def pig_it(text):
    lst = text.split()
    return ' '.join([elem[1:]+elem[0]+'ay' if elem.isalpha() else elem for elem in lst])



print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('O tempora o mores !')) # igPay atinlay siay oolcay