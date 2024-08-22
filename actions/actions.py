# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayCourseInterested(Action):

     def name(self) -> Text:
         return "action_say_course_interested"


     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course_interested = tracker.get_slot("course_interested")

        if not course_interested:      
            dispatcher.utter_message(text="I don't know which course you are interested in. ")
        else:       
            dispatcher.utter_message(text=f"Your course interested is {course_interested}!")
        return []
