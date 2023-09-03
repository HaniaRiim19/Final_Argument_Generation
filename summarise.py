from sklearn.feature_extraction.text import TfidfVectorizer

def extract_summary(input_file, output_file, num_top_sentences):
    # Load data from the input file
    sentences = []
    labels = []
    with open(input_file, "r") as file:
        for line in file:
            sentence, label = line.strip().split("\t")
            sentences.append(sentence)
            labels.append(label)

    # Initialize TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Calculate TF-IDF scores for sentences
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Calculate sentence scores based on TF-IDF scores
    sentence_scores = tfidf_matrix.sum(axis=1)

    # Combine sentence scores, sentences, and original order
    sentence_info = list(zip(sentences, sentence_scores, labels))

    # Sort sentences based on scores while maintaining original order
    sorted_sentences = sorted(sentence_info, key=lambda x: x[1], reverse=True)

    # Choose the top sentences for your summary
    top_sentences = [sentence for sentence, score, label in sorted_sentences[:num_top_sentences]]
    top_labels = [label for sentence, score, label in sorted_sentences[:num_top_sentences]]

    # Create a new output file for the summary
    with open(output_file, "w") as file:
        for sentence, label in zip(top_sentences, top_labels):
            file.write(f"{sentence}\t{label}\n")

    print("Summary written to", output_file)


