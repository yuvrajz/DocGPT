import gradio as gr
from utils import loader, embedder, chat

def run_app(file, url, question):
    if file:
        if file.name.endswith(".txt"):
            text = loader.load_txt(file)
        elif file.name.endswith(".docx"):
            text = loader.load_docx(file)
        else:
            return "Unsupported file format"
    elif url:
        text = loader.load_url(url)
    else:
        return "Provide a file or URL."

    texts = [text]
    index, embeddings, docs = embedder.create_index(texts)
    context = embedder.search(question, index, docs, embeddings)
    return chat.get_answer(context, question)

gr.Interface(
    fn=run_app,
    inputs=[gr.File(), gr.Textbox(label="URL"), gr.Textbox(label="Question")],
    outputs="text",
    title="Chat with Your Document (OpenAI)"
).launch()
