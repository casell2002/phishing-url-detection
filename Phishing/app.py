# -*- coding: utf-8 -*-
# Author: HO HOANG AN - DAO KHAC VUONG
# Date created: 12/10/2023 3:21 PM

import numpy as np
import pickle
import gradio as gr
from feature import FeatureExtraction

file = open("pickle/model.pkl", "rb")
gbc = pickle.load(file)
file.close()


def predict(URL):
    obj = FeatureExtraction(URL)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)

    y_pro_phishing = 1 - gbc.predict_proba(x)[0, 0]

    # y_pro_non_phishing = gbc.predict_proba(x)[0, 1]
    # print(y_pro_non_phishing, y_pro_phishing)

    pred = "It is {0:.2f}% safe to go".format(y_pro_phishing * 100)

    return pred


# Use HTML formatting to make the text bigger and centered
description_html = '<div style="font-size:24px;text-align:center;">Phishing URL Detection</div>'

iface = gr.Interface(fn=predict, inputs="text", outputs=["text"], description=description_html)
iface.launch()
