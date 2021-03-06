from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted

config={ "user_key":"f34bf64ba47d7efdbbf079a6a0803983"}
global response
global RestaurantList
RestaurantList = []

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
    
    ## Function to filer out the restaurants, based on the user's budget(avg cost for two people).
    def FetchRestaurantsOnUserBudget(self, lbudget, lrestaurants):
        lbudget = int(lbudget)
        MinBudget = 0
        MaxBudget = 999999999
        lcount = 1
        response=""
        # Clear the existing results for a new session
        RestaurantList.clear()

        if lbudget == 1:
           MaxBudget = 299
        elif lbudget == 2:
           MinBudget = 300
           MaxBudget = 700
        elif lbudget == 3:
           MinBudget = 700
    
        for restaurant in lrestaurants:
            RestaurantDict = {}
            ## Check if the Averag Cost is within the range of User's budget.
            if MinBudget <= restaurant['restaurant']['average_cost_for_two'] <= MaxBudget:
                RestaurantDict['name'] = restaurant['restaurant']['name']
                RestaurantDict['rating'] = restaurant['restaurant']['user_rating']['aggregate_rating']
                RestaurantDict['avgcost'] = restaurant['restaurant']['average_cost_for_two']
                RestaurantDict['address'] = restaurant['restaurant']['location']['address']
                RestaurantList.append(RestaurantDict)
                #response = response + "Found "+ restaurant['restaurant']['name']+ " User Rating "  + restaurant['restaurant']['user_rating']['aggregate_rating'] + " in "+ restaurant['restaurant']['location']['address']+"\n"

        if len(RestaurantList) == 0:
            response = "Not able to find any restaurants, matching your requirements"
        else:
            response = "Searching ... \n"
            for restaurant in sorted(RestaurantList, key = lambda k: k['rating'], reverse = True):
                if lcount <= 5:
                    response = response + restaurant['name']  + " in "+ restaurant['address'] + " has been rated " + str(restaurant['rating']) + "\n"
                else:
                    break
                lcount += 1
            response = response + "-----Search Finished ... \n\n"
        return response
	
    def run(self, dispatcher, tracker, domain):
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        print(budget)
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'mexican':73,'chinese':25,'italian':55,'north indian':50,'south indian':85, 'American':1}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
        d = json.loads(results)
        response=""

        if d['results_found'] == 0:
            response= "no results"
        else:
            response = self.FetchRestaurantsOnUserBudget(budget, d['restaurants'])
            
        dispatcher.utter_message("-----"+response)
        return [SlotSet('location',loc)]

# Store the list of Tier 1 and Tier 2 cities in a list 
AvailableCities = ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar'
,'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore'
, 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon'
, 'Guwahati', 'Hamirpur', 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada'
, 'Kannur', 'Kanpur', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram'
, 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Patna', 'Pondicherry', 'Purulia', 'Prayagraj'
, 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 'Thiruvananthapuram', 'Thrissur'
, 'Tiruchirappalli', 'Tiruppur', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal'
, 'Madras', 'Calcutta', 'Bangalore', 'Bombay', 'Baroda', 'Calicut', 'Cochin', 'Benares', 'Belagavi', 'Jamshedpur', 'Gurugram', 'Palakkad', 'Quilon', 'Allahabad']

# Convert the city name to lower case 
AvailableCities1 = [ city.lower() for city in AvailableCities ]


# Class to verify, if the location inputed by the user is in Tier1 and Tier2 list.
class VerifyLocation(Action):
    def name(self):
        return 'action_verify_location'
        
    def run(self, dispatcher, tracker, domain):
        zomato = zomatopy.initialize_app(config)
        loc = str(tracker.get_slot('location')).lower()
        
        if loc in AvailableCities1:
            return [SlotSet('location_match', True)]
        else:
            return [SlotSet('location_match', False)]

# Class to verify the inputed email-id and send the list of top 10 restaurants to the user by email.            
class SendEmail(Action):
    def name(self):
        return 'action_send_email' 
    
    def run(self, dispatcher, tracker, domain):
        import re
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText  
        
        zomato = zomatopy.initialize_app(config)
        reciever_email = str(tracker.get_slot('email'))
        
        #The mail addresses and password
        sender_address = 'singh.chandan181109@gmail.com'
        sender_pass = 'Syddon@18'
        
        if re.match('^[\w].*[@][\w]*[\.][a-z|A-Z]', reciever_email):
            response = ""
            res = ""
            for restaurant in sorted(RestaurantList, key = lambda k: k['rating'], reverse = True):
                    res = restaurant['name'] + "\n" +  restaurant['address'] + "\n" +  str(restaurant['avgcost']) + "\n" +  str(restaurant['rating']) + "\n\n"
                    response = response + res
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = "Foodie"
            message['To'] = reciever_email
            message['Subject'] = 'Restaurant List'   #The subject line
            email_content = "Hello," + "\n" + "As per your request, please find below the list of available restaurants matching your requirements: \n" + response + "Thank You \n"
            #The body and the attachments for the mail
            message.attach(MIMEText(email_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, reciever_email, text)
            session.quit()
            return [SlotSet('email_sent', True)]
        else:
            return [SlotSet('email_sent', False)]


# Class to restart the existing session.
class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'
	def run(self, dispatcher, tracker, domain):
		return[Restarted()]