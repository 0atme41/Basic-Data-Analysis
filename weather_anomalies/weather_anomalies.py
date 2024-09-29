import math
import collections
import urllib.request

import numpy as np
import matplotlib.pyplot as pp

import getweather

# fills missing values in the data set
def fillnans(array):
    nanValues = ~np.isnan(array)
    xnew = np.arange(365)
    return np.interp(xnew, xnew[nanValues], array[nanValues])

def findAvgTemp(year):
    return (np.mean(allyears['TMIN'][year - availableYears[0]]) + np.mean(allyears['TMAX'][year - availableYears[0]])) / 2

def smooth(array, window):
    return np.correlate(array, np.ones(window)/window, "same")

station = "SEATTLE"
availableYears = np.arange(1894, 1998)

# processes data set into 2D array of tuples
allyears = np.vstack([getweather.getyear('SEATTLE', ['TMIN', 'TMAX'], year) for year in availableYears]) 

# cleans data
for year in allyears:
    # fills missing values in the data set
    year['TMIN'], year['TMAX'] = fillnans(year['TMIN']), fillnans(year['TMAX'])

    # smooths the data, allowing more subtle trends to be visible
    year['TMIN'], year['TMAX'] = smooth(year['TMIN'], 10), smooth(year['TMAX'], 10) 

# calculates the mid century averge temperatur
midCenAvg = np.mean([findAvgTemp(year) for year in range(1945, 1956)])

# calculates the temperature anomaly per year
anomalies = np.array([findAvgTemp(year) - midCenAvg for year in availableYears])

# plots information
pp.plot(availableYears, smooth(anomalies, 5))
pp.xlabel("Year")
pp.ylabel("Temperature Anomaly")