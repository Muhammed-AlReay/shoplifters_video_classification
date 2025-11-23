# 🛒 Shoplifting Detection System

A Computer Vision Project for Retail Security

![Shoplifting Demo1](https://github.com/Muhammed-AlReay/shoplifters_video_classification/blob/main/1.jpeg)

![Shoplifting Demo2](https://github.com/Muhammed-AlReay/shoplifters_video_classification/blob/main/2.jpeg)

![Shoplifting Demo3](https://github.com/Muhammed-AlReay/shoplifters_video_classification/blob/main/3.jpeg)


## 📌 Overview

This project presents a **Shoplifting Detection System** designed to
identify suspicious activities in retail environments using **Computer
Vision** techniques.\
The system processes surveillance footage and detects actions that may
indicate potential theft, helping retailers enhance their security
measures and prevent losses.

The deployed solution is currently operational and provides actionable
insights that improve monitoring efficiency and real-time threat
analysis.

------------------------------------------------------------------------

## 🚀 Features

-   🎥 **Real-time video processing**
-   🤖 **Suspicious behavior detection** using computer vision
-   📊 **Alerts & insights** for shop owners and security teams
-   🛡️ Enhances retail security and theft prevention
-   ⚙️ Optimized for easy deployment in real store environments

------------------------------------------------------------------------

## 🧠 Technologies Used

-   Python\
-   OpenCV\
-   Deep Learning (CNN / LSTM / 3D-CNN / Transformer Models )
-   NumPy & Pandas\
-   TensorFlow / Keras or PyTorch
-   scikit-learn
-   Streamlit / django 

------------------------------------------------------------------------

## 📁 Project Structure

``` bash

video_classification/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── video_classifier_web/          ← Main Django Project
│   ├── __init__.py
│   ├── settings.py                ← Django Configuration
│   ├── urls.py                    ← Project-level URL Router
│   ├── asgi.py
│   └── wsgi.py
│
├── classifier/                    ← Main Application (App)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                   ← Video Upload Form
│   ├── models.py                  ← Video Database Model
│   ├── urls.py                    ← App-level URL Routing
│   ├── utils.py                   ← AI Model Prediction Logic
│   ├── views.py                   ← App Logic (Upload–List–Play–Delete)
│   └── migrations/
│       └── 0001_initial.py
│
├── media/                         ← Uploaded Video Files
│   └── videos/
│       └── (user uploaded videos)
│
└── templates/                     ← Front-End HTML Templates
    ├── upload.html                ← Video Upload Page
    ├── video_list.html            ← All Videos + Filtering
    ├── video_detail.html          ← Single Video Player
    └── confirm_delete.html        ← Delete Confirmation Page
```


------------------------------------------------------------------------


## ▶️ Installation & Usage

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/Muhammed-AlReay/shoplifters_video_classification.git
cd shoplifters_video_classification
```

### 2️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

``` bash
python app.py
```

------------------------------------------------------------------------

## 📦 Deployment

The system has been **successfully deployed** and tested in a simulated
retail environment.\
Deployment results show: - Improved monitoring accuracy\
- Faster detection response\
- Valuable security insights

------------------------------------------------------------------------

## 🧾 Conclusion

The development and deployment of this project demonstrate our strong
commitment to applying **advanced computer vision techniques** to solve
real-world challenges.\
We are proud of the technical achievements and the practical value this
system provides to retailers seeking smarter security solutions.

------------------------------------------------------------------------

## 👤 Author

**Muhammed Mahmoud AlSayed Ibrahim**\
AI Engineer \| Computer Vision Specialist

------------------------------------------------------------------------

## ⭐ Contributions

Contributions, issues, and suggestions are always welcome!\
Feel free to open a pull request or start a discussion.

