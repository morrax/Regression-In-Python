import csv
import matplotlib.pyplot as plt
from scipy import stats

# Get values from example dataset
with open('example_data.csv', 'r') as file:
    read = csv.DictReader(file)
    x = []
    y = []

    for row in read:
        if row['Country'] == 'Indonesia':
            x.append(int(row['Year']))
            y.append(float(row['Life expectancy ']))

# Get key values for linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Print the coefficient of correlation between values
print('r =', r)

# Function to determine where on the y-axis the corresponding x value will be placed
def func(x):
    return slope * x + intercept

# Run each value of x through the function
model  = list(map(func, x))

# Draw scatter plot
plt.scatter(x, y)
# Draw the line of linear regression
plt.plot(x, model)

# Save plot as image
plt.savefig('linear_regression.png')
