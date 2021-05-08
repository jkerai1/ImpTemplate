##Random Test IP: 221.241.59.100

import re
import sys

##Random Test IP: 221.241.59.100
##this file can be run in an online editor such as https://www.online-python.com/

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
punc_filter = re.compile('([/\s]\s*)')

def check(Ip): ##see if IP is valid using Regex
    if(re.search(regex, Ip)):
        pass ##no need to do anything if IP is valid
    else:
        sys.exit("Invalid IP address")
        
        
def Printfunc(IP):
    print("\n" + "IP: "  + IP)
  
def GetBrowserAndCountry():
    Browser = input("what is browser?   ").lower()


def CapitaliseEveryFirstLetter(someString): ##Capitalise every first letter ###
        someString = someString.split()
        newString =""
        
        for val in someString:
            newString += val.capitalize()+  " "
            
        return newString
            
    
####################Clean up shorthand###############################

###Chrome###
    if Browser.__contains__("chr") and not Browser.__contains__("chrome"):
        Browser = (Browser.replace("chr","Chrome"))
    
    if Browser.__contains__("cr") and not Browser.__contains__("chrome"): 
        Browser = (Browser.replace("cr","Chrome"))
        

###Firefox####
    if Browser.__contains__("ff") and not Browser.__contains__("ffox"):
        Browser = (Browser.replace("ff","Firefox"))
       
    if Browser.__contains__("ffox") and not Browser.__contains__("firefox"):   
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
#####################################################################################################################################################    

while True: ##run infinitely until session timeout
    IP = (input("IP address: ?  ").replace(" ",""))
    check(IP)
    Error_type = (input("Error_type ? ").lower())

    if Error_type == "ns" or Error_type == "not seen" or Error_type == "n" or Error_type == "not" or Error_type == "no":
        Printfunc(IP)
        print("\n" + "We can confirm that no traffic is seen on the Imperva portal for the IP provided.")
    
    elif Error_type == "seen" or Error_type.__contains__("allo") or Error_type == "s":
        Printfunc(IP)
        print("\n" + "We can confirm that traffic for the IP provided is seen on the Imperva portal and is allowed.")
	
	##Special Cases, put first because order matters in Python:
       
    elif ("kvinv") in Error_type: ##both 
        
        Browser, Country = GetBrowserAndCountry()
        Geo = input("what is geo?   ").lstrip() ##remove left most spaces
        Geo = CapitaliseEveryFirstLetter(Geo)
        Printfunc(IP)
        print("Browser: " + Browser) ##i could block this into one function if i really wanted to....
        print("Country: "+ Country)
        print("Geo Org: " + Geo  +"\n")
        print("We can confirm the IP provided is currently being blocked due to a VPN or a hosted environment and blocked due to a Javascript or Browser cookie issue.")

    elif ("inv") in Error_type or ("cook") in Error_type or "java" in Error_type or Error_type == "js" or Error_type.__contains__("forc") or Error_type == "fi" or Error_type.__contains__("bloc"):
        Browser, Country = GetBrowserAndCountry()
        Printfunc(IP)
        print("Browser: " + Browser)
        print("Country: "+ Country + "\n")
        print("We can confirm that traffic for the IP provided is currently blocked due to a Javascript or Browser cookie issue.")
    
    elif Error_type.__contains__("kv") or Error_type.__contains__("vp") or Error_type.__contains__("host"):
        Browser, Country = GetBrowserAndCountry()
        Geo = input("what is geo?   ")
	Geo = CapitaliseEveryFirstLetter(Geo)
        Printfunc(IP)
        print("Browser: " + Browser)
        print("Country: "+ Country)
        print("Geo Org: " + Geo  +"\n")
        print("We can confirm the IP provided is currently being blocked due to a VPN or a hosted environment.")
    
    else:
        print("incorrect option \n Options are: \n\n - NS for not seen \n\n - Seen or s or allowed \n\n - inv/cookie/javascript/js \n\n -Kv/vpn/host. Further info please see Github ReadMe https://github.com/jkerai1/ImpTemplate/blob/main/README.md ")
        
    print("\n-------------------------------------------------------------------------------------------------------------------------")    
