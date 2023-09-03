import os
import re

def process_text(input_file_path, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get the base filename
    filename = os.path.basename(input_file_path)

    # Create the output file path
    output_file_path = os.path.join(output_directory, f"output_{filename}")

    # Read the file
    with open(input_file_path, "r") as file:
        content = file.read()

    # Extract the text after "HEADNOTE:"
    match = re.search(r"HEADNOTE:(.*)", content, re.DOTALL)
    if match:
        text = match.group(1)
    else:
        text = ""

    # Remove the newline character before splitting the paragraphs into sentences
    text = text.replace("\n", " ")

    # Insert spaces between concatenated words
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)

    # Split the paragraphs into sentences using full stops or semicolons (excluding specific abbreviations)
    sentences = re.split(
        r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|;)(?<!\b[A-Za-z]\.)(?<!\bAct\.)\s(?!\d+\.\s)(?<!Cal\.\s)",
        text)

    # Write the sentences to the output file
    with open(output_file_path, "w") as output_file:
        for sentence in sentences:
            output_file.write(sentence.strip() + "\n")
    print("Sentences have been written to", output_file_path)
    return output_file_path

