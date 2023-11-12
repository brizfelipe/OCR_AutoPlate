# src/model/ocr_model.py

import torch
import torch.nn as nn

class OCRModel(nn.Module):
    def __init__(self):
        super(OCRModel, self).__init__()
        # Defina a arquitetura do seu modelo aqui

    def forward(self, x):
        # Implemente a lógica de forward do seu modelo aqui
        return x

    @staticmethod
    def load_model(model_path):
        model = OCRModel()
        model.load_state_dict(torch.load(model_path))
        model.eval()
        return model
