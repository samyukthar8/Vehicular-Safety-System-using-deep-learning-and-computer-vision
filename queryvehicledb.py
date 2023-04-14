import pandas as pd
import os
df = pd.read_csv(r"C:\Users\home\Documents\python\vehicledb.csv")

accdate=input("Enter date of accident in YYYY-MM-DD format")

acctime=input("Enter time of accident in 24h-min format")

accspec=accdate+'_'+acctime


data_file = fr"C:\Users\home\Documents\python\data\footage_{accspec}.csv"
#print(output_dir)
     
if not os.path.isfile(data_file):
    df1 = pd.DataFrame(columns=['No_plate', 'Owner_name','Insurance_policy_vendor','Policy_No','RTO_Location'])
    df1.to_csv(data_file,index=False)
    
else:
    df1 = pd.read_csv(data_file)
    
    

# Initialize the flag variable
continue_loop = True

while continue_loop:
    # Get user input for the license plate to search for
    license_plate = input("Enter a license plate number: ")

    # Query the dataframe to find the row with the matching license plate number
    result = df[df['No_plate'] == license_plate]

    # Print the result
    print(result)
    save=input("Do you want to save the details of this vehicle?y/n")
    if save=='y':
        df1=df1.append(result,ignore_index=True)
        df1.to_csv(data_file,index=False)
        print(df1)
    elif save=='n':
        cont=input("Do you want to continue the search?y/n")
        if cont=='y':
            continue
        elif cont=='n':
            break
        else:
            print("Enter valid character")
    else:
        break
    




