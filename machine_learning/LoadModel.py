import torch
from torch.utils import data
import torchvision
import setupModel as sm
from torchvision.datasets import MNIST
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import os
model_path = os.path.dirname(os.path.realpath(__file__))

# Load Model

device = sm.get_default_device()
model = sm.MnistModel(sm.input_size, sm.hidden_size, sm.num_classes)
model.load_state_dict(torch.load(model_path+'\Model.pt',map_location=device))
# Remove map_location above and uncomment below for GPU loading
# model.to(device)


"""FOR TESTING"""

# dataset = MNIST(root='machine_learning/data/',train = False,transform=transforms.ToTensor())

# def displayImage(img,model):
#     xb = img.unsqueeze(0)
#     yb = model(xb)
#     _, preds = torch.max(yb,dim=1)
#     return preds[0].item()

# img,label = dataset[0]
# plt.imshow(img[0],cmap='gray')
# plt.suptitle(f'Prediction: {displayImage(img,model)}')
# plt.show()
