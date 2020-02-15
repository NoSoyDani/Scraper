import webbrowser
from bs4 import BeautifulSoup
from colorama import init,Fore,Style,Back
import requests
import wget
import time
init()
#-----------------------------------------------------

print(Fore.YELLOW +                ' \n ')

print(Fore.BLUE +               '                            ▄████████    ▄████████ ███▄▄▄▄    ▄█   ▄██████▄  ███▄▄▄▄   ')
print(Fore.BLUE   +             '                            ███    ███   ███    ███ ███▀▀▀██▄ ███  ███    ███ ███▀▀▀██▄ ')
print(Fore.GREEN   +            '                            ███    █▀    ███    ███ ███   ███ ███▌ ███    ███ ███   ███ ')
print(Fore.GREEN   +            '                            ███          ███    ███ ███   ███ ███▌ ███    ███ ███   ███ ')
print(Fore.YELLOW   +           '                            ███        ▀███████████ ███   ███ ███▌ ███    ███ ███   ███ ')
print(Fore.YELLOW   +           '                            ███    █▄    ███    ███ ███   ███ ███  ███    ███ ███   ███ ')
print(Fore.RED  +               '                            ███    ███   ███    ███ ███   ███ ███  ███    ███ ███   ███ ')
print(Fore.RED   +              '                            ████████▀    ███    █▀   ▀█   █▀  █▀    ▀██████▀   ▀█   █▀  ')

print(Fore.MAGENTA  +                '            \n                                 Welcome to ION-Canion :D           by:YoNoSoyDani      \n')
print(Fore.WHITE+Style.BRIGHT  +   '                                                                                  \n')









URL=('http://'+ input('Insert URL in short format: (amazon.es)') + '/')
PB=input('Do you want see the raw file? :(YES/NO)')
MODE=input('Select MODE \n 1-FULL SCAN \n 2-URL SCAN \n 3-IMAGE SCAN \n I select: ')
r = requests.get(URL, stream=True)
R1=r.encoding
R3=r.content
R4=r.headers
R42=r.headers.get('server')
R5=r.status_code
encoding=("\'" + R1 +"\'")
print('--------------------------------------------------------------------------------------------------')
print('STATUS: ' , R5)
print('--------------------------------------------------------------------------------------------------')
print('ENCODING: ',R1)
print('--------------------------------------------------------------------------------------------------')
print('SERVER: ' , R42)
print('--------------------------------------------------------------------------------------------------')
print('RESPONSE: \n' , R4)
print('--------------------------------------------------------------------------------------------------')



time.sleep(3)


soup  =  BeautifulSoup (R3,'html.parser')


#____________________________________________________________________________________________________________-
def BASE_PAGE(R3):

    print(Back.RED+ '\n                      - BASE PAGE -                                  \n'+Back.RESET)


    if(PB=='YES'):
        print(R3)
    if(PB != 'YES' or PB != 'NO'):
        print("Okeeeyyy :)")





#------------------------------------------------------
def URL(MODE):

    if(MODE=="1" or MODE =="2" ):
        print(Back.RED + '\n                            - URL -                                   \n'+Back.RESET)


        tagsA = soup('link')
        for tag in tagsA:
            if((tag.get('href') !=  None ) and (len(tag.get('href')) != 0)  and (tag.get('href')[0] !='#')):
                print(tag.get('href'))


        print(Back.RED +'\n                     - MASSIVE REDIRECT -                                   \n'+Back.RESET)

        tags = soup('a')
        for tag in tags:
            if((tag.get('href') !=  None) and (len(tag.get('href')) != 0)  and (tag.get('href')[0] !='#')):
                print(tag.get('href'))


    #------------------------------------------------------
def IMAGES(MODE):
    if(MODE=="1" or MODE =="3" ):
        print(Back.RED+ '\n                      - IMAGES -                                  \n'+Back.RESET)
        cadena = input("Do you want to open the images in the web browser? (YES/NO):")
        dwld=input('Do you want to download the images? (YES/NO):')
        tags = soup('img')
        for tag in tags:
            if(tag.get('src') is not  None):
                image=tag.get('src')
                #imageM=("\'" + image +"\'")
                print(image)

            #BROWSER OPENING
            if(cadena=='YES'):
                webbrowser.open(image)
            #DOWNLOAD
            if((image.startswith('http://') == True) or (image.startswith('https://') == True) and ((image.endswith('.jpg')==True) or (image.endswith('.jpeg') == True) or (image.endswith('.png') == True)) and (dwld=='YES')):
                wget.download(image,'images')





#-----------------------------------------------------
def SCRIPT(MODE):
    if(MODE=="1" or MODE =="4" ):
        print(Back.RED+ '\n                      - SCRIPTS -                                  \n'+Back.RESET)
        tags = soup('embed')
        for tag in tags:
            if(tag.get('src') is not None):
                print(tag.get('src'))




#----------------------------------------------------
def OBJECT(MODE):
    if(MODE=="1"):
        print(Back.RED+ '\n                      - OBJECT -                                  \n'+Back.RESET)
        tags = soup('object')
        for tag in tags:
            if(tag.get('data') is not None):
                print(tag.get('data'))


#---------------------------------------------------
def VIDEO(MODE):

    if(MODE=="1"):
        print(Back.RED+ '\n                      - VIDEO -                                  \n'+Back.RESET)
        tags = soup('video')
        for tag in tags:
            if(tag.get('src') is not None):
                print(tag.get('src'))

#--------------------------------------------------
def AUDIO(MODE):

    if(MODE=="1"):
        print(Back.RED+ '\n                      - AUDIO -                                  \n'+Back.RESET)
        tags = soup('audio')
        for tag in tags:
            if(tag.get('src') is not None):
                print(tag.get('src'))
#--------------------------------------------------

def MAP(MODE):
    if(MODE=="1"):
        print((Back.RED+ '\n                      - MAP -                                  \n'+Back.RESET))
        tags = soup('map')
        for tag in tags:
            if(tag.get('name') is not None):
                print(tag.get('name'))

#--------------------------------------------------
def SOURCE(MODE):
    if(MODE=="1"):
        print(Back.RED+ '\n                      - SOURCE -                                  \n'+Back.RESET)
        tags = soup('source')
        for tag in tags:
            if(tag.get('src') is not None):
                print(tag.get('src'))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
BASE_PAGE(soup)
URL(MODE)
IMAGES(MODE)
SCRIPT(MODE)
OBJECT(MODE)
VIDEO(MODE)
AUDIO(MODE)
MAP(MODE)
SOURCE(MODE)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
