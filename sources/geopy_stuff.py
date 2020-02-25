import geopy.geocoders


geolocator = geopy.geocoders.Nominatim(user_agent='botanich')


def get_latitude_longtitude(location):
    """
    (str) -> (float, float)
    By given location returns latitude and longitude of given location
    """

    tmp = geolocator.geocode(location)
    return tmp.latitude, tmp.longitude
