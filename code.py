# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head(10))
# Summer or Winter
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data.loc[data['Total_Summer']==data['Total_Winter'], 'Better_Event'] = 'Both'
better_event=data['Better_Event'].value_counts(ascending=False).index[0]
# Top 10
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(146,axis=0,inplace=True)
def top_ten(df,col):
    country_list=list(df.nlargest(10,col)['Country_Name'])
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=list(set(top_10_summer).intersection(set(top_10_winter)).intersection(set(top_10)))
# Plotting top 10
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,figsize=(20,20))
summer_df.plot.bar('Country_Name','Total_Summer',ax=ax1)
winter_df.plot.bar('Country_Name','Total_Winter',ax=ax2)
top_df.plot.bar('Country_Name','Total_Medals',ax=ax3)
# Top Performing Countries
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'].values[0]
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'].values[0]
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'].values[0]
# Best in the world 
data_1=data.drop(146,axis=0)
data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
most_points=data_1['Total_Points'].max()
best_country=data_1[data_1['Total_Points']==most_points]['Country_Name'].values[0]
# Plotting the best
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True,ax=ax4)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


