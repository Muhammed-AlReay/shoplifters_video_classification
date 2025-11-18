import cv2
import numpy as np

def load_video(path, num_frames=16, size=(224, 224)):
    cap = cv2.VideoCapture(path)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total <= 0:
        cap.release()
        return np.zeros((num_frames, size[0], size[1], 3), dtype=np.float32)

    indices = np.linspace(0, total - 1, num_frames, dtype=int)
    frames = []
    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if not ret:
            frame = np.zeros((size[0], size[1], 3), dtype=np.uint8)
        else:
            frame = cv2.resize(frame, (size[1], size[0]))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)
    cap.release()
    frames = np.stack(frames, axis=0).astype(np.float32)
    return frames
