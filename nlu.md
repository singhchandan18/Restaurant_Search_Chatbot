## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Thanks!
- Yes
- Thanks
- yes. Please

## intent:deny
- No
- no
- nope, Thanks
- No, thank you
- No, Thanks
- no, thanks
- no. thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- sendemail

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hello
- hola
- Hello!
- hello!

## intent:restaurant_search
- i'm looking for a place to eat
- could you please find me a restaurant?
- I want to grab lunch
- I am searching for a dinner spot
- I am searching for a restaurant
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "budget", "value": "mid"} budget range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- please find me a restaurant
- [Lesser than Rs. 300]{"entity": "budget", "value": "1"}
- [Rs. 300 to 700]{"entity": "budget", "value": "2"}
- [More than 700]{"entity": "budget", "value": "3"}
- [singh.chandan1809@gmail.com](email)
- [singh.chandan18@gmail.com](email)
- please find me a [chinese](cuisine) restaurant in [delhi](location)
- please find me a restaurant in [delhi](location)
- please find me a restaurant in [jabalpur](location)
- I am looking for a restaurant
- gurgaa
- [Delhi](location)
- I am looking for a restaurant in [mumbai](location)
- [American](cuisine)
- [Gurra](location)
- please find me a restaurant in [Jaipur](location)
- [singhchandn](email)
- Please find me a restaurant in [Pune](location)
- [ahcjjc](location)
- please find me a restaurant in [indore](location)
- [kjuuss](location)
- Please find me a restaurant in [Rewa](location)
- please find me a restaurant in [Shirdi](location)
- [jalgaon](location)
- Please find me a restaurant in [Jaipur](location)
- [xyz.res](email)
- can you please find me a restaurant
- [Mumbai](location)
- [sigh_chandan](email)
- please show me restaurants in [Agra](location)
- I am looking for [South Indian](cuisine) restaurant in [delhi](location)
- Please find me a [North Indian](cuisine) restaurant in [Pune](location)
- hi, can you please find me an [italian](cuisine) restaurant
- [Bengaluru](location)
- I am looking for some restaurants
- [Bilaspur](location)
- Im hungry. Looking out for some good restaurants
- [bengaluru](location)
- [Mexican](location)
- I'll prefer [italian](cuisine)
- [300-700 range]{"entity": "budget", "value": "2"}
- yes. Please send it to [ahbcdj@dkj.com](email)
- Can you suggest some good restaurants in [Rishikesh](location)
- Okay. Show me some in [Allahabad](location)
- Ill prefer [chines]{"entity": "cuisine", "value": "chinese"}
- [>700]{"entity": "budget", "value": "3"}
- [xyz@sth.edu](email)
- Can you suggest some good restaurants in [kolkata](location)
- [american](cuisine)
- [<300]{"entity": "budget", "value": "1"}
- [jddk.2jmd@kdl.co.in](email)
- in [mubaim](location)
- in [Mumbai](location)
- Im hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- [<300]{"entity": "budget", "value": "1"}

## synonym:1
- Lesser than Rs. 300
- <300

## synonym:2
- Rs. 300 to 700
- 300-700 range

## synonym:3
- More than 700
- >700

## synonym:4
- four

## synonym:Bangalore
- Bengaluru

## synonym:Chennai
- Madras

## synonym:Delhi
- New Delhi
- dilli

## synonym:Gurugram
- Gurgaon

## synonym:Kolkata
- Calcutta

## synonym:Mumbai
- Bombay

## synonym:Vadodara
- Baroda

## synonym:Varanasi
- Benares

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
