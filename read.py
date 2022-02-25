'''
to store data permanently, weneed to create a file.

opening a file:
===================

open('filename','mode')

This function returns reference or file pointer of the file that 
exists or is created.

mode:
========
r-read mode: open file for reading only(no writing).
w-open file for writing(no reading)
a-open file in append mode for writing(no reading)
r+-read and write 
w+-write and read 
a+- append(write) and read 
rb
wb 
ab

'''
try:
    fp=open("student.txt",'r')
    print(fp)
    print("file opened")
    
except FileNotFoundError:

   print("please create a file")    
   
finally:

    fp.close()  #close the file   

