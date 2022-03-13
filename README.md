[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jkerai1/ImpTemplate/HEAD)
# Imp Template Generator 

"Imp -Template v1.1-noFileOutput.py" is just for the online editor i.e. no file output, https://www.online-python.com/


FileOutput Version(s) outputs a text file with all logged events but can't be run in an online editor (because you can't create the file locally). notepad++ recommended for this method as it has silent auto-refresh. (if you want to work that way that is)

.ipynb code also outputs a text file also, this version has nicer readability, checkboxes but can only be run on Jupyter Notebook

AutoCopy version requires pyclip. To install "pip install pyclip" in your python terminal (or anaconda prompt) MS teams version requires pymsteams which can be installed using "pip install pymsteams" in the same manner

GUI version and MSTeams version function identically, with the exception of the MS webhook.

![image](https://user-images.githubusercontent.com/55988027/117706200-e8a89200-b1c4-11eb-9756-b29fd47579a0.png)

#  Error Shorthands (case insensitive) For Non-GUI users:

Traffic Not Seen - not seen, ns, n,not,no

Traffic Seen - seen, allo, allowed, allow, s

Traffic blocked due to ForceIdentify OR Invalid-Token - inv, invalid, cook, cookie, java, javascript, js, fi, forc, bloc, tok

KVDC - kv, kvdc, kvd, vp, vpn, host

	Special Cases:
	
	invalid and kvdc - kvinv
	
	force identity and allowed - pfi,partialforce
	
	partial blocked - pb,partialblock 

# Browser Shorthands (not req'd but handy,case insensitive) Non GUI users:

Chrome - chr,cr,chro,chrom

firefox - ff, ffox

safari - saf,safa,safar

edge - edg

opera - op

yandex - yan, ya

F1 app - f1


# AutoCopy

In this version, the code copies the last investigation to your clipboard automatically as plain text thus you don't need to remember to put Ctrl + shift +V to paste into teams. In this version you will have to paste after every investigation as only one entry can be stored in the clipboard

# Useful Notes:
		
Program is easiest to use in Juypter notebook. Jupyter also lets you open .txt as well if you want that functionality

ctrl + c interrupts python terminal but ctrl shift c (copying as raw text) does not (does not apply to jupyter notebook but does for the Jupyter Terminal)

f.close() - closes file in case u need to edit the .txt


# Jupyter Notebook Users

To paste as plain text is ctrl shift v to Teams if copying straight from Jupyter notebook AND NOT using the AutoCopy Version     <<<

Ctrl + enter is run a block

Shift + L toggles line numbers in jupyter - useful for debugging


# Notepad ++ users
If you want to reload the .txt automatically on notepad++, go to Settings / Preferences, then the MISC tab and check Update silently under File Status Auto-detection.

![image](https://user-images.githubusercontent.com/55988027/117534363-fd303300-afe8-11eb-8b48-6020c4d7437a.png)









# Other  Features:

- Autocapitialization & removal of whitespaces

- Regex to validate IP address (pending on GUI version)

- Punctuation stripping on Country line


# Snow Misc


Enable template toolbar

![image](https://user-images.githubusercontent.com/55988027/117541308-35e10400-b00b-11eb-9c0e-24862d7276c0.png)

Click on the "+" to create a template

![image](https://user-images.githubusercontent.com/55988027/117541325-485b3d80-b00b-11eb-9fe7-522170fde830.png)


Assigning to yourself does not seem to work at the moment.

Fill in company name(s) as apprioprate 

![117545567-3fc03280-b01e-11eb-9ee2-0fbaa9e24f2e](https://user-images.githubusercontent.com/55988027/118389566-6dab0580-b622-11eb-9c23-ef9e9aa30d92.png)
