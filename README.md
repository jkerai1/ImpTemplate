# Imp Template Generator 

"Imp -Template v1.1-noFileOutput.py" is just for the online editor i.e. no file output, https://www.online-python.com/


FileOutput Version(s) outputs a text file with all logged events but can't be run in an online editor (because you can't create the file locally). notepad++ recommended for this method as it has silent auto-refresh. (if you want to work that way that is)

.ipynb code also outputs a text file also, this version has nicer readability, checkboxes but can only be run on Jupyter Notebook

AutoCopy version requires pyclip. To install "pip install pyclip" in your python terminal (or anaconda prompt)

![image](https://user-images.githubusercontent.com/55988027/117706200-e8a89200-b1c4-11eb-9756-b29fd47579a0.png)

#  Error Shorthands (case insensitive):

Traffic Not Seen - not seen, ns, n,not,no

Traffic Seen - seen, allo, allowed, allow, s

Traffic blocked due to ForceIdentify OR Invalid-Token - inv, invalid, cook, cookie, java, javascript, js, fi, forc, bloc, tok

KVDC - kv, kvdc, kvd, vp, vpn, host

	Special Cases:
	
	invalid and kvdc - kvinv
	
	force identity and allowed - pfi,partialforce
	
	partial blocked - pb,partialblock 

# Browser Shorthands (not req'd but handy,case insensitive):

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

f.close() - closes file in case u need to delete the .txt


# Jupyter Notebook Users

To paste as plain text is ctrl shift v to Teams if copying straight from Jupyter notebook AND NOT using the AutoCopy Version     <<<

Ctrl + enter is run a block

Shift + L toggles line numbers in jupyter - useful to debugging

Bottom blocks are buttons to take you to a website, set accordingly

![image](https://user-images.githubusercontent.com/55988027/117545508-f5d74c80-b01d-11eb-8e07-e362191f7bb9.png)


# Notepad ++ users
If you want to reload the .txt automatically on notepad++, go to Settings / Preferences, then the MISC tab and check Update silently under File Status Auto-detection.

![image](https://user-images.githubusercontent.com/55988027/117534363-fd303300-afe8-11eb-8b48-6020c4d7437a.png)









# Other  Features:

- Autocapitialization & removal of whitespaces

- Regex to validate IP address

- Punctuation stripping on Country line

# Future Ideas

Check box for websites if users want it, personally i find keyboard faster

# Snow Misc


Enable template toolbar

![image](https://user-images.githubusercontent.com/55988027/117541308-35e10400-b00b-11eb-9c0e-24862d7276c0.png)

Click on the "+" to create a template

![image](https://user-images.githubusercontent.com/55988027/117541325-485b3d80-b00b-11eb-9fe7-522170fde830.png)


Assigning to yourself does not seem to work at the moment.

Fill in company name(s) as apprioprate 

![117541762-50b47800-b00d-11eb-8d5b-b2a8df0a70f5](https://user-images.githubusercontent.com/55988027/117545567-3fc03280-b01e-11eb-9ee2-0fbaa9e24f2e.png)
