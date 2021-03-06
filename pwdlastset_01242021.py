import os
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
    mydomains = {
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

        for key in domain_list:
            df.drop(df[df['DomainName'] == mydomains[key]].index,inplace=True) #Group each Domain
                        
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
    csv_data = df.to_csv(csv_filename,index=False,header=True,encoding='utf-8-sig')
    return csv_data

  
if __name__ == "__main__":
    
    for filename in os.listdir(cwd):
        if "[Report]" in filename:
            x = 0
            y = 1
            while y != 11:
                df = pd.read_csv(filename)
                for name in range(x, y):
                    rows = domain_name(name) 
                    create_csv(rows,name)
                del df
                x += 1
                y += 1

    messagebox.showinfo("INFO","Finished Processing")


        
               
           
