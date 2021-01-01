from OOP import Data
def main():
    Cust=Data()
    while True:
        print("")
        print("""
        ====== Choose any number from below =======
        1. Create a new Key
        2. Read the existing key and  value
        3. Delete an exisiting Key
        4. Modify the data key
        5. Display the existing datastore
        6. Exit
        """)
        choice = input("Enter choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int! enter value between (1-6)")
            continue
        
        if choice == 1:
            
            key=input("Enter the key : ")
            try:
                value=int((input("Enter the value (only integer): ")))
            except ValueError:
                continue
            time1=int(input("Enter 0 for unlimted time or mention time in seconds for expiry : "))
            print("")
            if(time1>0):
                Cust.create(key, value,time1)
            else:
                Cust.create(key,value)
        if choice == 2:
            key1=input("Enter the key want to read : ")
            print("")
            print(Cust.read(key1))
            
        if choice == 3:
            delete=input("Enter the key you want to delete : ")
            Cust.delete(delete)
        if choice == 4:
            mkey=input("Enter the key you want to modify : ")
            try:
                mvalue=int(input("Enter the value for corresponding key(only integer) : "))
            except ValueError:
                continue
            Cust.modify(mkey, mvalue)
        if choice==5:
            Cust.ShowData()
        if choice==6:
            del Cust # Removing the object to save memory
            print(".............Exiting the portal...........")
            break
        else:
            print("Enter the correct choice number ")
if __name__=="__main__":
    main()










# We can use the multithreading using following syntax
# Comment the following code if threading is not done
    

###########################################
    
    
thread1=Thread(target=Cust.create or Cust.read or Cust.delete,args=(key_name,value,mytime))
thread1.start()
thread2=Thread(target=Cust.create or Cust.read or Cust.delete,args=(key_name,value,mytime))
thread2start()
thread1.join()
thread2.join()
print("done")


############################################