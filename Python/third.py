import matplotlib.pyplot as plt
import seaborn as sns

x=['sun','mon','fri','tues','wed']

y=[5,6.3,4,9,2]

ax=sns.stripplot(x)
ay=sns.stripplot(y)

ax.set(xlabel ='Days', ylabel ='amount_spend')

plt.title('my first graph')

plt.show()