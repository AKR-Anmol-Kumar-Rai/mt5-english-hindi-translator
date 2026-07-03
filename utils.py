<<<<<<< HEAD
def data_cleaning(text):
    text = text.lower().strip()
    return text


def translate_text(text, model, tokenizer, device):
    text = data_cleaning(text)

    input_text = "translate English to Hindi: " + text

    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        truncation=True,
        padding=True
    ).to(device)

    outputs = model.generate(                # output is generated in form of token ids
        **inputs,
        max_length=50,
        num_beams=5
    )

    translation = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

=======
def data_cleaning(text):
    text = text.lower().strip()
    return text


def translate_text(text, model, tokenizer, device):
    text = data_cleaning(text)

    input_text = "translate English to Hindi: " + text

    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        truncation=True,
        padding=True
    ).to(device)

    outputs = model.generate(                # output is generated in form of token ids
        **inputs,
        max_length=50,
        num_beams=5
    )

    translation = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

>>>>>>> 8b1eac7 (Initial commit)
    return translation