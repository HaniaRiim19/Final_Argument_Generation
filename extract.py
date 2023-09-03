def extract_sentences_with_labels(input_file, output_file, target_labels):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    extracted_sentences = []
    for line in lines:
        sentence, label = line.strip().split('\t')
        if label in target_labels:
            # Store both sentence and label
            extracted_sentences.append((sentence, label))

    with open(output_file, 'w', encoding='utf-8') as f:
        for sentence, label in extracted_sentences:
            # Write sentence and label together
            f.write(f"{sentence}\t{label}\n")
    print("Extraction complete. Extracted sentences saved to", output_file)



    
