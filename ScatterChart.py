import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
data['date'] = pd.to_datetime(data['date'])
data.sort_values('date', inplace=True)

cases = data['cases']
date_x = data['date']
deaths_y = data['deaths']
ratio = data['ratio']

plt.scatter(date_x, deaths_y, c=ratio, cmap='summer',
            edgecolor='black', linewidth=1,alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Percent Died')

plt.title('Percent Of Reported Cases Died (USA)')
plt.ylabel('Deaths')

plt.tight_layout()

plt.show()

# Creating "ratio" in csv file
# 
# df = pd.DataFrame(data)
# 
# df['ratio'] = (deaths_y/cases) * 100
#
# df.to_csv('percentCSV.csv')