import pandas as pd
pd.options.mode.chained_assignment = None
path=r"main.csv"
data=pd.read_csv(path)
newdata=data.loc[data['COUNTRY'].str.contains('USA')]
newdata.to_csv(r'output\filteredCountry.csv',index=False);
new_data = newdata[['SKU','PRICE']]

def change(x):
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', '').replace('?', ''))
    return(x)

new_data['PRICE'] = new_data['PRICE'].apply(change).astype('float')
new_data.to_csv(r'interm\intermediate_f_c.csv',index=False)

first_and_second_min_prices = pd.read_csv(r"interm\intermediate_f_c.csv")
temp_data = first_and_second_min_prices.sort_values(['SKU','PRICE']).groupby('SKU').nth(1)
temp_data['FIRST_MINIMUM_PRICE'] = first_and_second_min_prices.sort_values(['SKU','PRICE']).groupby('SKU').min()
temp_data['SECOND_MINIMUM_PRICE'] = first_and_second_min_prices.sort_values(['SKU','PRICE']).groupby('SKU').nth(1)

temp_data.to_csv(r'interm\intermediate_p.csv',index_label="SKU")
df = pd.read_csv(r"interm\intermediate_p.csv")
final_data_frame = df.drop(labels='PRICE',axis='columns')
final_data_frame.to_csv(r'output\lowestPrice.csv',index=False)
