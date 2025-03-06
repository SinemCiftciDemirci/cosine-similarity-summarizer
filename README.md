# Cosine Similarity Summarizer

## Overview
This project provides a text summarization tool based on cosine similarity. It selects the most relevant sentences from a given text using a BERT-based Sentence Transformer model and saves the generated summary.

🔗 Related Projects This project is part of a modular research framework for evaluating and improving fairy tale summarization models. Below are the related repositories:

| Children's Tale Summarizer - Flask App | The main Flask-based API that generates fairy tale summaries. (https://github.com/SinemCiftciDemirci/childrens-tale-summarizer-flask-app) |

| GPT Summarizer | Creates GPT-based fairy tale summaries. (https://github.com/SinemCiftciDemirci/gpt-summarizer) |

| Cosine Similarity Summarizer | Performs extractive summarization using cosine similarity. (https://github.com/SinemCiftciDemirci/cosine-similarity-summarizer) |

| Single Summary Evaluation | Measures the performance of a single summary using BERTScore and ROUGE score. (https://github.com/SinemCiftciDemirci/single-summary-evaluation) |

| Batch Summary Performance Evaluation | Compares model-generated summaries with GPT and Cosine-based reference summaries, calculating ROUGE and BERTScore collectively. (https://github.com/SinemCiftciDemirci/batch-summary-performance-evaluation) |

| Summary Performance Comparison | Creates visual performance comparisons from the Model_Performance.xlsx file produced in the Batch Summary Evaluation repo. (https://github.com/SinemCiftciDemirci/summary-performance-comparison) |

| Vision Model Test | Translates the generated summaries into English and creates three visuals: introduction, development, and conclusion. (https://github.com/SinemCiftciDemirci/vision-model-test) |

Each repository serves a unique role in evaluating or improving summarization models. You can use them individually or together for deeper analysis.


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

