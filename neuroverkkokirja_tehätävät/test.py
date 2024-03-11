import torch

print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))
# torch.set_default_tensor_type('torch.cuda.FloatTensor')
while True:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    x = torch.tensor([10.0, 20.0, 30.0], device=device)
    y = torch.tensor([1.0, 2.0, 3.0], device=device)
    z = (x + y)
    #  print(z)