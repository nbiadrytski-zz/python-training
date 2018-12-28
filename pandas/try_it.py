import pandas

list1 = [1, 2, 3]
list2 = [4, 5, 6]
column_name = ["Price", "Age", "Value"]
row_name = ["First", "Second"]

person1 = {"Name": "Nick", "Surname": "Biadrytski"}
person2 = {"Name": "Jimmy", "Surname": "Toledo"}

df1 = pandas.DataFrame([list1, list2], columns=column_name, index=row_name)

df2 = pandas.DataFrame([person1, person2])

print(df1)
print("############################")
print(df2)
print("############################")
print("Average value of df1:\n", df1.mean())
print("############################")
print("df1 Prices:\n", df1.Price)
