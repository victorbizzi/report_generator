import matplotlib.pyplot as pl
import seaborn as sb
import pandas


def report_generator():
    data = pandas.read_excel('transactions.xlsx')
    filtered_data = data[data['Status'].isin(['Running', 'Stopped', 'Connection Refused'])]
    g_data = filtered_data.groupby('Status')['Flow'].count().reset_index(name='Count')

    for status in ['Running', 'Stopped', 'Connection Refused']:
        if status not in g_data['Status'].values:
            g_data = pandas.concat([g_data, pandas.DataFrame({'Status': [status], 'Count': [0]})], ignore_index=True)

    g_data['Status'] = pandas.Categorical(g_data['Status'], categories=['Running', 'Stopped', 'Connection Refused'], ordered=False)
    g_data = g_data.sort_values('Status')
    sb.barplot(data=g_data, x='Status', y='Count')
    pl.title('Flows and Status')
    pl.xlabel('Status')
    pl.ylabel('Flows Count')
    pl.grid(True)
    pl.yticks(range(0, g_data['Count'].max() + 1))

    pl.savefig('report.jpeg', format='jpeg')
    pl.show() #This is just to open the "Figure" window. If you don't want to open it, just comment this line because tje brevious line already saved the image as jpeg

report_generator()