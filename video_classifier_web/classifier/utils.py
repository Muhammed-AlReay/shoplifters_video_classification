import os
import cv2
import torch
import numpy as np
from transformers import AutoImageProcessor, VideoMAEForVideoClassification

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_DIR = "D:/Mohamed/Deep/video_classification/src/saved_model"

processor = AutoImageProcessor.from_pretrained(MODEL_DIR)
model = VideoMAEForVideoClassification.from_pretrained(MODEL_DIR)
model.to(DEVICE)
model.eval()

CLASS_NAMES = ['non shop lifters', 'shop lifters']

def load_video(path, num_frames=16, size=(224, 224)):
    cap = cv2.VideoCapture(path)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    indices = np.linspace(0, max(0, total-1), num_frames).astype(int)
    frames = []

    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if not ret:
            frame = np.zeros((size[1], size[0], 3), dtype=np.uint8)
        frame = cv2.resize(frame, size)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)

    cap.release()
    return np.array(frames)

def predict_video(video_path):
    frames = load_video(video_path)
    inputs = processor(list(frames), return_tensors="pt", sampling_rate=1)
    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1)[0]

    pred_idx = torch.argmax(probs).item()
    confidence = probs[pred_idx].item() * 100
    return CLASS_NAMES[pred_idx], confidence
