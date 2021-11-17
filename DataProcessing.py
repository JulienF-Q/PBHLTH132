import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\julie\Desktop\Cours Berkeley\IA and Health\Project\ProjectPH.csv')
data = data[data['sentiment_polarity'] != 0]
data['created'] = pd.to_datetime(data['created'])

plt.plot('created', 'sentiment_polarity', data=data)
plt.show()


#Ideas :
# Display, for each month the average value of the polarity for this given month
#