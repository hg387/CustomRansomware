----------------------------------------------------------------------------------------------------------------------------
REQUIRMENTS
----------------------------------------------------------------------------------------------------------------------------

Python 3.7 or later are required to be installed onto the machine for the malware to run

----------------------------------------------------------------------------------------------------------------------------
BACKGROUND
----------------------------------------------------------------------------------------------------------------------------
The following paragraph is to explain the overall flow of the malware and how it would work in a REAL attack.
This malware would be placed onto the victims machine via a phising email asking for the victim to open a pdf file. This pdf file would actually be our malware masqueraded as a pdf to fool the victim into downloading it and opening it. Upon opening the pdf, our malware will run and encrpyt the victim's files. It will then prompt the user to go to a webpage to pay for the key needed to decrypt their files. This webpage would be hosted on a server that we own and would ask for credit card information. The user will be able to confirm that their files are decryptable via running the malware with command 3, which will decrpyt one file for the victim. Once payment is confirmed, the victim would be given the private key needed to decrpyt their files. The victim would then run the malware with the command 2 to decrpyt their files

----------------------------------------------------------------------------------------------------------------------------
IMPORTANT DETAILS ABOUT OUR MALWARE
--------------------------------------------------------------
In a real attack, we would be hosting the payment webpage on a domain that we own but for this project it is a static page that has the private key hidden in it, only become visible once submit is clicked. The program uses not-so-simple encryption to encrypt all the text files. The private key for decypting the files is encrypted via SHA256 to further ensure that the victim cannot get the private key without paying. Also, even the victim has the encrypted SHA-256 form of the private key, the victim would not able to interpret private key from it as reverting SHA-256 encryption is infeasible. The public key that is generated from the not-so-simple encryption is stored in a .key file which is hidden on linux systems and is stored after converted into bytes. This conversion of bytes also done so that naive victim won't have any idea about what's in the file if he/she found the .key file and opened it. This .key also get cleaned up once decryption of all files is done using command 2. Our encryption cover all numeric alphabets and punctations.

----------------------------------------------------------------------------------------------------------------------------
INSTRUCTIONS
----------------------------------------------------------------------------------------------------------------------------
Command 1 to run program for Encryption:
  python3 Walker.py
  
Command 2 to run program for Decryption:
  python3 Walker.py -d [KEY]
 
 Note: if entered the wrong key, the program is going to again ask the user for key until either 'exit' is entered or correct private key is entered.
 
Command 3 to run program for Decryption of only one file:
  python3 Walker.py --one

Note: Once Decrypted only one file, cut that file otherwise it would get decrypted again when running the program with the Key. 

-----------------------------------------------------------------------------------------------------------------------------
ATTACHED FILES INFO
-----------------------------------------------------------------------------------------------------------------------------
1) Walker.py: the main program which is used to run the malware
2) decrypt.py: the program used to decrypt using not-so-simple subsitution algorithm
3) encrypt.py: the program used to encrypt using not-so-simple subsituttion algorithm
4) webpage.py: the program used to generate the static webpage
5) Group Project: the directory containing various kind of files for testing the malware
