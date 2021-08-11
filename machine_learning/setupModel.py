import torch
import numpy as np
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
import torch.nn as nn
import torch.nn.functional as F

# Hyperparameters
input_size = 28*28
hidden_size = 64
num_classes = 10
batch_size = 100
learning_rate1 = 0.5
learning_rate2 = 0.1
epochs1 = 5
epochs2 = 10

# Setup GPU


def get_default_device():
    if torch.cuda.is_available():
        return torch.device('cuda')
    return torch.device('cpu')


def to_device(data, device):
    if isinstance(data, (list, tuple)):
        return [to_device(x, device) for x in data]
    return data.to(device, non_blocking=True)


# Setup Model


class MnistModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        # Hidden Layer
        self.linear1 = nn.Linear(input_size, hidden_size)
        # Output Layer
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, inp):
        # Flatten 100 by 1 by 28 by 28 Tensor to 100 by 784 Tensor
        inp = inp.view(inp.size(0), -1)
        # Pass through hidden layer
        out = self.linear1(inp)
        # Zero any negative values
        out = F.relu(out)
        # Pass through output layer
        out = self.linear2(out)
        return out


# Setup Dataloader


class DeviceDataLoader():
    def __init__(self, dl, device):
        self.dl = dl
        self.device = device

    def __iter__(self):
        for b in self.dl:
            yield to_device(b, self.device)

    def __len__(self):
        return len(self.dl)

# Setup Stochastic Gradient Descent Optimizer


def loss_batch(model, loss_func, xb, yb, opt=None, metric=None):
    # Generate predictions
    preds = model(xb)
    # Calculate Loss
    loss = loss_func(preds, yb)

    if opt is not None:
        loss.backward()
        opt.step()
        opt.zero_grad()
    metric_result = None
    if metric is not None:
        metric_result = metric(preds, yb)
    return loss.item(), len(xb), metric_result


def evaluate(model, loss_fn, valid_dl, metric=None):
    with torch.no_grad():
        results = [loss_batch(model, loss_fn, xb, yb, metric=metric)
                   for xb, yb in valid_dl]

        losses, nums, metrics = zip(*results)
        total = np.sum(nums)
        avg_loss = np.sum(np.multiply(losses, nums))/total
        avg_metric = None
        if metric is not None:
            avg_metric = np.sum(np.multiply(metrics, nums))/total
    return avg_loss, total, avg_metric


def fit(epochs, lr, model, loss_fn, train_dl, valid_dl, metric=None, opt_fn=None):
    losses, metrics = [], []

    if opt_fn is None:
        opt_fn = torch.optim.SGD
    opt = opt_fn(model.parameters(), lr=lr)

    for epoch in range(epochs):
        for xb, yb in train_dl:
            loss, _, _ = loss_batch(model, loss_fn, xb, yb, opt)

        result = evaluate(model, loss_fn, valid_dl, metric)
        val_loss, total, val_metric = result

        losses.append(val_loss)
        metrics.append(val_metric)

        if metric is None:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {val_loss:.4f}')
        else:
            print(
                f'Epoch [{epoch+1}/{epochs}], Loss: {val_loss:.4f}, {metric.__name__}: {val_metric:.4f}')
    return losses, metrics


# Calculates accuracy of model by comparing predictions with actual answers
def accuracy(outputs, labels):
    _, preds = torch.max(outputs, dim=1)
    return torch.sum(preds == labels).item()/len(preds)
