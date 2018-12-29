import pandas

df1 = pandas.read_json("http://pythonhow.com/supermarkets.json")

df1 = df1.set_index("Address")

print(df1)
#                          City        ...                    State
# Address                               ...
# 3666 21st St     San Francisco        ...                 CA 94114
# 735 Dolores St   San Francisco        ...                 CA 94119
# 332 Hill St      San Francisco        ...         California 94114
# 3995 23rd St     San Francisco        ...                 CA 94114
# 1056 Sanchez St  San Francisco        ...               California
# 551 Alvarado St  San Francisco        ...                 CA 94114
print("----------------------------------------------------------------------------")

print(df1.loc["332 Hill St": "3995 23rd St", "Country": "ID"])
#             Country  Employees  ID
# Address
# 332 Hill St      USA         25   3
# 3995 23rd St     USA         10   4
print("----------------------------------------------------------------------------")

# for index "332 Hill St" get ID
print(df1.loc["332 Hill St", "ID"])
print("----------------------------------------------------------------------------")

# for all indexes get Country
print(df1.loc[:,"Country"])
# Address
# 3666 21st St       USA
# 735 Dolores St     USA
# 332 Hill St        USA
# 3995 23rd St       USA
# 1056 Sanchez St    USA
# 551 Alvarado St    USA
print("----------------------------------------------------------------------------")

# for indexes get 735 Dolores St and 332 Hill St
# for columns get Country and Employees
print(df1.iloc[1:3, 1:3])
#                Country  Employees
# Address
# 735 Dolores St     USA         15
# 332 Hill St        USA         25
print("----------------------------------------------------------------------------")

# get the value from column Name for index(or row) 3
print(df1.ix[3, "Name"])
# Ben's Shop
print("----------------------------------------------------------------------------")

# delete index 735 Dolores St
print(df1.drop("735 Dolores St", 0))
print("----------------------------------------------------------------------------")

# delete first 3 rows based on index
print(df1.drop(df1.index[0:3], 0))
print("----------------------------------------------------------------------------")

# delete first 3 columns based on index
print(df1.drop(df1.columns[0:3], 1))
print("----------------------------------------------------------------------------")

# add column Continent
# get number of rows by shape[0]
# and multiply by 5
df1["Continent"]=df1.shape[0]*["North America"]
print(df1)
#                          City      ...            Continent
# Address                             ...
# 3666 21st St     San Francisco      ...        North America
# 735 Dolores St   San Francisco      ...        North America
# 332 Hill St      San Francisco      ...        North America
# 3995 23rd St     San Francisco      ...        North America
# 1056 Sanchez St  San Francisco      ...        North America
# 551 Alvarado St  San Francisco      ...        North America
print("----------------------------------------------------------------------------")

# update Continent column
# by adding country from Country column
df1["Continent"]=df1["Country"] + ", " + "North America"
print(df1)
#                          City         ...                   Continent
# Address                                ...
# 3666 21st St     San Francisco         ...          USA, North America
# 735 Dolores St   San Francisco         ...          USA, North America
# 332 Hill St      San Francisco         ...          USA, North America
# 3995 23rd St     San Francisco         ...          USA, North America
# 1056 Sanchez St  San Francisco         ...          USA, North America
# 551 Alvarado St  San Francisco         ...          USA, North America
print("----------------------------------------------------------------------------")

# 1. TO INSERT A ROW
# rows are now columns
df1_rows_now_columns = df1.T
print(df1_rows_now_columns)
# Address          3666 21st St         ...             551 Alvarado St
# City            San Francisco         ...               San Francisco
# Country                   USA         ...                         USA
# Employees                   8         ...                          20
# ID                          1         ...                           6
# Name                  Madeira         ...                  Richvalley
# State                CA 94114         ...                    CA 94114
# Continent  USA, North America         ...          USA, North America
print("----------------------------------------------------------------------------")

# 2. TO INSERT A ROW
# adding a new row which is actually a column
df1_rows_now_columns["My Address"]=["My City", "My Country", 10, 222, "Gippo", "My State", "Europe"]
print("----------------------------------------------------------------------------")

# 3. TO INSERT A ROW
# rows are now rows and columns are columns back
df1 = df1_rows_now_columns.T
print(df1)
#                          City         ...                   Continent
# Address                                ...
# 3666 21st St     San Francisco         ...          USA, North America
# 735 Dolores St   San Francisco         ...          USA, North America
# 332 Hill St      San Francisco         ...          USA, North America
# 3995 23rd St     San Francisco         ...          USA, North America
# 1056 Sanchez St  San Francisco         ...          USA, North America
# 551 Alvarado St  San Francisco         ...          USA, North America
# My Address             My City         ...                      Europe
