def challenge0():
    print(2**38)
    
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

def challenge4():
    import urllib.request
    import re
    
    
    def geturl(purl, count):
        with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+purl) as url:
            text = url.read().decode('utf-8')
    
        print(text)
        address = re.search('the next nothing is \d+', text) #82682 alerta para o erro de buscar apenas o numero
    
        if address == None:
            print ('Dividing url by two...')
            purl = int(purl)/2 #como informado em 16044
            geturl(str(purl), count+1)
    
        else:
            address = re.search('\d+', address.group()) #separando apenas os numeros
            address = (address.group())
            if count < 400:
                geturl(address, count+1)

    geturl('12345', 0)

    #no meio dos next nothings, um indica peak.html
