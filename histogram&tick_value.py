import matplotlib.pyplot as plt
#life_exp and lilfe_exp1950 is a list..
# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# Histogram of life_exp, 15 bins
plt.hist(life_exp,15)

# Show and clear plot
plt.show()
plt.clf()   #.clf is used for clear the screen for further use..

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950,15)


#changing the x-axis/y-axis representation as 1000 written as 1k


# Definition of tick_val and tick_lab
tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)  #its represent on x-axis the tick-lab list is used instead of their corresponding tick_val......

# Show and clear plot again
plt.show()
plt.clf()
