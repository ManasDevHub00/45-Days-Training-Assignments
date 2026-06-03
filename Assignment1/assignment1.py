"""
1. Explain the difference between the following data types with examples: 
• Integer (int)  
• Float (float)  
• String (str)  
• Boolean (bool) """

# Anaswer:
# Integer (int) - it is data type that represents whole numbers without a decimal point. Example: 5, -3, 0
num = 10
num1 = -5
print(type(num))
print(type(num1))

# Float (float) - it is a data type that represents numbers with a decimal point. Example: 3.14, -0.5, 0.0
pi = 3.14
print(type(pi))

# String (str) - it is a data type that represent a sequence of characters enclosed in quotes (single or double). 
# Example: "Hello", 'Python', "123"
str = "Hello World"
print(type(str))

# Boolean (bool) - it is a data type that represents  True or False. Example: True, False
a = True
b = False
print(type(a))
print(type(b))

"""Q2 write a python program to create three variables 
name 
age 
city 
Store your details in them and print the values 
"""
name = " Manas"
age = 20
city = "Bangalore"  

print("Name:", name)
print("Age:", age)
print("City:", city)


"""Q3 Write a python program that:
Take's user name as input.
Prints the name in uppercase .
Prints the total number of characters in the name."""

user_name = input("Enter your name: ")
print("Name in uppercase:", user_name.upper())
print("Total number of characters in the name:", len(user_name))

"""4. Explain any five commonly used string methods in Python with 
examples."""

# 1. upper() - it is a string method that is used to convert all characters in a string to uppercase 
# Example:
str1 = "hello world"
print(str1.upper())  # Output: "HELLO WORLD"

# 2. lower() - it is a string method that is used to convert all characters in a string to lowercase
# Example:
str2 = "HELLO WORLD"
print(str2.lower())  # Output: "hello world"

# 3. strip() - it is a string method that is used to remove any leading and trailing whitespace from a string
# Example:
str3 = "   Hello World   "
print(str3.strip())  # Output: "Hello World"

# 4. replace() - It is a string method that is used to replace a specifice string with another string in a given string 
# Example:
str4 = "Hello World"
print(str4.replace("World", "Python"))  # Output: "Hello Python"

# 5. isdigit() - it is a string method that is used to check if all characters in a string are digits.
# It returns True if all characters are digits, otherwise it returns False
# Example:
str5 = "12345"
print(str5.isdigit())  # Output: True

str6 = "Hello123"
print(str6.isdigit())  # Output: False

"""
Q5 Create a list containing the names of five fruits.
Print the complete list.
Print the first and last fruit element.
Print the total number of fruits in the list."""

fruit = ["Apple","Banana","Mango","Grapes","Orange"]

print("First element:", fruit[0])
print("Last element:", fruit[-1])

print("Total number of items in the list:", len(fruit))

"""Q6 write a python program to 
create a list of numbers [10,20,30,40,50]
Add 60 to the list
Remove 20 from the list
print updated list"""

l1 = [10, 20, 30, 40, 50]
l1.append(60)
l1.remove(20)
print("Updated list:", l1)



"""7. What is Artificial Intelligence (AI)? Explain its importance and mention 
any four real-life applications of AI. """

# answer:
"""Aritificial Intelligence (AI) is a branch of computer science that focuses 
on creating the ability of machine to perfrom tasks that require human intelligence.
These tasks include problem sloving, leraning , understanding natural language, and making decisions.

AI systems are different from traditional software because traditional software follows a set of predefined 
rules and instructions to do a task whereas AI systems can learn from data and experience make their decision 
based on that learning and get better over time ."""

# Importance of AI:
"""1.Automation: AI can automate reptitive tasks,  which can save time , money and increase efficiency this leds 
pepole to focus on more complex and creative tasks."""

"""2. Data Analysis: AI can analyze large amounts of data quickly and accurately, which can help businesses make 
informed decisions and identify patterns and trends that may not be apparent to humans. For human it is difficult to
analyze large data but AI can do it easily """

"""3. 24/7 Availability: AI systems can operate 24/7 without the need for breaks or rest.This can incerase productivity
and provide continuous support to customers and users."""

#  Four Real-life applications of AI:

"""1. Virtual Assistants 
AI powered virtual assistants like Siri, Alexa, and Google Assistant can perform tasks such as setting reminders, answering questions, 
play music and controlling smart home devices. These assistence use ML and NLP to understand and respond to user commands."""

"""2.Recommendation Systems
Companies like Netflix , Prime videos , Amazon , You Tube and Soitfy use Ai based recommendation system to suggest best movies , music , shows 
videos and products to user according to their perferences and behavior.
These systems analyze user data like search history , past purchases and ratings to provide personalized recommendations.Then 
these recommendation system can increase user engagement and sales for businesses."""

"""3. Autonomous Vehicles
AI is a key technology behind self-driving cars. Autonomous vehicles use AI algorithms to process data from sensors and cameras to 
navigate and make decisions on the road. This technology has the potential to improve road safety and reduce traffic congestion."""

"""4. Healthcare 
 AI is widely used in healthcare for diagnosing several diseeases from X ray and MRI scan which help to find the diesease like cancer ,
 tumor and other diesease at early stage and also help to find best treatment for patient and also help to find the drug discovery 
 in less time . """

"""8.  Identify whether the following are examples of AI and explain why: 
• ChatGPT  
• Google Maps route prediction  
• Calculator  
• Netflix recommendations  
• Voice assistants (Alexa/Siri) """

#Answer:
"""1. ChatGPT - Yes, ChatGPT is an example of AI. It is a LLM(Large Language Model) developed by OpenAI .
It trained on a large dataset of test and can generate human_like responses to user input. It uses natural 
language processing (NLP) and machine learning (ML) techniques to understand and respond to user queries."""

"""2. Google Maps route prediction - Yes, this is an example of AI. Google Maps uses AI alogorthims to analyz 
traffic data, user behavior , road conditions and other factors to predict the best route for users. 
It can also provide real-time updates and alternative routes based on changing traffic conditions."""

"""3 .Calculator - No, a calculator is not an example of AI because it is a simple too that performa basic
arthimetic operations based on predefined rules and instructions it does not have any learning or 
decision making capabilities."""

"""4. Netflix recommendations - Yes, this is an example of AI.  Netflix uses AI based recommendation system to 
suggest movies and TV shows  to users according to their preferences. It analysis user pervious viewing history 
and behavior  according that decided what kind of shows like by users like comdey,action,fiction etc. This helps 
to increase user engagement and satisfaction."""

"""5. Voice assistants (Alexa/Siri) - Yes, voice assistants like Alexa and Siri are examples of AI. They use natural 
language processing (NLP) and machine learning (ML) techniques to understand the human language respond according to it . 
They can perform tasks such as setting reminders, answering questions, playing music, and controlling smart home devices 
based on user input."""

