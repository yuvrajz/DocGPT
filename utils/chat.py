import openai
from config import MODEL_NAME

def get_answer(context, question):
    prompt = f"Using the context below, answer the question:\n\nContext: {context}\n\nQuestion: {question}\nAnswer:"
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response['choices'][0]['message']['content']
