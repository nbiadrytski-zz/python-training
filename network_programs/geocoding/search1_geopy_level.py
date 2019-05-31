from geopy.geocoders import Nominatim


if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    user_agent = 'test'

    location = Nominatim(user_agent=user_agent).geocode(address)

    print(location.latitude, location.longitude)