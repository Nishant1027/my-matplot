import matplotlib.pyplot as plt
import numpy as np

np_pop=np.array(pop)  #pop is a list of corresponding index of country list's population...

# Double np_pop
np_pop=np_pop*2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp,s=np_pop)


# Specify c is a color list of specifies continent based and alpha is a opacity  inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2,c=col,alpha=0.8)


# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()