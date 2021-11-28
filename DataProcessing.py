import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\julie\Desktop\Cours Berkeley\IA and Health\Project\ProjectPH.csv')

#data = pd.read_csv(r'C:\Users\julie\Desktop\Cours Berkeley\IA and Health\Project\ProjectPH2.csv')
data = data[data['selftext'] != '[effacé]']
data['created'] = pd.to_datetime(data['created'])




indexs = data.index
month_2022 = []
only_month_2022 = []
month = []
days =[]
avg_tot_month =[]
predicted_avg = []

for index in indexs:
        date = str(data['created'][index].year)+"-"+str(data['created'][index].month)
        if (date in month) == False:
            month.append(date)
        date2 = str(data['created'][index].year)+"-"+str(data['created'][index].month )+"-"+str(data['created'][index].day)
        if (date2 in days)==False:
            days.append(date2)
        date_2022 ='2022'+'-'+str(data['created'][index].month)
        only_date_2022 = str(data['created'][index].month)
        if (date_2022 in month_2022) == False:
            month_2022.append(date_2022)
            only_month_2022.append(only_date_2022)

for month_1 in month:
    avg_month = 0
    sum = 0
    count = 0
    for index in indexs:
        date = str(data['created'][index].year) + "-" + str(data['created'][index].month)
        if date == month_1:
            sum = sum + data['sentiment_polarity'][index]
            count = count + 1
    avg_month = sum / count
    avg_tot_month.append(avg_month)

for month_2022_1 in only_month_2022:
    avg_2022 = 0
    sum_2022 = 0
    count_2022 = 0
    for index in indexs:
        date_month = str(data['created'][index].month)
        if date_month == month_2022_1:
            count_2022 = count_2022 + 1
            sum_2022 = sum + data['sentiment_polarity'][index]
    avg_2022 = sum_2022/count_2022
    predicted_avg.append(avg_2022)


print(predicted_avg)


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
plt.title('Average of the sentiment score by month')
plt.show()

days = pd.to_datetime(days)
plt.plot(days,avg_tot_day)
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.title('Average of the sentiment score by days')
plt.show()

plt.hist(data['status'])
plt.title('Distribution of the sentiment')
plt.show()


print(month_2022)
plt.plot(month_2022, predicted_avg)
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.title('Prediction of the average sentiment score for the next year')
plt.show()

