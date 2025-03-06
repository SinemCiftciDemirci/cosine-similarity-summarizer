from sentence_transformers import SentenceTransformer, util
import nltk
import tkinter as tk
from tkinter import filedialog
import os

# Check and download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Open file dialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])

if not file_path:
    print("No file selected.")
    exit()

# Read the file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Split text into sentences
sentences = nltk.sent_tokenize(text)
total = len(sentences)
print(total)

# Load the model (BERT-based Sentence Transformer model)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Vectorize all sentences
sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

# Convert the entire text into a vector
text_embedding = model.encode(text, convert_to_tensor=True)

# Compute cosine similarity
similarities = util.pytorch_cos_sim(sentence_embeddings, text_embedding)

# Rank sentences based on similarity scores
similarity_scores = similarities.squeeze(1).tolist()
ranked_sentences = sorted(zip(similarity_scores, range(len(sentences))), reverse=True)

# Select top-ranked sentences while preserving original order
num_sentences = total // 6
print(num_sentences)
selected_sentences_indices = sorted(ranked_sentences[:num_sentences], key=lambda x: x[1])

# Generate summary in original order
summary_sentences = [sentences[index] for _, index in selected_sentences_indices]
reference_summary = " ".join(summary_sentences)

# Save the summary to 'cos_sim_summaries' folder
summaries_folder = "cos_sim_summaries"
if not os.path.exists(summaries_folder):
    os.makedirs(summaries_folder)

# Generate a new file name based on the input file
base_name = os.path.basename(file_path)
summary_file_path = os.path.join(summaries_folder, f"{os.path.splitext(base_name)[0]}.txt")

with open(summary_file_path, "w", encoding="utf-8") as summary_file:
    summary_file.write(reference_summary)
        
print(f"Summary saved at '{summary_file_path}'")
