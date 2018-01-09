from urllib.parse import urlencode
import urllib.request
import simplejson
from shapely.geometry import Point, Polygon


def within(la1, lo1, la2, lo2, x, y):
    pt = Point(x, y)
    mid1 = (la1+la2)/2
    mid2 = (lo1+lo2)/2
    poly = Polygon([(la1, lo1), (la2, lo2), (la1, lo2),(la2, lo1)])
    return poly.contains(pt)


googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'


def get_coordinates(query, from_sensor=False):
    query = query.encode('utf-8')
    params = {
        'address': query,
        'sensor': "true" if from_sensor else "false"
    }
    url = googleGeocodeUrl + urlencode(params)
    json_response = urllib.request.urlopen(url)
    response = simplejson.loads(json_response.read())
    if response['results']:
        location = response['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
    else:
        latitude, longitude = None, None
    return latitude, longitude

