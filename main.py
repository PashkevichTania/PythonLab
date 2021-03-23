import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker


# c1 = input('country1').capitalize()
# if len(c1) == 2: c1 = c1.upper()
# c2 = input('country2').capitalize()
# if len(c2) == 2: c2 = c2.upper()
# c3 = input('country3').capitalize()
# if len(c3) == 2: c3 = c3.upper()
# c4 = input('country4').capitalize()
# if len(c4) == 2: c4 = c4.upper()
c1 ='Russia'
c2 ='US'
c3 ='German'
c4 ='France'

# https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv
df = pd.read_csv('https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv')
countries = [c1, c2, c3, c4]
df = df[df['Country/Region'].isin(countries)]


df = df.pivot(index='Date', columns='Country/Region', values='Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries

populations = {'Canada': 37664517, 'Germany': 83721496 , 'United Kingdom': 67802690 , 'Afghanistan': 37466414,
               'Japan': 126500000, 'US': 330548815, 'France': 65239883, 'China': 1438027228, 'Russia': 146877088,
               'Ukraine': 41688482, 'Belarus': 9450000}

num = covid.copy()
for country in list(num.columns):
    num[country] = num[country]/populations[country] * 100000

colors = {c1: '#045275', c2: '#089099', c3: '#7CCBA2', c4: '#FCDE9C'}
plt.style.use('fivethirtyeight')

plot = covid.plot(figsize=(18,9), color=list(colors.values()), linewidth=7, legend=False)
plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('Num of Cases')

for country in list(colors.keys()):
    plot.text(x = covid.index[-1], y = covid[country].max(), color = colors[country], s = country, weight = 'bold')
    print(covid[country].max())

plt.show()