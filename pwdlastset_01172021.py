import os
from types import new_class
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.withdraw()
cwd = os.getcwd()


# def create_csv(df,domains,key):
#     """Function that will create new csv file per Domain."""

#     domains.pop(key)
#     df.drop(df[df['DomainName'] == domains[key]].index,inplace=True) #Group each Domain
#     n_rows = str(len(df.axes[0])) # ROWS AFTER grouping each Domain  

#     #Filename 
#     a = filename.split("_")
#     b1 = a.pop(0)
#     b2 = key
#     b3 = n_rows
#     b4 = a.insert(0,b2)
#     b5 = a.insert(1,b3)
#     c = "_".join(a)
#     csv_filename = c

#     #Saving the Data Frame into the New CSV file
#     csv_data = df.to_csv(csv_filename,index=False,header=True)

def domainlist(name):
    DOMAIN_LIST = ["g09","g08","g07","g06","g05","g04","g03","g02","g01","r01"]
    new_domain_list = []
    new_domain_list.append(DOMAIN_LIST)
    del new_domain_list[0][name]
    print (new_domain_list) 
    return new_domain_list
                

def domainname(df):
    """Function to filter out rows not included in the domain."""
    domains = {
        "g09" : "g09.fujitsu.local",
        "g08" : "g08.fujitsu.local",
        "g07" : "g07.fujitsu.local",
        "g06" : "g06.fujitsu.local",
        "g05" : "g05.fujitsu.local",
        "g04" : "g04.fujitsu.local",
        "g03" : "g03.fujitsu.local",
        "g02" : "g02.fujitsu.local",
        "g01" : "g01.fujitsu.local",
        "r01" : "r01.fujitsu.local"
    }

 
    for name in range(10):
        domainlist(name)
        
        
            
for filename in os.listdir(cwd):
    if "[Report]" in filename:
        df = pd.read_csv(filename)
        domainname(df)



        
           
"""  
        df.drop(df[df['DomainName'] == 'Windows 10 Enterprise'].index,inplace=True) #Group each Domain
        n_rows = str(len(df.axes[0])) # ROWS AFTER grouping each Domain    

    #Creating new filename
        a = filename.split("_")
        b1 = a.pop(0)
        b2 = key
        b3 = n_rows
        b4 = a.insert(0,b2)
        b5 = a.insert(1,b3)
        c = "_".join(a)
        csv_filename = c
        print(key)

        #Saving the Filtered Data Frame into the New CSV file
        csv_data = df.to_csv(csv_filename,index=False,header=True)
"""
        
       


        


            

        
