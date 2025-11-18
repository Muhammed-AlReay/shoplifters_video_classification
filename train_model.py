import os
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoFeatureExtractor, AutoModelForVideoClassification
from load_video import load_video

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

SAVE_DIR = "saved_model"
os.makedirs(SAVE_DIR, exist_ok=True)

MODEL_NAME = "MCG-NJU/videomae-base-finetuned-kinetics"
NUM_LABELS = 2  
fe = AutoFeatureExtractor.from_pretrained(MODEL_NAME)
model = AutoModelForVideoClassification.from_pretrained(MODEL_NAME, num_labels=NUM_LABELS, ignore_mismatched_sizes=True)
model.to(DEVICE)


model.save_pretrained(SAVE_DIR)
fe.save_pretrained(SAVE_DIR)
print(f"Model and feature extractor saved to {SAVE_DIR}")
