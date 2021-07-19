import torch
import SetupModel as sm

# Load Model

device = sm.get_default_device()
model = sm.MnistModel(sm.input_size, sm.hidden_size, sm.num_classes)
model.load_state_dict(torch.load('Model.pt'))
model.to(device)
