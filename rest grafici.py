import seaborn as sns
import matplotlib.pyplot as plt

# carica dataset di esempio
tips = sns.load_dataset("tips")

# crea un grafico a dispersione
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
plt.show()
