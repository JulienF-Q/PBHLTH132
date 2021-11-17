import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\julie\Desktop\Cours Berkeley\IA and Health\Project\ProjectPH.csv')

data = data[data['sentiment_polarity'] != 0]
data['created'] = pd.to_datetime(data['created'])

indexs = data.index
month = []
avg =[]
for index in indexs:
        date = str(data['created'][index].year)+"-"+str(data['created'][index].month)
        if (date in month) == False:
            month.append(date)

for month_1 in month:
    avg_month = 0
    sum = 0
    count = 0
    for index in indexs:
        date = str(data['created'][index].year) + "-" + str(data['created'][index].month)
        if (date == month_1):
            sum = sum + data['sentiment_polarity'][index]
            count = count + 1
    avg_month = sum / count
    avg.append(avg_month)



month = pd.to_datetime(month)
plt.plot(month,avg)
plt.show()

#plt.plot('created', 'sentiment_polarity', data=data)
#plt.show()


#Ideas :
# Display, for each month the average value of the polarity for this given month
