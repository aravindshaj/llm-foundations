import platform
import sys

import torch


def main() -> None:
    print("=== Python ===")
    print(sys.version)
    print()

    print("=== System ===")
    print("Platform:", platform.platform())
    print("Machine:", platform.machine())
    print()

    print("=== PyTorch ===")
    print("Torch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("CUDA device count:", torch.cuda.device_count())
        print("Current device:", torch.cuda.current_device())
        print("Device name:", torch.cuda.get_device_name(0))

        x = torch.randn(2000, 2000, device="cuda")
        y = x @ x
        print("CUDA matmul OK:", y.shape)
    else:
        print("No CUDA GPU detected. This is expected on a MacBook Air.")

        x = torch.randn(1000, 1000)
        y = x @ x
        print("CPU matmul OK:", y.shape)


if __name__ == "__main__":
    main()
