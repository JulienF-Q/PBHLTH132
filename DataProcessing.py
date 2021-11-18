import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\julie\Desktop\Cours Berkeley\IA and Health\Project\ProjectPH.csv')

data = data[data['selftext'] != '[effacé]']
data['created'] = pd.to_datetime(data['created'])

indexs = data.index
month = []
days =[]
avg_tot_month =[]
for index in indexs:
        date = str(data['created'][index].year)+"-"+str(data['created'][index].month)
        if (date in month) == False:
            month.append(date)
        date2 = str(data['created'][index].year)+"-"+str(data['created'][index].month )+"-"+str(data['created'][index].day)
        if(date2 in days)==False:
            days.append(date2)

print(days)

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
    avg_tot_month.append(avg_month)


avg_tot_day =[]
for day_1 in days:
    avg_days = 0
    sum = 0
    count = 0
    for index in indexs:
        date = str(data['created'][index].year) + "-" + str(data['created'][index].month) +"-"+str(data['created'][index].day)
        if (date == day_1):
            sum = sum + data['sentiment_polarity'][index]
            count = count + 1
    avg_days = sum / count
    avg_tot_day.append(avg_days)

month = pd.to_datetime(month)
plt.plot(month,avg_tot_month)
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.show()

days = pd.to_datetime(days)
plt.plot(days,avg_tot_day)
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.show()