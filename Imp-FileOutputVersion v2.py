##Reference Stuff: ###

#Random Test IP:     221.241.59.100
#f.close()
#readme https://github.com/jkerai1/ImpTemplate/blob/main/README.md


#################     Imports         #############################
import re #Regex
import os #for getting username
import datetime #get datestamp
from pathlib import Path #for seeing if file exists or not
import sys
import webbrowser
#import snow ##I have a seperate script to open snow  , comment this out 

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

punc_filter = re.compile('([/\s]\s*)')  #Check for whitespaces or backslashes

def check(Ip): ##see if IP is valid using Regex, whitespaces are removed when reading in anyway
    
    if(re.search(regex, Ip)):
        pass ##no need to do anything if IP is valid
    else:
        
        if Ip.__contains__("sno"): ##shortcut to snow
            
            print("insert your snow link here using webbrowser.open(""www."")") ##if using jupyter adding to a seperate block would be better
            
        f.close() #close file stream
        sys.exit("Invalid IP address")
        
        
def Printfunc(IP): #simple func to print IP to console as well as write to the text file
    print("\n" + "IP: "  + IP) 
    f =open(filepath,"a")
    f.write("\n" + "IP: "  + IP + "\n")
    f.close()

        
def PrintAndAppend(stringtoappend):
    print(stringtoappend)
    f =open(filepath,"a")
    f.write(stringtoappend +"\n")
    f.close()
    
    
def GetBrowserAndCountry():
    Browser = input("what is browser?   ").lower()
    
###  Clean up shorthand############################### probably a better way to do this using regex, dictionary and .split()#############

###Chrome###
    if Browser.__contains__("chr") and not Browser.__contains__("chrome"):
        Browser = (Browser.replace("chr","Chrome"))
    
    if Browser.__contains__("cr"): 
        Browser = (Browser.replace("cr","Chrome"))

###Firefox####
    if Browser.__contains__("ff") and not Browser.__contains__("ffox"):
        Browser = (Browser.replace("ff","Firefox"))
       
    if Browser.__contains__("ffox"):   
        Browser = (Browser.replace("ffox","Firefox"))
       
        
###Safari#######        

    if Browser.__contains__("saf") and not Browser.__contains__("safari"):
        Browser = (Browser.replace("saf","Safari"))

####Edge#####
        
    if Browser.__contains__("edg") and not Browser.__contains__("edge"):
        Browser = (Browser.replace("edg", "Edge"))
    
###opera###        

    if ("op" in Browser) and not Browser.__contains__("opera"):
        Browser = (Browser.replace("op", "Opera"))
###Yandex###

    if "ya" in Browser and not Browser.__contains__("yandex") and not Browser.__contains__("yan"):
        Browser = (Browser.replace("ya", "Yandex"))
        
    if "yan" in Browser and not ("yandex") in Browser:
        Browser = (Browser.replace("yan", "Yandex"))
        
###F1 App####
    if "f1" in Browser and not "f1 app" in Browser:
        Browser = Browser.replace("f1","F1 App")
    
        
        
    Browser = punc_filter.split(Browser)
    Browser = ''.join([i.capitalize() for i in Browser])
        
    Country =input ("what is country?   ").upper().replace(" ","") ##convert to upper and remove whitespaces
    Country = re.sub(r'[^\w\s]', '', Country) ##strip punctuation
    
    return Browser, Country    


def CapitaliseEveryFirstLetter(someString): ##Capitalise every first letter ###
        someString = someString.split()
        newString =""
        
        for val in someString:
            
            if val.isupper():
                newString += val +  " "
            
            else:
                newString += val.capitalize()+  " "

        return newString
    



###########Create New file or check if one exists############################

date =  datetime.datetime.now().strftime("%d-%m-%y")
filepath = os.path.join("C:\\Users\\" + os.getlogin() + "\\Desktop","Imperva - " + date + ".txt") ##get user name. ##Syntax:  os.path.join(dir_name, base_filename + "." + filename_suffix)

#note can easily be changed to a different file format like .doc using a library


#see if file exists, if it doesn't then make one.        
if Path(filepath).is_file(): 
    print ("File exist -> " + filepath) #f =open(filepath,"a") #by default it is text not binary
else:
    print ("File does not exist...creating one now... " + filepath)
    f =open(filepath, "x")#for a new file. if file already exists then to append use


