 
# import urllib
import urllib.request, urllib.parse, urllib.error

# import json
import json

# import ssl to ignore certifications
import ssl

# this is the base url for service url
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# indefinite loop, true means this will run only until until it breaks
while True:

    # you will write the location of the address
    address = input('Enter location: ')
    # example you hit Ann Arbor, MI

    # if i hit enter , it will get out of the loop
    if len(address) < 1: break

    # creates an empty dictionary
    parms = dict()

    # add a key inside address with a value of address
    parms['address'] = address

    # if api_key is not false the parms key will have a value of api_key
    if api_key is not False: parms['key'] = api_key

    # concatenate base url and encoded parsed parms dictionary
    # will get serviceurl
    # will transform this urllib.parse.urlencode({'address': address})
    # into address=Ann+Arbor%C+MI
    # concatenate into
    # https://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%C+MI
    url = serviceurl + urllib.parse.urlencode(parms)

    # print Retrieving the url
    print('Retrieving', url)

    # file handler for the url, with ctx ignoring ssl errors
    uh = urllib.request.urlopen(url, context=ctx)

    # read and decode from string to utf-8
    # pull all the entire doc {}[] , then decode utf8 to string
    data = uh.read().decode()

    # print retrieved with length of the data
    print('Retrieved', len(data), 'characters')

    # try this first, if it blows up then run except
    try:

        # json.load string from DATA and return a dictionary
        js = json.loads(data)

    except:

        # or elseit will have a value of js = None
        js = None

    # filter if JS is false, if status key is not in the js dictionary or status key is not equal to OK value
    # if not js = if we got nothing
    # status not in js = if status not in dictionary
    # status != OK = if status is not equal to okay
    if not js or 'status' not in js or js['status'] != 'OK':
        # print failed
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # this will pretty print it with indent of 4
    # this will look like how you see a json file
    print(json.dumps(js, indent=4))


    # this will pretty print it with indent of 4
    # this will look like how you see a json file
    print(json.dumps(js, indent=4))

    # for each value inside the results lists from the pretty print json
    for each in js['results']:

        # get the place_id value from place_id key from each list
        placeid = each['place_id']

        # print the placeid
        print("The place id value is " + str(placeid))
        break
    break
