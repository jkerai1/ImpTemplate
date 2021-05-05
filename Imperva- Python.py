import re
##import datetime

##Random Test IP: 221.241.59.100
##this file can be run in an online editor such as https://www.online-python.com/

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def check(Ip): ##see if IP is valid using Regex
    if(re.search(regex, Ip)):
        pass ##no need to do anything if IP is valid
    else:
        print("Invalid Ip address")
        quit()
        
def Printfunc(IP):
    print("\n" + "IP: "  + IP)
  
def GetBrowserAndCountry():
    Browser = input("what is browser?   ").lower()
    
    ######################Clean up shorthand############################### probably a better way to do this using regex#############
    if Browser.__contains__("chr") and not Browser.__contains__("chrome"):
        Browser = (Browser.replace("chr","Chrome"))
        
    if Browser.__contains__("chrome"):
        Browser = (Browser.replace("chrome","Chrome"))  # i should probably just use regex to search for "/"
        
    if Browser.__contains__("ff") and not Browser.__contains__("ffox"):
        Browser = (Browser.replace("ff","Firefox"))
       
    if Browser.__contains__("ffox") and not Browser.__contains__("Firefox"):   
        Browser = (Browser.replace("ffox","Firefox"))
       
    if Browser.__contains__("firefox"):   
        Browser = (Browser.replace("firefox","Firefox"))

    if Browser.__contains__("saf") and not Browser.__contains__("safari"):
        Browser = (Browser.replace("saf","Safari"))
        
    if Browser.__contains__("safari"):
        Browser =(Browser.replace("safari","Safari"))
        
    if Browser.__contains__("edg") and not Browser.__contains__("edge"):
        Browser = (Browser.replace("edg", "Edge"))
    
    if Browser.__contains__("edge"):
        Browser = (Browser.replace("edge", "Edge"))
        
    if Browser.__contains__("opera"):
        Browser = (Browser.replace("opera", "Opera"))
        
    Country =input ("what is country?   ").upper()
    
    return (Browser), Country 
#####################################################################################################################################################    
print("Error codes are: ns,seen,inv or kv \n")

    
while True: ##run infinitely until session timeout
    IP = (input("IP address: ?"))
    check(IP)
    Error_type = (input("Error_type ?").lower())

    if Error_type == "ns" or Error_type == "not seen":
        Printfunc(IP)
        print("\n" + "We can confirm that no traffic is seen on the Imperva portal for the IP provided.")
    
    elif Error_type == "seen" or Error_type == "allowed":
        Printfunc(IP)
        print("\n" + "We can confirm that traffic for the IP provided is seen on the Imperva portal and is allowed.")

    elif Error_type.__contains__("inv") or Error_type ==  "cookie" or Error_type == "javascript" or Error_type == "js":
        Browser, Country = GetBrowserAndCountry()
        Printfunc(IP)
        print("Browser: " + Browser)
        print("Country: "+ Country + "\n")
        print("We can confirm that traffic for the IP provided is currently blocked due to a Javascript or Browser cookie issue.")
    
    elif Error_type.__contains__("kv") or Error_type.__contains__("vpn") or Error_type.__contains__("host"):
        Browser, Country = GetBrowserAndCountry()
        Printfunc(IP)
        print("Browser: " + Browser)
        print("Country: "+ Country + "\n")
        print("We can confirm the IP provided is currently being blocked due to a VPN or a hosted environment.")
    
    else:
        print("incorrect option")
        
    print()    
    
    
    ##Note, it is possible to get python to output to a textfile which could make logging much easier...
    
    ##x = datetime.datetime.now()
    #f =open("Imperva" + x + ".txt", "x") #for a new file. if file already exists then to append use
    
    #with open("testfile.txt", "a") as f:
	    #f.write("I'm an additional line.")
    ##check if file exists by
    
    ##from pathlib import Path
        
    #if Path('filename.txt').is_file():
    
#        print ("File exist")
#else:
 #   print ("File not exist")