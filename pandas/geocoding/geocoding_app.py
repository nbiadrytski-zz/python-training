from geopy.geocoders import ArcGIS
import pandas

# create ArcGIS object
nom = ArcGIS()

df = pandas.read_csv("http://pythonhow.com/supermarkets.csv")

# update Address column
# to include City, State, Country columns
df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

# add Coordinates column based on Address column
# and geocode the values
df["Coordinates"] = df["Address"].apply(nom.geocode)

# add Latitude and Longitude columns based on Coordinates column
# and aply latitude and longitude methods in corresponding column for each row using lambda
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x is not None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x is not None else None)

df.to_excel("output.xlsx")
