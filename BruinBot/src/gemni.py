import textwrap
import google.generativeai as genai

from IPython.display import Markdown

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [

]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["My name is Eric"]
  },
  {
    "role": "model",
    "parts": ["It's nice to meet you, Eric! What would you like to talk about today?"]
  },
])


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def initialize_gemini():
    try:
        # Replace 'userdata.get' with the method you use to securely fetch your API key.
        GOOGLE_API_KEY = $hidden$
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')        
        return model
    except Exception as e:
        print(f"Failed to initialize Gemini API: {e}")
        return None

def main():
    model = initialize_gemini()
    if not model:
        return
    
    print("Welcome to Gemini terminal interaction! Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter your question: ")
        if user_input.lower() == 'exit':
            break
        
        try:
            # Constructing the input data in the expected format
            input_data = {
                "parts": [
                    {"text": user_input}  # Assuming 'text' is the correct key for simple text inputs
                ]
            }
            response = model.generate_content(input_data)
            print(response.candidates[0].content.parts[0].text)
        except Exception as e:
            print(f"Error processing your question: {e}")



if __name__ == '__main__':
    main()
