import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_news(headlines):

    text = "\n".join(headlines)

    prompt = f"""
    Summarize these news headlines in 4-5 lines:

    {text}
    """

    response = model.generate_content(prompt)

    return response.text