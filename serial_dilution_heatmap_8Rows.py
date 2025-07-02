import random
import matplotlib.pyplot as plt
import numpy as np

class Pipette:
    def __init__(self, max_volume=200, error_rate=0.01):
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

def simulate_full_plate_vertical_dilution(start_conc=100.0, dilution_factor=2.0, transfer_volume=100.0):
    plate = np.zeros((8, 12))  # 96-well plate (8 rows x 12 columns)
    pipette = Pipette()

    for col in range(12):  # Columns 1–12
        plate[0, col] = start_conc  # Start each column with full concentration at Row A
        for row in range(1, 8):  # Rows B–H
            pipette.aspirate(transfer_volume)
            pipette.dispense()
            plate[row, col] = plate[row - 1, col] / dilution_factor

    return plate

def plot_heatmap(plate_data, colormap="plasma"):
    fig, ax = plt.subplots(figsize=(12, 6))
    cax = ax.imshow(plate_data, cmap=colormap, interpolation="nearest")

    # Tick labels
    ax.set_xticks(np.arange(12))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels([str(i+1) for i in range(12)])
    ax.set_yticklabels(["A", "B", "C", "D", "E", "F", "G", "H"])

    # Add value labels
    for i in range(8):
        for j in range(12):
            val = plate_data[i, j]
            label = f"{val:.1f}" if val > 0 else ""
            color = "white" if val > 50 else "black"
            ax.text(j, i, label, ha="center", va="center", color=color, fontsize=8)

    ax.set_title(f"Serial Dilution Down Columns (Colormap: {colormap})")
    fig.colorbar(cax, label="Concentration Units")
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plate = simulate_full_plate_vertical_dilution()
    plot_heatmap(plate, colormap="plasma")  # Try: 'viridis', 'inferno', 'coolwarm', 'Blues'
