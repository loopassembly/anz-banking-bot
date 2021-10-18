import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

DIALOGFLOW_PROJECT_ID = 'banking-blwv'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'
text_to_be_analyzed = ""




class chattxt:
    def __init__(self,txt):
        self.text=txt

    def response(self):
        global text_to_be_analyzed
        text_to_be_analyzed=self.text
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
        except InvalidArgument:
            raise
        return response.query_result.fulfillment_text

# chat =chattxt('hello')
# print(chat.response())

    
       



