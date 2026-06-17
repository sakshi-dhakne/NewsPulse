import google.generativeai as genai

genai.configure(api_key="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")

model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_news(headlines):

    text = "\n".join(headlines)

    prompt = f"""
    Summarize these news headlines in 4-5 lines:

    {text}
    """

    response = model.generate_content(prompt)

    return response.text