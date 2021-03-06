import os
from types import new_class
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.withdraw()
cwd = os.getcwd()


def domain_name(name):
    """Function that filters for each Domain"""
    domain_list = ["a09","b08","c07","d06","e05","f04","g03","h02","i01","j01"]

    #Dictionary containing the domain name
    domains = {
        "a09" : "a-email.local",
        "b08" : "b-email.local",
        "c07" : "c-email.local",
        "d06" : "d-email.local",
        "e05" : "e-email.local",
        "f04" : "f-email.local",
        "g03" : "g-email.local",
        "h02" : "h-email.local",
        "i01" : "i-email.local",
        "j01" : "j-email.local"
    }

    try:
        del domain_list[name]
        new_domain_list = [ _ for _ in domain_list]

        for key in new_domain_list:
            df.drop(df[df['DomainName'] == domains[key]].index,inplace=True) #Group each Domain
           
        n_rows = str(len(df.axes[0])) # ROWS AFTER grouping each Domain 
        return n_rows      

    except IndexError:
        pass    

def create_csv(n_rows,name):
    """Function that will create new csv for each Domain"""
    domain_list = ["a09","b08","c07","d06","e05","f04","g03","h02","i01","j01"]
    #New Filename
    a = filename.split("_")
    b1 = a.pop(0)
    b2 = domain_list[name]
    b3 = n_rows
    b4 = a.insert(0,b2)
    b5 = a.insert(1,b3)
    c = "_".join(a)
    csv_filename = c

    #Saving the Data Frame into the New CSV file
    csv_data = df.to_csv(csv_filename,index=False,header=True)
    return csv_data
    

def count(x, y):
    for name in range(x, y):
        rows = domain_name(name)
        create_csv(rows,name)
        
  
for filename in os.listdir(cwd):
    if "[Report]" in filename:
        df = pd.read_csv(filename)
        count(0,1)
        del df

        df = pd.read_csv(filename)
        count(1,2)
        del df

        df = pd.read_csv(filename)
        count(2,3)
        del df

        df = pd.read_csv(filename)
        count(3,4)
        del df

        df = pd.read_csv(filename)
        count(4,5)
        del df

        df = pd.read_csv(filename)
        count(5,6)
        del df

        df = pd.read_csv(filename)
        count(6,7)
        del df

        df = pd.read_csv(filename)
        count(7,8)
        del df

        df = pd.read_csv(filename)
        count(8,9)
        del df

        df = pd.read_csv(filename)
        count(9,10)    
        del df 

        


            

        
