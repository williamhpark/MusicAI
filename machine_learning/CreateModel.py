import SetupModel as sm
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import MNIST
import os


dataset = MNIST(root='data/', train=True, transform=transforms.ToTensor())


filename = 'Model.pt'


device = sm.get_default_device()
model = sm.MnistModel(sm.input_size, sm.hidden_size,
                      output_size=sm.num_classes)
sm.to_device(model, device)


def split_indices(size, valid_pct):
    n_val = int(size*valid_pct)
    indexList = np.random.permutation(size)
    return indexList[n_val:], indexList[:n_val]


train_indices, valid_indices = split_indices(len(dataset), valid_pct=0.2)

train_sampler = SubsetRandomSampler(train_indices)
train_dl = DataLoader(dataset, sm.batch_size, sampler=train_sampler)

valid_sampler = SubsetRandomSampler(valid_indices)
valid_dl = DataLoader(dataset, sm.batch_size, sampler=valid_sampler)

train_dl = sm.DeviceDataLoader(train_dl, device)
valid_dl = sm.DeviceDataLoader(valid_dl, device)

# Train model twice
print(f'First series with learning rate: {sm.learning_rate1}')
losses1, metrics1 = sm.fit(sm.epochs1, sm.learning_rate1, model, F.cross_entropy,
                           train_dl, valid_dl, metric=sm.accuracy)

print(f'Second series with learning rate: {sm.learning_rate2}')
losses2, metrics2 = sm.fit(sm.epochs2, sm.learning_rate2, model, F.cross_entropy,
                           train_dl, valid_dl, metric=sm.accuracy)

# Save model parameters
torch.save(model.state_dict(), filename)

if os.path.isfile(filename):
    print(f"Model saved as {filename}.")
else:
    print("Unable to save model.")
