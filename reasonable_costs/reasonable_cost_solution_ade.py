import os

import pandas as pd

os.system('clear')


def remove_currency(cost):
    return float(str(cost)[1:])

def add_currency(cost,currency='$'):
    return f'{currency}{cost:.2f}'

def filter_data_file(data_file):
    read_file_df = pd.read_csv(data_file, delim_whitespace=True,header=0) 
    read_file_df = read_file_df[read_file_df['Recommended'] == 'Yes' ] 
    read_file_df['Cost'] = read_file_df['Cost'].apply(remove_currency)
    read_file_df = read_file_df[(read_file_df['Cost'] > 20) & (read_file_df['Cost'] < 50)]
    read_file_df['Date'] = pd.to_datetime(read_file_df['Date'],format = '%m/%d/%y')
    read_file_df = read_file_df.sort_values(by='Date', ascending=False)
    read_file_df['Cost'] = read_file_df['Cost'].apply(add_currency)
    read_file_df.index += 2
    return read_file_df


def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    print(filter_data_file(f'{directory}/file'))

if __name__ == "__main__":
    main()



















# read_file_df['Cost'] = read_file_df['Cost'].map(lambda x: x.lstrip('$').strip()) 
# ^ strip off currency,need to add it back
# read_file_df['Cost'] = pd.to_numeric(read_file_df['Cost'], errors='coerce') 
# ^ errors=raise will return ValueError
# read_file_df.fillna('')
# read_file_df['Cost'].apply(pd.to_numeric)   
# ^ need to check docs, somehow not working, is it converting only to int???
# read_file_df['Cost'] = read_file_df['Cost'].astype(float).astype(int)  
# ^ Another working way to convert a column, must convert to float before int
# read_file_df.info()  #Get info on dataframe
# read_file_df = read_file_df.reset_index(drop=True)
# ^ allows you to reset the index starting from 0
# read_file_df.to_string(index=False)
# ^ allows you to remove the index 


# def remove_currency(cost):
#     try:
#         return float(cost)
#     except ValueError:
#         if not cost[0].isdigit():
#             return float(str(cost)[1:])
#         elif not cost[-1].isdigit():
#             return float(str(cost)[:-1])