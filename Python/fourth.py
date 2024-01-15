import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
tips.head()
sns.kdeplot(data=tips,x="tip")
sns.rugplot(data=tips,x="tip")
plt.show()

