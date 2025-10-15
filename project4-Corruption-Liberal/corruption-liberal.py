
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""Upload the data"""

dt = pd.read_excel('/content/LIBERAL.xlsx')

"""Sum of empty space or null data"""

dt.isnull().sum()

"""Filling the data"""

dt = dt.fillna(dt.mode().iloc[0]) # fill the data with mode
print(dt)

dt.describe() # Statistics Summary of the data

"""Question 1b"""

# Calculate indicator sums
indicator_columns = ['v2exbribe_ord', 'v2exembez_ord', 'v2excrptps_ord', 'v2exthftps_ord',
                     'v2lgcrrpt_ord', 'v2jucorrdc_ord', 'v2mecorrpt_ord']  # Removed duplicate 'v2exthftps_ord'

indicator_sums = dt[indicator_columns].sum()
total_sum = indicator_sums.sum()
print("Indicator Sums:")
indicator_sums

# Calculate weights
weights = indicator_sums / total_sum
weights = round(weights, 2)
print("Weights based on the sum of each indicator:")
weights

"""Question 2"""

!pip install pycountry_convert

import plotly.express as px
import pycountry_convert as pc

"""Question 2a"""

# Function to get continent code from country name
def get_continent(country_name):
    try:
        country_code = pc.country_name_to_country_alpha2(country_name, cn_name_format="default")
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        return continent_code
    except KeyError:
        # Handle cases where country name is not found, including 'Zanzibar'
        if country_name == "Zanzibar":
            return "AF"  # Assign Zanzibar to Africa
        return 'Unknown'

# Apply the get_continent function to get the continent information
dt['continent'] = dt['country_name'].apply(get_continent)

# Filter for African countries
africa_countries = dt[dt['continent'] == 'AF'].copy()

columns_to_adjust = ['v2exbribe_ord', 'v2exembez_ord', 'v2excrptps_ord', 'v2exthftps_ord', 'v2lgcrrpt_ord', 'v2jucorrdc_ord', 'v2mecorrpt_ord']

for column in columns_to_adjust:
    africa_countries[column] = africa_countries[column] / 4

# Define the columns to be used for calculating the weighted average
columns_to_average = ['v2exbribe_ord', 'v2exembez_ord', 'v2excrptps_ord', 'v2exthftps_ord', 'v2lgcrrpt_ord', 'v2jucorrdc_ord', 'v2mecorrpt_ord']

# Calculate the weighted average correctly
africa_countries['weighted_average1'] = round(africa_countries[columns_to_average].mean(axis=1),2)
# Drop the 'continent' column
africa_countries = africa_countries.drop(['continent'], axis=1)

print(africa_countries)

africa_countries['country_name'].unique()

africa_countries_2023 = africa_countries[africa_countries['year'] == 2023]

# Now africa_countries_2023 contains only the data for the year 2023
print(africa_countries_2023)

# The choropleth map
fig = px.choropleth(africa_countries_2023,
                    locations="country_name",  # Use country_name for locations
                    locationmode='country names', # Specify the locationmode
                    color="weighted_average1",  # Use the weighted average for color
                    hover_name="country_name",  # Show country name on map
                    color_continuous_scale="Viridis",
                    title="Weighted Average Corruption Indicator by Country (Africa, 2023)",
                    labels={'weighted_average':'Weighted Average Corruption Indicator'}
                   )

fig.update_geos(fitbounds="locations", visible=False) # Fit map to locations and hide the default map
fig.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular'))

fig.show()

""" Question 2 b"""

dt['v2exbribe_ord'] = dt['v2exbribe_ord']/4
dt['v2exbribe_ord'] = dt['v2exbribe_ord'] # 1:> No corruption, 0:> corruption
# Select the data for Zanzibar in the year 2023
selected_data = dt[(dt['country_name'] == 'Zanzibar') & (dt['year'] == 2023)]

# Display the result
selected_data[['country_name', 'year', 'v2exbribe_ord']]

"""Question 2C"""

# Divide specific columns by devide 4 and assign back to the same columns
columns_to_process = ['v2exembez_ord', 'v2excrptps_ord', 'v2exthftps_ord', 'v2lgcrrpt_ord', 'v2jucorrdc_ord', 'v2mecorrpt_ord']

for column in columns_to_process:
    dt[column] = dt[column] / 4
# 1:No corruption, 0: corruption

selected_data = dt[(dt['country_name'] == 'Zanzibar') & (dt['year'] == 2020)]

# Display the result
selected_data[['country_name', 'year', 'v2exbribe_ord','v2exembez_ord','v2excrptps_ord','v2exthftps_ord','v2lgcrrpt_ord','v2jucorrdc_ord','v2mecorrpt_ord']]

"""Question 3"""

# List of countries
countries = ['Zanzibar', 'Tanzania', 'India', 'France', 'United States of America']

# Filter the dataframe to include only the specified countries
filtered_dt = dt[dt['country_name'].isin(countries)].copy()

# Filter the dataframe to include only years between 2001 and 2023
filtered_dt = filtered_dt[(filtered_dt['year'] >= 2001) & (filtered_dt['year'] <= 2023)]

# Display the filtered dataframe
filtered_dt = filtered_dt.drop(['continent'], axis=1)

filtered_dt['sum_indicators'] = filtered_dt['v2exbribe_ord'] + filtered_dt['v2exembez_ord'] + filtered_dt['v2excrptps_ord'] + filtered_dt['v2exthftps_ord'] + filtered_dt['v2lgcrrpt_ord'] + filtered_dt['v2jucorrdc_ord'] + filtered_dt['v2mecorrpt_ord']

# Calculate weight for each row
filtered_dt['weight'] = round(filtered_dt['sum_indicators'] / 7 , 2)

# Display the relevant columns
filtered_dt[['country_name','year', 'sum_indicators', 'weight']]

# Create the line plot
plt.figure(figsize=(12, 6))  # Adjust figure size for better visibility

# Assuming 'filtered_dt' has the 'weight' column
grouped_data = filtered_dt.groupby(['year', 'country_name'])[['weight']].mean().reset_index() # Recalculate grouped_data to include 'weight'

for country in grouped_data['country_name'].unique():
    country_data = grouped_data[grouped_data['country_name'] == country]
    plt.plot(country_data['year'], country_data['weight'], label=country)

plt.xlabel('Year')
plt.ylabel('corruption_indicators')
plt.title('Weights by Year and Country')
plt.xticks(range(2001, 2024))  # Set x-axis ticks to years from 2001 to 2023
plt.legend()
plt.grid(True)
plt.show()

"""Question: 4"""

from sklearn.decomposition import PCA
import plotly.express as px

africa_countries_2023 = africa_countries[africa_countries['year'] == 2023]
indicator = ['v2exbribe_ord', 'v2exembez_ord', 'v2excrptps_ord', 'v2exthftps_ord', 'v2lgcrrpt_ord', 'v2jucorrdc_ord', 'v2mecorrpt_ord']
X = africa_countries_2023[indicator]

pca = PCA(n_components=1)
# Ensure X is a NumPy array
X_array = np.array(X)
# Perform PCA transformation
pca_index = pca.fit_transform(X_array)
# Normalize PCA index to range [0, 1]
pca_index_normalized = (pca_index - np.min(pca_index)) / (np.max(pca_index) - np.min(pca_index))

africa_countries_2023 = africa_countries_2023.copy()
# Assign the normalized PCA index to the dataframe
africa_countries_2023.loc[:, 'pca_index'] = pca_index_normalized.flatten()

fig = px.scatter(africa_countries_2023, x = 'weighted_average1', y = 'pca_index', hover_name = 'country_name', trendline = "ols", title = 'Comparison of Indices for African Countries(Weight vs PCA)')
fig.show()

# Round the 'pca_index'
africa_countries_2023.loc[:, 'pca_index'] = africa_countries_2023['pca_index'].round(2)
africa = africa_countries_2023[['country_name', 'weighted_average1', 'pca_index']].copy()
print(africa)

# Calculation of correlation coefficient between PCA index and Weight Average
y = africa_countries_2023['pca_index']
x = africa_countries_2023['weighted_average1']
correlation_coefficient = np.corrcoef(x, y)[0, 1]
correlation_coefficient
