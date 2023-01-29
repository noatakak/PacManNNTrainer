import numpy as np
import pandas as pd
import torch

import os
import subprocess
import cupy as cp

import time

from pacNet import pac_net


def main():
    print(torch.cuda.get_device_name())
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"CUDA version: {torch.version.cuda}")




    # torch.save(pacNet, "savedModels/pacMODEL.pt");

    handle = subprocess.Popen("java -cp C:\\Users\\noata\\PycharmProjects\\PacManNNTrainer\\javaGame\\target\\spring-2020-1.0-SNAPSHOT-jar-with-dependencies.jar Spring2020Main ")
    time.sleep(20)
    handle.terminate
    print("Hello World")

if __name__ == '__main__':
    main()

