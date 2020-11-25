----------------------------------------------------------------------------------------------------------------------------
REQUIRMENTS
----------------------------------------------------------------------------------------------------------------------------

Python 3.7 or later are required to be installed onto the machine for the malware to run

----------------------------------------------------------------------------------------------------------------------------
BACKGROUND
----------------------------------------------------------------------------------------------------------------------------
The following paragraph is to explain the overall flow of the malware and how it would work in a REAL attack.
This malware would be placed onto the victims machine via a phising email asking for the victim to open a pdf file. This pdf file would actually be our malware masqueraded as a pdf to fool the victim into downloading it and opening it. Upon opening the pdf, our malware will run and encrpyt the victim's files. It will then prompt the user to go to a webpage to pay for the key needed to decrypt their files. This webpage would be hosted on a server that we own and would ask for credit card information. The user will be able to confirm that their files are decryptable via running the malware with the [INSERT COMMAND], which will decrpyt one file for the victim. Once payment is confirmed, the victim would be given the private key needed to decrpyt their files. The victim would then run the malware with the {INSERT COMMAND] to decrpyt their files

----------------------------------------------------------------------------------------------------------------------------
IMPORTANT DETAILS ABOUT OUR MALWARE
--------------------------------------------------------------
In a real attack, we would be hosting the payment webpage on a domain that we own but for this project it is a static page that has the private key in it. The program uses not-so-simple encryption to encrypt all the text files. The private key for decypting the files is encrypted via SHA256 to further ensure that the victim cannot get the private key without paying. The public key that is generated from the not-so-simple encryption is stored in a .key file which is hidden on linux systems and is converted into bytes. Our encryption does not encrypt '/n' or EOF, but will cover all numeric alphabets.

----------------------------------------------------------------------------------------------------------------------------
INSTRUCTIONS
----------------------------------------------------------------------------------------------------------------------------

