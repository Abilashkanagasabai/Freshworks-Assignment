# Required Libraries
import threading
from threading import*
import time

 #'dic' is the dictionary in which we store data

#for create operation 
#we use syntax "create(key_name,value,timeout_value)" time is optional 
class Data:
    def __init__(self):
        
        self.dic={}

    def create(self,key,value,mytime=0):
        if key in self.dic:
            print("***",key,"already exists","***") 
        else:
            if(key.isalpha()):
                if len(self.dic)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and JSON object value less than 16KB 
                    if mytime==0:
                        l=[value,mytime]
                        print("*** Key created ***")
                    else:
                        l=[value,time.time()+mytime]
                        print("*** Key created ***")

                    if len(key)<=32: #constraints for input key_name capped at 32chars
                        self.dic[key]=l
                else:
                    print("*** Memory limit exceeded!! ***")#error message2
            else:
                print("*** Invalid key_name, key_name must contain only alphabets and no special characters or numbers")

    #for read operation
    #use syntax "read(key_name)"
                
    def read(self,key):
        if key not in self.dic:
            print("*** The ",key,"is not present in database. Please enter a valid key ***") 
        else:
            b=self.dic[key]
            if b[1]!=0:
                if time.time()<b[1]: #comparing the present time with expiry time
                    stri="***"+str(key)+":"+str(b[0]) + " ***"#to return the value in the format of JasonObject i.e.,"key_name:value"
                    return stri
                else:
                    print("** The",key,"has expired ***") 
            else:
                stri="*** "+str(key)+":"+str(b[0])+ " ***"
                return stri
    
    #for delete operation
    #use syntax "delete(key_name)"
    
    def delete(self,key):
        if key not in self.dic:
            print("*** The ",key,"is not present in database. Please enter a valid key ***") 
        else:
            b=self.dic[key]
            if b[1]!=0:
                if time.time()<b[1]: #comparing the current time with expiry time
                    del self.dic[key]
                    print("*** key is successfully deleted ***")
                else:
                    print("** The",key,"has expired ***")  
            else:
                del self.dic[key]
                print("*** key is successfully deleted ***")
    
    #I have an additional operation of modify in order to change the value of key before its expiry time if provided
    
    #for modify operation 
    #use syntax "modify(key_name,new_value)"
    
    def modify(self,key,value):
        b=self.dic[key]
        if b[1]!=0:
            if time.time()<b[1]:
                if key not in self.dic:
                    print("*** The ",key,"is not present in database. Please enter a valid key ***") 
                else:
                    l=[]
                    l.append(value)
                    l.append(b[1])
                    self.dic[key]=l
                    print("*** Value modified ***")
            else:
                print("** The",key,"has expired ***")
        else:
            if key not in self.dic:
                print("*** The ",key,"is not present in database. Please enter a valid key ***") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                self.dic[key]=l
                print("*** Value modified ***")
                
    #I have an additional operation of display all the elements in database irrespective of their expiry time
    
    #for ShowData operation 
    #use syntax "ShowData()"      
                
    def ShowData(self):
        for i in self.dic:
            print("|",i,"------>",self.dic[i][0],"|")
            print("-"*20)
            