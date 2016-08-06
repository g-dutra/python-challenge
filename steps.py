def challenge1():
    #myString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    myString = "map"

    decrypt = ""
    #cifra de césar, somando a chave (2) em cada caractere
    for i in myString:
        if (i >= 'a' and i <= 'z'):
            tempc = ((ord(i) - ord('a')+ 2) % 26)
            decrypt += chr(tempc + ord('a'))
                       
        else:
            decrypt += i
                       
    print (decrypt)
    
    
def challenge2():
    import collections

    od = collections.OrderedDict() #porque um dicionario normal me daria um anagrama das letras do link
    chars = open('rarechars.txt')
    
    
    for line in chars:
        for c in line:
            if c in od:
                od[c] += 1
            else:
                od[c] = 1
    
    print (od)

    #os caracteres mais raros formam o proximo link: equality

def challenge3():
    import re
    equality = open('equality.txt')
    
    for line in equality:
        result = re.findall('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', line) #EXATAMENTE 3 uppercase = chars 1 e 8 são lower
        if result !=[]:
            print(result)
        
    # a letra em lowercase no meio de cada linha forma o próximo link: linkedlist
