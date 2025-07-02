import random

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


def simulate_serial_dilution(start_conc=100.0, dilution_factor=2.0, wells=12, transfer_volume=100.0, pipette_size=200):
    plate = [0.0] * wells
    plate[0] = start_conc  # First well has stock concentration

    pipette = Pipette(pipette_size)

    print("Simulating 1:2 serial dilution across 12 wells (Row A)...\n")
    print(f"Well A1: {plate[0]:.2f} units (starting concentration)")

    for i in range(1, wells):
        # Aspirate from previous well
        aspirated = pipette.aspirate(transfer_volume)

        # Dispense into current well
        transferred = pipette.dispense()

        # Mix (simplified assumption)
        plate[i] = plate[i-1] / dilution_factor

        print(f"Well A{i+1}: {plate[i]:.2f} units (diluted)")

    return plate


if __name__ == "__main__":
    simulate_serial_dilution()
