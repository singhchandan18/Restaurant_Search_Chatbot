## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "singh.chandan1809@gmail.com"}
    - slot{"email": "singh.chandan1809@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
* affirm
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "singh.chandan1809@gmail.com"}
    - slot{"email": "singh.chandan1809@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
* affirm
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_email_address
* deny
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_email_address
* deny
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "singh.chandan1809@gmail.com"}
    - slot{"email": "singh.chandan1809@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
* affirm
    - utter_goodbye
	- action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "singh.chandan1809@gmail.com"}
    - slot{"email": "singh.chandan1809@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_email_address
* deny
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "xyz.res"}
    - slot{"email": "xyz.res"}
    - action_send_email
    - slot{"email_sent": false}
    - utter_invalid_email
* restaurant_search{"email": "singh.chandan1809@gmail.com"}
    - slot{"email": "singh.chandan1809@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "1"}
    - slot{"budget": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "sigh_chandan"}
    - slot{"email": "sigh_chandan"}
    - action_send_email
    - slot{"email_sent": false}
    - utter_invalid_email
* restaurant_search{"email": "singh.chandan18@gmail.com"}
    - slot{"email": "singh.chandan18@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - utter_email_address
* deny
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "delhi"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "singh.chandan1809@gmail.com"}
    - slot{"email": "singh.chandan1809@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Pune"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Pune"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "singh.chandan18@gmail.com"}
    - slot{"email": "singh.chandan18@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
	- action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "singh.chandan1809@gmail.com"}
    - slot{"email": "singh.chandan1809@gmail.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bilaspur"}
    - slot{"location": "Bilaspur"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "Bilaspur"}
    - utter_email_address
* deny
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_search_restaurants
    - slot{"location": "bengaluru"}
    - utter_email_address
* restaurant_search{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_verify_location
    - slot{"location_match": false}
    - utter_teir3
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "3"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "1"}
    - slot{"budget": "1"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
    - utter_goodbye
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_verify_location
    - slot{"location_match": false}
    - utter_teir3
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "1"}
    - slot{"budget": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_email_address
* affirm
    - utter_ask_email_address
* restaurant_search{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"email_sent": true}
    - utter_email_sent
	- action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location_match": true}
    - utter_ask_budget
* restaurant_search{"budget": "1"}
    - slot{"budget": "1"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_email_address
* deny
    - utter_goodbye
	- action_restart
