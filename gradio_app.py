import gradio as gr
import requests

def generate_response(context, user_question, model):
    URL = "http://0.0.0.0:8000/get_ollama_response"
    data = {"context": context, "question": user_question, "model": model}
    response = requests.post(URL, json=data)
    if response.status_code == 200:
        return response.json()['response']
    return "Failed to connect the server!!!"


def submit_rating(response_text, rating):
    if rating is not None and response_text != "":
        url = "http://0.0.0.0:8000/insert_rating"
        data = {"response": response_text, "rating": rating}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return "Rating submitted successfully"
        return "failed to submit rating"

    return "No rating od response submitted"

with gr.Blocks() as iface:
    with gr.Row():
        context_input = gr.Textbox(label="Context")
        question_input = gr.Textbox(label="User Question")
        model_input = gr.Dropdown(label="Model", choices=["llama3.2:latest", "llama2:latest", "mistral:latest", "phi3:latest","gemma:latest"])
        submit_btn = gr.Button("Generate Response")

    response_output = gr.Textbox(label="Response", interactive=False)
    rating_input = gr.Slider(label="Rate the response", minimum=1, maximum=5, step=1)
    rating_btn = gr.Button("Submit Rating")
    rating_output = gr.Label()

    submit_btn.click(
        generate_response,
        inputs=[context_input, question_input, model_input],
        outputs=[response_output]
    )

    rating_btn.click(
        submit_rating,
        inputs=[response_output, rating_input],
        outputs=rating_output
    )

iface.launch()
