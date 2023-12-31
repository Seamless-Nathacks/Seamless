from brainflow.board_shim import BoardShim, BoardIds, BrainFlowInputParams
from brainflow.data_filter import DataFilter, FilterTypes
import numpy as np
import matplotlib.pyplot as plt
import time


params = BrainFlowInputParams()
params.serial_port = "COM3" #May be a unique value, have to check on your own device once connected to Open BCI
board_id = BoardIds.GANGLION_BOARD.value
print(board_id)

# Initialize the board
board = BoardShim(board_id, params)
board.prepare_session()

# Start data streaming
board.start_stream()

# Initialize variables for data collection
time.sleep(5)  # Wait for 5 seconds to collect data
sampling_rate = board.get_sampling_rate(board_id)
data = []

# Read and plot data for 10 seconds (adjust as needed)
duration = 10  # in seconds
start_time = time.time()
while time.time() - start_time < duration:
    data_chunk = board.get_current_board_data(250)  # Get 250 samples
    data.extend(data_chunk[0])

# Stop the stream and release resources
board.stop_stream()
board.release_session()

# Visualize the data using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(data)
plt.title('EEG Data from OpenBCI')
plt.xlabel('Sample')
plt.ylabel('Voltage')
plt.show()
