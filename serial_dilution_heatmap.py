import random
import matplotlib.pyplot as plt
import numpy as np

class Pipette:
    def __init__(self, max_volume, error_rate=0.01):
        self.max_volume = max_volume
        self.error_rate = error_rate
        self.current_volume = 0

    def aspirate(self, volume):
        if volume > self.max_volume:
            raise ValueError("Volume exceeds pipette capacity.")
        error = volume * random.uniform(-self.error_rate, self.error_rate)
        self.current_volume = volume + error
        return self.current_volume

    def dispense(self):
        dispensed_volume = self.current_volume
        self.current_volume = 0
        return dispensed_volume

def simulate_serial_dilution(start_conc=100.0, dilution_factor=2.0, transfer_volume=100.0):
    plate = np.zeros((8, 12))  # 96-well plate: 8 rows x 12 cols
    pipette = Pipette(max_volume=200)

    # Start dilution in Row A (index 0)
    row = 0
    plate[row, 0] = start_conc

    for col in range(1, 12):
        pipette.aspirate(transfer_volume)
        pipette.dispense()
        plate[row, col] = plate[row, col - 1] / dilution_factor

    return plate

def plot_heatmap(plate_data):
    fig, ax = plt.subplots(figsize=(12, 6))
    cax = ax.imshow(plate_data, cmap="Reds", interpolation="nearest")

    # Customize axis
    ax.set_xticks(np.arange(12))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels([str(i+1) for i in range(12)])
    ax.set_yticklabels(["A", "B", "C", "D", "E", "F", "G", "H"])

    # Label each cell with value
    for i in range(8):
        for j in range(12):
            text = f"{plate_data[i, j]:.1f}" if plate_data[i, j] > 0 else ""
            ax.text(j, i, text, ha="center", va="center", color="white" if plate_data[i,j] > 50 else "black")

    ax.set_title("Serial Dilution in 96-Well Plate (Row A)")
    fig.colorbar(cax, label="Concentration Units")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plate = simulate_serial_dilution()
    plot_heatmap(plate)
