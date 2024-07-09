import gradio as gr
import numpy as np

def img_flip(img):
    # return np.flip(img, axis=0)
    return np.flip(img, axis=1)


imgflip = gr.Interface(img_flip, inputs=['image'], outputs=['image'])
imgflip.launch(share=True)