import textwrap
import google.generativeai as genai
import os
import reflex as rx

from IPython.display import Markdown

# Configuration settings for the generative model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192
}

safety_settings = []
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# class TutorialState(rx.State):
#     question: str
#     chat_history: list[tuple[str, str]]

#     async def answer(self):
#         GOOGLE_API_KEY = os.getenv("AIzaSyC7LY2KvbhIy7zVKPiB-Xzi7sUsdvpzR9w")
#         genai.configure(api_key=GOOGLE_API_KEY)

#         answer = ""
#         self.chat_history.append((self.question, answer))
#         # self.question = ""
#         yield


def training_queries():
    return model.start_chat(history=[])

class TutorialState(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    async def answer(self):
        GOOGLE_API_KEY = "AIzaSyC7LY2KvbhIy7zVKPiB-Xzi7sUsdvpzR9w"
        genai.configure(api_key=GOOGLE_API_KEY)
        convo = training_queries()

        answer = convo.send_message(self.question)
        self.chat_history.append((self.question, answer.text))
        self.question = ""
        yield