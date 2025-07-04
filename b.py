import pandas as pd

#create a simple dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Harsha', 'Tanaya'],
    'Age': [25, 30, 35, 19, 21],
    'City': ['New york', 'Paris', 'London', 'Yavatmal', 'Ladkhed'],
    'College': ['JDIET', 'JCOE', 'GH raisoni', 'Priyadarshani', 'YCC']
}
df = pd.DataFrame(data)

#display the dataframe
print(df)

#access a column
print(df['Name'])

#basic statistics
print(df['Age'].mean()) #average age

#filter rows
print(df[df['Age']>25])