import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
#self & init: https://stackoverflow.com/questions/625083/what-init-and-self-do-on-python
    def __init__(self):
        #super: https://forums.fast.ai/t/why-super-init/20390/2
        super(Net, self).__init__()
        self.fc1 = nn.Linear(9, 27)
        self.dropout1 = nn.Dropout(p=0.9, inplace=False)
        self.fc2 = nn.Linear(27, 81)
        #inplace: https://stackoverflow.com/questions/58589128/what-is-the-meaning-of-in-place-in-dropout
        self.dropout2 = nn.Dropout(p=0.8, inplace=False)
        self.fc3 = nn.Linear(81, 27)
        self.dropout3 = nn.Dropout(p=0.8, inplace=False)
        self.fc4 = nn.Linear(27, 18)
        self.dropout4 = nn.Dropout(p=0.8, inplace=False)
        self.fc5 = nn.Linear(18, 9)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        #dropout example: https://medium.com/@zhang_yang/scaling-in-neural-network-dropout-layers-with-pytorch-code-example-11436098d426
        #x = self.dropout1(x)
        x = F.relu(self.fc2(x))
        #x = self.dropout2(x)
        x = F.relu(self.fc3(x))
        #x = self.dropout3(x)
        x = F.relu(self.fc4(x))
        #x = self.dropout4(x)
        x = self.fc5(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features