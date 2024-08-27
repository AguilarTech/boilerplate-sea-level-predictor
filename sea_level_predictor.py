import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12,6))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit

    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_level_predicted = intercept + slope * years_extended

    # Plot the line of best fit
    plt.plot(years_extended, sea_level_predicted, color='red', label='Best Fit Line')

    years_extended = np.arange(df['Year'].min(), 2051)
    sea_level_predicted = intercept + slope * years_extended

    plt.plot(years_extended, sea_level_predicted, color='red', label='Best Fit Line')


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended_recent = np.arange(2000, 2051)
    sea_level_predicted_recent = intercept_recent + slope_recent * years_extended_recent

    plt.plot(years_extended_recent, sea_level_predicted_recent, color='green', label='Best Fit Line (2000 Onwards)')
    


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()