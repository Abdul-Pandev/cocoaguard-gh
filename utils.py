import numpy as np
import tensorflow as tf
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
from model_utils import EfficientNetPreprocessing


# ── Constants ─────────────────────────────────────────────────────
IMG_SIZE         = (224, 224)
OPTIMAL_THRESHOLD = 0.65
COCOA_THRESHOLD   = 0.65


# ── Model Loader ──────────────────────────────────────────────────
@st.cache_resource
def load_disease_model():
    return tf.keras.models.load_model(
        'model/phase2.keras',
        compile=False,
        custom_objects={
            'EfficientNetPreprocessing': EfficientNetPreprocessing
        }
    )


@st.cache_resource
def load_cocoa_checker():
    return tf.keras.models.load_model(
        'model/cocoa_checker.keras',
        compile=False
    )


# ── Preprocessor ──────────────────────────────────────────────────
def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Takes a PIL Image and returns a numpy array
    ready for model prediction.

    Raw pixels 0-255 are passed through without
    scaling — EfficientNetPreprocessing inside
    the model handles the scaling internally.
    """
    image     = image.convert('RGB')
    image     = image.resize(IMG_SIZE)
    img_array = np.array(image, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# ── Predictor ─────────────────────────────────────────────────────
def predict(model, processed_image: np.ndarray) -> dict:
    """
    Runs model inference and applies optimal threshold.

    Returns a dictionary with:
    - predicted_class: 'cssvd' or 'healthy'
    - confidence: float 0-100
    - probability: raw sigmoid output 0-1
    - cssvd_probability: probability of CSSVD 0-100
    - healthy_probability: probability of Healthy 0-100
    """
    raw_output  = model.predict(processed_image, verbose=0)
    probability = float(raw_output[0][0])

    if probability > OPTIMAL_THRESHOLD:
        predicted_class = 'healthy'
        confidence      = probability * 100
    else:
        predicted_class = 'cssvd'
        confidence      = (1 - probability) * 100

    return {
        'predicted_class':    predicted_class,
        'confidence':         confidence,
        'probability':        probability,
        'cssvd_probability':  (1 - probability) * 100,
        'healthy_probability': probability * 100
    }


# ── Recommendations ───────────────────────────────────────────────
def get_recommendation(predicted_class: str) -> dict:
    """
    Returns structured recommendation for the predicted class.
    """
    recommendations = {
        'healthy': {
            'summary': 'No signs of CSSVD detected.',
            'actions': [
                'Continue regular farm monitoring',
                'Maintain good farm sanitation',
                'Check surrounding trees periodically',
                'Keep records of farm health observations'
            ],
            'urgency': 'low'
        },
        'cssvd': {
            'summary': 'CSSVD infection detected on this plant.',
            'actions': [
                'Isolate the infected tree immediately',
                'Contact your agricultural extension officer',
                'Do not move plant material from infected area',
                'Monitor all surrounding trees closely',
                'Document the location and severity'
            ],
            'urgency': 'high'
        }
    }
    return recommendations[predicted_class]


# ── Charts ────────────────────────────────────────────────────────
def confidence_bar_chart(cssvd_prob: float, healthy_prob: float):
    """
    Horizontal bar chart showing probability for each class.
    """
    df = pd.DataFrame({
        'Class':       ['CSSVD', 'Healthy'],
        'Probability': [cssvd_prob, healthy_prob],
        'Color':       ['#E74C3C', '#2ECC71']
    })

    fig = px.bar(
        df,
        x='Probability',
        y='Class',
        orientation='h',
        color='Class',
        color_discrete_map={
            'CSSVD':   '#E74C3C',
            'Healthy': '#2ECC71'
        },
        title='Prediction Confidence Breakdown',
        range_x=[0, 100]
    )

    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#FAFAFA',
        xaxis_title='Confidence (%)',
        yaxis_title=''
    )

    return fig


def dataset_distribution_chart(cssvd_count: int, healthy_count: int):
    """
    Pie chart showing dataset class distribution.
    """
    fig = px.pie(
        names=['CSSVD', 'Healthy'],
        values=[cssvd_count, healthy_count],
        title='Dataset Class Distribution',
        color_discrete_sequence=['#E74C3C', '#2ECC71']
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#FAFAFA'
    )

    return fig


def training_history_chart(metric: str, train_values: list, val_values: list):
    """
    Line chart for training vs validation metrics.
    metric: 'Accuracy' or 'Loss'
    """
    epochs = list(range(1, len(train_values) + 1))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=epochs,
        y=train_values,
        mode='lines+markers',
        name=f'Training {metric}',
        line=dict(color='#2ECC71')
    ))

    fig.add_trace(go.Scatter(
        x=epochs,
        y=val_values,
        mode='lines+markers',
        name=f'Validation {metric}',
        line=dict(color='#3498DB')
    ))

    fig.update_layout(
        title=f'Training vs Validation {metric}',
        xaxis_title='Epoch',
        yaxis_title=metric,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#FAFAFA'
    )

    return fig
