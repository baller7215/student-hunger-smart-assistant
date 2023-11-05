# Import the modules
import requests
import json
import googlemaps

# Varibles & User assignment
keyword = input("What would you like to search for?: ")
price_range = input("Enter price range (1-4): ")
user_radius = input("Enter radius: ")
start_location = input("Enter start location: ")
end_location = input("Enter end location: ")
#start_location = "557 E Peltason Dr, Irvine, CA 92612"
#end_location = "1100 Stanford Irvine, CA 92foodfoo612"

#YELP
# Define API Key, Business Path, and Header
MY_API_KEY = '6mLB3ALj81mZE8sRJRG_vcHFxwiSNil68L_4oXGfoOIRpt71HZefFEnyB64sqCX6hbwefrd59r0lm-KMcXwopls3WnbhkU7noAp4Nj1-WQJYVzXxN0x3i51BE5RGZXYx'
BUSINESS_PATH = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % MY_API_KEY}


"""--------------------------------------------------"""


#GOOGLEMAPS to find the midpoint coordinates (latitude and longitude)
api_key = "AIzaSyAfRQpoq3taz21mykNEsicxmJ9SmR4If4g"

# Construct the request URL
url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_location}&destination={end_location}&mode=walking&key={api_key}"

# Send the request
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract the route information
if "routes" in data and len(data["routes"]) > 0:
    route = data["routes"][0]
    
    # Get the polyline points from the overview_polyline
    overview_polyline = route["overview_polyline"]["points"]
    
    # Decode the polyline points
    from polyline import decode
    points = decode(overview_polyline)
    
    # Calculate the midpoint index
    total_points = len(points)
    midpoint_index = total_points // 2
    
    # Get the coordinates of the midpoint
    midpoint = points[midpoint_index]
    
    # The midpoint is a tuple of (latitude, longitude)
    latitude, longitude = midpoint
    
    #print(f"Midpoint coordinates: {latitude}, {longitude}")
    latitude_coor = latitude
    longitude_coor = longitude
else:
    print("No route found.")


"""--------------------------------------------------"""


#YELP
# Define the Parameters of the search
PARAMETERS = {'term': keyword,
              'limit': 50,
              'radius': user_radius,
              'price': price_range,
              'latitude': latitude_coor,
              'longitude': longitude_coor,
              'sort_by': 'best_match'}

# Make a Request to the API, and return results
response = requests.get(url=BUSINESS_PATH, 
                        params=PARAMETERS, 
                        headers=HEADERS)

# Convert response to a JSON String
business_data = response.json()  

# print the data
print(json.dumps(business_data, indent = 3))

file_path = 'business_data.txt'

# Open the file in write mode and write the JSON data
with open(file_path, 'w') as file:
    file.write(json.dumps(business_data, indent=3))

# Print a message to confirm that the data has been saved
print(f"Business data has been saved to {file_path}")