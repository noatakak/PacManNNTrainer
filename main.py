import numpy as np
import pandas as pd
import torch

from pacNet import pac_net


def main():
    print(torch.cuda.get_device_name())
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"CUDA version: {torch.version.cuda}")


    pacNet = pac_net()
    pacNet.to(device)
    print("Number of Parameters: " + str(sum(p.numel() for p in pacNet.parameters() if p.requires_grad)))
    torch.save(pacNet, "savedModels/pacMODEL.pt");
    temp = pacNet.parameters()

    print("Hello World")

if __name__ == '__main__':
    main()

