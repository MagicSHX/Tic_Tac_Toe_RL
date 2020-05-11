import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(9, 27)
        self.fc2 = nn.Linear(27, 81)
        self.dropout2 = nn.Dropout(p=0.8, inplace=False)
        self.fc3 = nn.Linear(81, 27)
        self.dropout3 = nn.Dropout(p=0.8, inplace=False)
        self.fc4 = nn.Linear(27, 18)
        self.dropout4 = nn.Dropout(p=0.8, inplace=False)
        self.fc5 = nn.Linear(18, 9)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.fc5(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features