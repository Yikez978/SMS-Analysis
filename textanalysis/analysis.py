from textanalysis import readxml
from collections import Counter
import pandas as pd

def get_data():
    """initially get the data"""
    #TODO implement
    path = rb"C:\Users\Ryan\PycharmProjects\TextAnalysis\data\smsbackup\sms-20170429205511.xml"
    tree = readxml.read_xml(path)
    df = readxml.sms_backup_to_df(tree)
    return df

def count_names(dataframe):
    c = Counter(dataframe["contact_name"])
    print(c)


def sample(data):
    writer = pd.ExcelWriter('output.xlsx')
    data = data.head()
    data.to_excel(writer, 'Sheet1')

def export(data):
    data.to_csv(path_or_buf=r"C:\Users\Ryan\PycharmProjects\TextAnalysis\data\output\sms_out.csv",encoding='utf-8')


def main():
    df = get_data()
    print(df.info())
    count_names(df)
    #format = Apr 2, 2016 6:16:18 PM NEVERMIND THIS NEEDS TO BE FIXED
    #see documentation
    df['datetime'] = pd.to_datetime(df['readable_date'], format='%b %d, %Y %-I:%M:%S %p ')
    df['mm/dd/yyyy'] = df['datetime'].apply(lambda x: x.strftime('%m/%d%/%Y'))
    sample(df)
    export(df)

if __name__ == "__main__":
    main()
