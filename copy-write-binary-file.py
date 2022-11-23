# COPYING FILES - A SIMPLE AND FUNCTIONAL TOOL
from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536) #prepares a memory for data transfer 4rm src to dest.(such memory is usually known as buffer)
total  = 0 # counts d bytes copied
try:
    readin = src.readinto(buffer)#first attemp to store in buffer
    while readin > 0:#stop only if 0 bytes is returned
        written = dst.write(buffer[:readin])#write d buffer content to d output file using slice to limit d no of bytes
        total += written
        readin = src.readinto(buffer)#read d next file chunk
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()