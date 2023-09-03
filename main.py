from preprocess import *
from infer import*
from extract import*
from summarise import*
from arguments import *
from test import*
import pandas as pd
import numpy as np
import re
from PyPDF2 import PdfReader
import os
import docx

def main():
    input_file_path = "input_file.txt"
    output_directory = "infer/data"
    target_labels = ["Facts", "Ratio of the decision"]  # Specify your target labels
    num_sentences= 40  # Specify the number of sentences for the summary

    # Step 1: Preprocess the input text 
    processed_file_path = process_text(input_file_path, output_directory)

    # Step 2: Asssign labels to each sentence in the document
    infer()

    # Step 3: Extract only sentences which are Facts or Ratio of the Decision 
    extract_sentences_with_labels('infer/predictions.txt', 'infer/predictions_facts.txt', target_labels)

    # Step 4: Summarise the extracted sentences
    input_file = "infer/predictions_facts.txt"
    output_file = "infer/final/case_summary.txt"
    num_top_sentences = 40
    extract_summary(input_file, output_file, num_top_sentences)

    # Read the summary
    train_directory = 'infer/final'
    text_data = read_documents_from_directory(train_directory)
    text_data = re.sub(r'\n+', '\n', text_data).strip()  # Remove excess newline characters

    with open("infer/train.txt", "w") as f:
      f.write(text_data)

    train_file_path = "infer/train.txt"
    model_name = 'gpt2'
    output_dir = '/content/drive/MyDrive/Final_Argument_Generation/result'
    overwrite_output_dir = False
    per_device_train_batch_size = 8
    num_train_epochs = 50.0
    save_steps = 50000

    # Train
    train(
        train_file_path=train_file_path,
        model_name=model_name,
        output_dir=output_dir,
        overwrite_output_dir=overwrite_output_dir,
        per_device_train_batch_size=per_device_train_batch_size,
        num_train_epochs=num_train_epochs,
        save_steps=save_steps
    )

    #Step 5: Final Argument Generation
    model2_path = "result"
    sequence2 = "What can we infer from the text?"
    max_len = 500
    arguments=generate_arguments(model2_path, sequence2, max_len)

    # Specify the path to the file containing the original text
    file_path = 'infer/predictions_facts.txt'

    # Read the original text from the file
    original_text = read_text_from_file(file_path)

    #Step 6: Calculate and print the cosine similarity score
    similarity_score = calculate_similarity(original_text, arguments)
    print(f"Cosine Similarity Score: {similarity_score} \n")

    #Argument Generation 2
    model2_path = "result"
    sequence2 = "what decision can we make from the text?"
    max_len = 500
    arguments=generate_arguments(model2_path, sequence2, max_len)

    
        

if __name__ == "__main__":
     main()
