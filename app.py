import streamlit as st
import torch
from PIL import Image
import numpy as np
import cv2
import tempfile

# Définir le chemin absolu vers le répertoire YOLOv5 et les poids du modèle
yolov5_path = '/Users/tarekatbi/Desktop/ML/env/yolov5'
weights_path = '/Users/tarekatbi/Desktop/ML/env/yolov5/runs/train/exp13/weights/best.pt'

# Charger le modèle YOLOv5 avec les poids entraînés
model = torch.hub.load(yolov5_path, 'custom', path=weights_path, source='local')

st.title("Détection de Panneaux de Signalisation")
st.write("Téléchargez une image ou une vidéo pour détecter les panneaux de signalisation.")

uploaded_file = st.file_uploader("Choisissez une image ou une vidéo...", type=["jpg", "jpeg", "png", "mp4", "avi", "mov"])

def detect_in_image(image):
    st.write("Traitement de l'image...")
    img = np.array(image)
    st.write("Image convertie en tableau NumPy.")
    results = model(img, size=640, conf=0.25)  # Augmenter la taille de l'image et ajuster le seuil de confiance
    st.write("Prédictions effectuées.")
    results_img = results.render()[0]
    results_pil = Image.fromarray(results_img)
    st.write("Résultats rendus en image PIL.")
    return results_pil

def detect_in_video(video_path):
    st.write("Lecture de la vidéo...")
    vid_cap = cv2.VideoCapture(video_path)
    if not vid_cap.isOpened():
        st.write("Erreur: Impossible de lire la vidéo.")
        return None
    
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    temp_video_path = temp_video.name
    temp_video.close()
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(vid_cap.get(cv2.CAP_PROP_FPS))
    width = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))
    
    st.write(f"Début du traitement vidéo... FPS: {fps}, Width: {width}, Height: {height}")
    frame_count = 0
    while True:
        ret, frame = vid_cap.read()
        if not ret:
            break

        st.write(f"Traitement de la frame {frame_count + 1}...")

        # Prétraiter la frame pour améliorer la qualité
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (width, height))
        
        # Appliquer le modèle
        results = model(frame, size=640, conf=0.25)  # Augmenter la taille de l'image et ajuster le seuil de confiance
        st.write(f"Résultats bruts pour la frame {frame_count + 1}: {results.xyxy[0]}")
        
        results_frame = results.render()[0]
        results_frame = cv2.cvtColor(results_frame, cv2.COLOR_RGB2BGR)
        out.write(results_frame)
        frame_count += 1
        if frame_count % 10 == 0:
            st.write(f"Frames traitées : {frame_count}")
    
    vid_cap.release()
    out.release()
    st.write(f"Traitement terminé. Total des frames traitées : {frame_count}")
    return temp_video_path

if uploaded_file is not None:
    if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption='Image Téléchargée.', use_column_width=True)
        st.write("Détection en cours...")
        results_pil = detect_in_image(image)
        st.image(results_pil, caption='Résultats de la Détection', use_column_width=True)
    elif uploaded_file.type in ["video/mp4", "video/avi", "video/mov"]:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        st.video(tfile.name)
        st.write("Détection en cours...")
        output_video_path = detect_in_video(tfile.name)
        if output_video_path:
            st.video(output_video_path)
            st.write("Télécharger la vidéo traitée :")
            with open(output_video_path, 'rb') as f:
                st.download_button('Télécharger la vidéo', f, file_name='video_traitee.mp4')