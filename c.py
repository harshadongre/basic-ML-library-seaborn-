import seaborn as sns #for data visualization
import pandas as pd
import matplotlib.pyplot as plt

#sample dataframe
df = pd.DataFrame({'branch':['EE','CSE','EE','CSE','ENTC','MECH','TEXTILE', 'ENTC','MECH','TEXTILE'],
                   'Score': [85, 90, 78,38,79, 88, 55, 67, 82, 74]})    

#plot a boxplot
sns.boxplot(x='branch', y='Score', data=df)
plt.show()                 