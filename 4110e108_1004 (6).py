# -*- coding: utf-8 -*-
"""4110E108_1004

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z-ihnulaX-bamSOa7sp4Ze_BdIizk6_Q
"""

print("4111001671")
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())