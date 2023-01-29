import numpy as np
import pandas as pd
import torch

from pacNet import pac_net


def main():
    #print(torch.cuda.get_device_name())
    #device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    #print(f"CUDA version: {torch.version.cuda}")


    pacNet = torch.load("savedModels/pacMODEL.pt", map_location=torch.device('cpu'))
    #pacNet.to(device)
    print("Number of Parameters: " + str(sum(p.numel() for p in pacNet.parameters() if p.requires_grad)))

    layer1Param = pacNet.layer1.weight
    layer1bias = pacNet.layer1.bias
    layer1Weights = torch.Tensor.detach(pacNet.layer1.weight.data).numpy()

    # torch.save(pacNet, "savedModels/pacMODEL.pt");

    print("Hello World")

if __name__ == '__main__':
    main()

