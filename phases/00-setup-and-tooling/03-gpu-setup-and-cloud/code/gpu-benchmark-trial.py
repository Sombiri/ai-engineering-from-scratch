import torch
import time



def synchronize_device(device):
    if device == "cuda":
        torch.cuda.synchronize()
    elif device == "mps":
        torch.mps.synchronize()

# the function is used to benchmark gpu. 
# the condition statement check to know which accelerator is available.
def benchmark_gpu():
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    print(device)

    size = 4000
    
    cpu1 = torch.randn(size, size) 
    cpu2 = torch.randn(size, size)

    _ = cpu1 @ cpu2 
        
    start_time = time.perf_counter()
    result_cpu = cpu1 @ cpu2
    cpu_time = time.perf_counter() - start_time
    print(f"CPU time: {cpu_time:.6f} seconds")

    if device == "cpu":
        print("No accelerator available.")
        return
        
    accelerator1 = cpu1.to(device)
    accelerator2 = cpu2.to(device)
    
    _ = accelerator1 @ accelerator2 #untimed accelerator warm up


    synchronize_device(device)
    start_time = time.perf_counter()
    result_accelerator = accelerator1 @ accelerator2
    synchronize_device(device)
    accelerator_time = time.perf_counter() - start_time
    
    print(f"Accelerator time: {accelerator_time:.6f} seconds")
    print(f"SpeedUp: {cpu_time/accelerator_time:.2f}x")
    print(f"Result_device: {result_accelerator.device}")

benchmark_gpu()