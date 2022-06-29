# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


#shift, enter then run cell with data 

#Book Recommendations Chatbox
#- have a conversation to recommend a book
 #  - maybe we can create a database of different books for categories or look up popular books (idk if the chatbot can do that)
#- checks local libraries (in your area) for availability of the book - open accessible API?
#- ask how the chatbot did and store it to a database (database of reviews) - firebase?
# open source project or just open source framework?

#. ./venv/bin/activate
# rasa interactive
# rasa visualize


#overall clean up code by Friday

#actually make these work with intended functionality
#error checking/NLU fallback (?)
#finalize all stories, intents, etc...work
# synonyms below intents?
# actions in domain file at the end? idk what that is 
class ActionZipcode(Action):
    def name(self) -> Text:
        return "action_zipcode"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_search(text="Libraries searched.")

        return []


class ActionGenre(Action):
    def name(self) -> Text:
        return "action_genre"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_recommend(text="Books recommended")

        return []


class ActionGenre(Action):
    def name(self) -> Text:
        return "action_genre"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        import requests
        genre = str(tracker.get_slot("genre"))

        url = "https://hapi-books.p.rapidapi.com/week/{}"

        headers = {
	        "X-RapidAPI-Key": "f0a08a2e27mshbbcba9e7478a9d3p166424jsn655128100cf2",
	        "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
            }

        response = requests.request("GET", url.format(genre), headers=headers)
        data = response.json()
        
        #edit
        try:
            title = data["books"][0]["book"]
        except:
            title = "Sorry, there is no book in this genre."
        dispatcher.utter_recommend(text="{}({}): {}".format(genre))
        return []



