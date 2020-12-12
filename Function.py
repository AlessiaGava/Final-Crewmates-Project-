#function that gives you info about a player, given their name (or surname)

def fun_name(df, n):
    name_count=df['Names'].str.contains('n').sum()       #gives you the number of items found
    filtered_df_multiple = df.loc[df["Names"] == "n"]    #gives you a mini df containing filtered data
    if name_count>0:        #if the name is present in the dataset
        if name_count>1:    #if the name belongs to 2 or more players
            print(filtered_df_multiple)
            print("Please, be more specific: choose the player you want")
            break
        else:               #if the name is unique
            print(filtered_df_multiple)
    else:                   #if the name is NOT present in the dataset
        print("We did not find the name. Please, try again.")
