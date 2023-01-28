import torch
import torch.nn as nn
import torch.nn.functional as F

class pac_net(nn.Module):
    def __init__(self):
        super(pac_net, self).__init__()
        self.layer1 = torch.nn.Conv2d(in_channels=12, out_channels=24, kernel_size=3, padding=0)
        self.layer2 = torch.nn.Conv2d(in_channels=24, out_channels=12, kernel_size=3, padding=1)
        self.max_pool = torch.nn.MaxPool2d(2, 2)
        self.layer3 = torch.nn.Conv2d(in_channels=12, out_channels=6, kernel_size=3, padding=1)
        self.layer4 = torch.nn.Conv2d(in_channels=6, out_channels=1, kernel_size=2, padding=1)
        self.flatten = torch.nn.Flatten()
        self.linear = torch.nn.Linear(14, 10)

        self.outputLayer = torch.nn.Linear(10, 8)

        self.activationFunc = torch.nn.Tanh

        self.batchNorm1 = torch.nn.BatchNorm2d(24)
        self.batchNorm2 = torch.nn.BatchNorm2d(12)
        self.batchNorm3 = torch.nn.BatchNorm2d(6)
        self.batchNorm4 = torch.nn.BatchNorm2d(1)

    def forward(self, nn_input):
        # Layer 1
        output_1 = self.layer1(nn_input)
        output_1 = self.batchNorm1(output_1)
        output_1 = self.activationFunc(output_1)

        # Layer 2
        output_2 = self.layer2(output_1)
        output_2 = self.batchNorm2(output_2)
        output_2 = self.activationFunc(output_2)
        output_2 = self.max_pool(output_2)

        # Layer 3
        output_3 = self.layer3(output_2)
        output_3 = self.batchNorm3(output_3)
        output_3 = self.activationFunc(output_3)

        # Layer 4
        output_4 = self.layer4(output_3)
        output_4 = self.batchNorm4(output_4)
        output_4 = self.activationFunc(output_4)
        output_4 = self.max_pool(output_4)

        # Flatten (Layer 5)
        output_5 = self.flatten(output_4)

        # Linear (Layer 6)
        output_6 = self.linear(output_5)

        # Output
        output = self.outputLayer(output_6)
        output = F.softmax(output, dim=1)

        return output
