# pipetting_sim/simulator.py
import pandas as pd

class PipettingSimulator:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.plate_type = '96'  # default; could be param

    def optimize_transfers(self):
        # Dummy example logic
        self.df['Transfers'] = self.df['Volume_uL'].apply(self._simulate_transfer)
        return self.df

    def _simulate_transfer(self, volume):
        max_vol = 200  # max pipette volume
        n_transfers = -(-volume // max_vol)  # ceiling division
        return f\"{n_transfers} transfer(s) of ≤ {max_vol} uL\"