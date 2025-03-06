# Cosine Similarity Summarizer

## Overview
This project provides a text summarization tool based on cosine similarity. It selects the most relevant sentences from a given text using a BERT-based Sentence Transformer model and saves the generated summary.

## Features
- Uses **sentence-transformers** for embedding generation.
- Computes **cosine similarity** between sentences and the overall text.
- Selects the most important sentences to generate a summary.
- Saves the summary automatically in a specified folder.

## Requirements
Make sure you have the following dependencies installed before running the script:

```bash
pip install sentence-transformers nltk
```

## Usage

1. Run the script:

```bash
python cosine_similarity.py
```

2. A file selection window will open. Choose a `.txt` file to summarize.
3. The script will process the file and generate a summary.
4. The summary will be saved in the `cos_sim_summaries/` folder with the same name as the input file.

## Output
The summarized text is saved as a `.txt` file inside the `cos_sim_summaries/` directory.

## Folder Structure
```
cosine-similarity-summarizer/
│── README.md
│── cosine_similarity.py
│── cos_sim_summaries/  # Summarized files will be stored here

## Notes
- The script automatically downloads required NLTK data if not already available.
- It selects **1/6th of the total sentences** based on their similarity scores.

## License
This project is open-source and available under the MIT License.