##########################Body############################################################
while True: ##run infinitely until session timeout

###Get IP and Error####
    IP = (input("IP address: ?  ").replace(" ",""))
    IP = IP.replace("-", "") #sometimes they leave a dash at the end
    
    check(IP)
    Error_type = (input("Error_type ?  ").lower())
    
    ##if statement block to check to see which error we have##########

    if Error_type == "ns" or Error_type == "not seen" or Error_type == "n" or Error_type == "not" or Error_type == "no":
        Printfunc(IP)
        string_to_append  = ("\n" + "We can confirm that no traffic is seen on the Imperva portal for the IP provided.")
        PrintAndAppend(string_to_append)
    
    elif Error_type == "seen" or Error_type.__contains__("allo") or Error_type == "s":
        
        Browser,Country = GetBrowserAndCountry()
        Printfunc(IP)
        PrintAndAppend("Browser: " + Browser)
        PrintAndAppend("Country: "+ Country)
        
        string_allowed = ("\n" + "We can confirm that traffic for the IP provided is seen on the Imperva portal and is allowed.")
        PrintAndAppend(string_allowed)
        
 ##Special Cases, put first because order matters in Python:
       
    elif ("kvinv") in Error_type: ##both 
        
        Browser, Country = GetBrowserAndCountry()
        Geo = input("what is geo?   ").lstrip() ##remove left most spaces
        Geo = CapitaliseEveryFirstLetter(Geo)
        Printfunc(IP)
        PrintAndAppend("Browser: " + Browser) ##i could block this into one function if i really wanted to....
        PrintAndAppend("Country: "+ Country)
        PrintAndAppend("Geo Org: " + Geo  +"\n")
        PrintAndAppend("We can confirm the IP provided is currently being blocked due to a VPN or a hosted environment and blocked due to a Javascript or Browser cookie issue.")


###Normal Cases####
    elif ("inv") in Error_type or ("cook") in Error_type or "java" in Error_type or Error_type == "js" or Error_type.__contains__("forc") or Error_type == "fi" or Error_type.__contains__("bloc") or Error_type.__contains__("tok"):
        Browser, Country = GetBrowserAndCountry()
        Printfunc(IP)
        
        ##Browser
        browserString = ("Browser: " + Browser) 
        PrintAndAppend(browserString)
        
       ##Country
        CountryString = "Country: "+ Country + "\n"
        PrintAndAppend(CountryString)
        
        
        BlockedString  =  "We can confirm that traffic for the IP provided is currently blocked due to a Javascript or Browser cookie issue."
        PrintAndAppend(BlockedString)
    
    elif ("kv") in Error_type or Error_type.__contains__("vp") or Error_type.__contains__("host") or Error_type.__contains__("auto"):
        
        Browser, Country = GetBrowserAndCountry()
        Geo = input("what is geo?   ").lstrip() ##remove left most spaces
        Geo = CapitaliseEveryFirstLetter(Geo)
        Printfunc(IP)
        PrintAndAppend("Browser: " + Browser)
        PrintAndAppend("Country: "+ Country)
        PrintAndAppend("Geo Org: " + Geo  +"\n")
        PrintAndAppend("We can confirm the IP provided is currently being blocked due to a VPN or a hosted environment.")
    
        
  ##at this point I have all shorthand codes i think so i could use a dictionary.........
       
        
    else:
        print("\n incorrect option \n Options are: \n\n - not seen - not seen,ns,n.not,n \n\n - Seen - s,allow,allowed,s \n\n - traffic blocked - inv,invalid, cook, cookie, java, javascript, js, fi, forc, bloc, tok \n\n -KVDC - kv, kvdc, kvd, vp, vpn, host \n \nfor further info please see readme https://github.com/jkerai1/ImpTemplate/blob/main/README.md ")
        
        getReadMeOpenRequest = input("Would you like to go to the readme? (y) ").lower()
        
        if "y" in getReadMeOpenRequest:
            webbrowser.open("https://github.com/jkerai1/ImpTemplate/blob/main/README.md")
        else:
            pass
        
    PrintAndAppend("\n-------------------------------------------------------------------------------------------------------------------------") ##seperator  
    
    ##useful testing references:
    #Random Test IP:     221.241.59.100
    #f.close()
