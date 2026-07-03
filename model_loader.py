<<<<<<< HEAD
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model():
    model = T5ForConditionalGeneration.from_pretrained("./last_final_saved_translation_model")
    tokenizer = T5Tokenizer.from_pretrained("./last_final_saved_tokenizer_model")
    model.to(device)
=======
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model():
    model = T5ForConditionalGeneration.from_pretrained("./last_final_saved_translation_model")
    tokenizer = T5Tokenizer.from_pretrained("./last_final_saved_tokenizer_model")
    model.to(device)
>>>>>>> 8b1eac7 (Initial commit)
    return model, tokenizer, device