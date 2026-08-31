import torch


if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

t1 = torch.tensor([1.0, 2.0, 3.0], device=device)
t3 = torch.dot(t1, t1)

print(device, t3)







