import pandas as pd
from pipetting_sim.simulator import PipettingSimulator

def test_optimize_transfers():
    df = pd.DataFrame({'Sample': ['A'], 'Volume_uL': [250]})
    sim = PipettingSimulator(df)
    df2 = sim.optimize_transfers()
    assert 'Transfers' in df2.columns
    assert '2 transfer(s)' in df2['Transfers'][0]
