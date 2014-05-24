FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    list = []
    list2 =[]
    final = ""
    
    s = str(number)
    i = 0
    for c in s:
        list2.append(c)
    
    ten = False
    hundred = False
    teen = False
    skip = False
    for c in reversed(s):
        if(ord(c) == 48 and ten == True):
            hundred = True
        elif(hundred == True):
            if(skip == True):
                skip = False
                continue
            else:
                list.append(((FIRST_TEN[ord(c) - 49]) + " hundred "))
        elif(ten == True):
            list.append(OTHER_TENS[ord(c) - 50] + " ")
            hundred = True
        else:
            if(len(s) == 1):
              list.append(FIRST_TEN[ord(c) - 49])
            else:
                if(len(s) == 2 and list2[0] == "1"):
                    list.append(SECOND_TEN[ord(c) - 48])
                    break
                elif(len(s) == 3 and list2[1] == "1"):
                    list.append(SECOND_TEN[ord(c) - 48])
                    hundred = True
                    skip = True
                else:
                    if(ord(c) == 48):
                        ten = True
                    else:
                        list.append(FIRST_TEN[ord(c) - 49])
                        ten = True
                  
                     
        
    for x in reversed(list):
        final += x
    #replace this for solution
    return final.strip()

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
