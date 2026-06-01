from transformers import AutoModelForCausalLM, AutoTokenizer

from .config import NORML_MAXTOKEN, PROMPT, THINKING

model_name = "Qwen/Qwen3-0.6B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")


def convert(msg: str):
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": msg},
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=THINKING,
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(**model_inputs, max_new_tokens=NORML_MAXTOKEN)
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :].tolist()

    try:
        index = len(output_ids) - output_ids[::-1].index(151668)
    except ValueError:
        index = 0

    thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
    content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

    print(f"{thinking_content}")
    print("-" * 66)
    print(f"\n{content}")
    print("=" * 66)

    return content
