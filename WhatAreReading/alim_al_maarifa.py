import os.path
from urllib.request import urlopen


def download_file(download_url, filename):
    response = urlopen(download_url)
    file = open(filename, 'wb')
    file.write(response.read())
    file.close()


def verifier_existance(filename):
    return os.path.exists(filename)


logo = '''
    ***************************************************************
    *** Coded by  Abou èlè2 il jèm3i  أبو آلاء الجامعي           ***
    *** mail : tunisian-whitehat-security-team@googlegroups.com ***
    *** web  : http://www.whitehats.tn                          ***
    *** fb   : https://www.facebook.com/WhiteHats.tn            ***
    *** FOR all WhatAreReading Members                          ***
    ***************************************************************
'''
choice = '''
    You want to download all 300 books or just 1 book?
    1 : Enter 1 to download all 300 books
    2 : Enter 2 to download just 1 book
'''
exiit = '''
    You want to continue downloading or EXit
    y : Enter y to continue ;
    n : Enter n to exit     ;
'''
motal3a = '''
********************************************
    اللهم علمنا ما ينفعنا  و إنفعنا بما علمتنا
سبحانك انك أنت العليم الحكيم
********************************************
'''
url1 = "http://ia801404.us.archive.org/12/items/aalam_almaarifa/"
url2 = "https://ia701201.us.archive.org/19/items/khaldialibrary-maarifa/"
continuer = "y"
print(logo)
while continuer == "y":
    choix = input(choice)
    choix = int(choix)
    if choix == 1:
        for x in range(1, 289):
            if x == 268:
                continue

            if x < 10:
                xString = "00" + str(x)
            elif x < 100:
                xString = "0" + str(x)
            else:
                xString = str(x)

            if x > 268:
                url = url2 + xString + ".pdf"
            else:
                url = url1 + xString + ".pdf"

            if verifier_existance(xString + ".pdf"):
                print("THE file exist :D ")
            else:
                download_file(url, xString + ".pdf")
    else:
        book = input("Enter the number of your  Book  : ")
        book = int(book)
        if book == 268:
            print ("This book is not FOUND")
        elif book > 289:
            print ("the last book in our data base is 289 :)  ")
        else:
            if book < 10:
                xString = "00" + str(book)
            elif book < 100:
                xString = "0" + str(book)
            else:
                xString = str(book)

            if book > 268:
                url = url2 + xString + ".pdf"
            else:
                url = url1 + xString + ".pdf"

            if verifier_existance(xString + ".pdf"):
                print("THE file exist :D ")
            else:
                download_file(url, xString + ".pdf")
    continuer = input(exiit)
print(motal3a)
xxxxx = input("press <Enter> to exit ")
