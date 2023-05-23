import os
import gradio as gr
import numpy as np
from PIL import Image

def process_image(image):
    save_folder = "/desktop/uploads"
    os.makedirs(save_folder, exist_ok=True)
    save_path = os.path.join(save_folder, "uploaded_image.jpg")
    # Save the image array as a file
    image = image.astype(np.uint8)  # Convert to uint8
    pil_image = Image.fromarray(image)
    pil_image.save(save_path)

    return save_path

image_input = gr.inputs.Image(shape=(300, 200), label="Upload Image")
path_output = gr.outputs.Textbox(label="Image Path")

interface = gr.Interface(fn=process_image, inputs=image_input, outputs=path_output, title="Image Uploader")

interface.launch(debug=True)



