import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./stroopdata.csv")


#Statatistics

print(data.describe())


#Plots

sns.set(color_codes=True)
sns.distplot(data["Congruent"], bins=10, kde=False, label="Congruent")
sns.distplot(data["Incongruent"], bins=10, kde=False, label="Incongruent")
plt.xlabel("List time", fontdict=None, labelpad=None)
plt.ylabel("# of people", fontdict=None, labelpad=None)
plt.legend(loc='upper right')
plt.title("List time histogram", fontdict=None, loc='center', pad=None)
plt.show()

sns.distplot(data["Difference"], bins=10, kde=False, label="Difference")
plt.xlabel("List time difference", fontdict=None, labelpad=None)
plt.ylabel("# of people", fontdict=None, labelpad=None)
plt.legend(loc='upper right')
plt.title("List time difference histogram", fontdict=None, loc='center', pad=None)
plt.show()

sns.jointplot(x="Congruent", y="Incongruent", data=data, kind="kde")
plt.show()