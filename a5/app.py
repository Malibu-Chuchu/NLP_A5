from flask import Flask, request, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load the model and tokenizer
model_path = "PattycherryAnker/optimize-human-preference"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get user input from the form
        user_input = request.form.get("prompt")
        inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = model.generate(
                inputs.input_ids,
                attention_mask=inputs.attention_mask,
                max_length=100,
                num_return_sequences=1,
                pad_token_id=tokenizer.eos_token_id,
            )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return render_template("index.html", prompt=user_input, response=response)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)