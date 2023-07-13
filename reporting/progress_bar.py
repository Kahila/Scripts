from tqdm import tqdm
import time

# show loading progress
def progress_bar():
    for i in tqdm (range (100), desc="Loading..."):
        time.sleep(0.1)
        pass