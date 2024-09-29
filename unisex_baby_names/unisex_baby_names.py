import pandas as pd
import matplotlib.pyplot as plt

# dataframe of baby names from every available year
allyears = pd.read_csv('allyears.csv.gz')

# adds all the occurances of names from all years and sorts by sex
totals = allyears.groupby(['sex', 'name']).number.sum()

# sorts by male and female and calculates ratios for each name
male, female = totals.loc['M'], totals.loc['F']
ratios = (totals.loc['M'] / totals.loc['F']).dropna()

# calculates if a name is unisex or not using the ratios
unisex = ratios[(ratios > 0.5) & (ratios < 2)].index

# combines the male list and female list by each unisex name and sorts by occurance
common = (male.loc[unisex] + female.loc[unisex]).sort_values(ascending=False).head(10)

allyears_indexed = allyears.set_index(['sex', 'name', 'year']).sort_index()
plt.figure(figsize=(9,9))

# makes and formats separate plots for each name, showing both male and female occurances
for i, name in enumerate(common.index):
    plt.subplot(5, 2, i+1)

    plt.plot(allyears_indexed.loc['M', name], label='M')
    plt.plot(allyears_indexed.loc['F', name], label = 'F')

    plt.legend()
    plt.title(name)

plt.tight_layout()