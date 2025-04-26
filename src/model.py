import torch.nn as nn


class ThreatDetectionModel(nn.Module):
    def __init__(self):
        super(ThreatDetectionModel, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(7, 128),  # First fully connected layer
            nn.ReLU(),  # ReLU activation
            nn.Linear(128, 64),  # Second fully connected layer
            nn.ReLU(),  # ReLU activation
            nn.Linear(64, 1),  # Third fully connected layer
            nn.Sigmoid()  # Sigmoid activation for binary classification
    )

    def forward(self, x):
        return self.model(x)