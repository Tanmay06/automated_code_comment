import json
import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_comment(command):
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    input_text = f"Comment on SQL command: {command}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=1700, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)
    generated_comment = tokenizer.decode(output[0], skip_special_tokens=True)[:50]
    return generated_comment


def main():
    with open('./data/create_table.json', 'r') as file:
        data = json.load(file)

    sql_commands = data.get('sql_commands', [])
    df = pd.DataFrame({'sql_commands': sql_commands})
    df['comments'] = df['sql_commands'].apply(generate_comment)
    df.to_csv('./data/create_table_comments.csv', index=False)

if __name__ == "__main__":
    main()
