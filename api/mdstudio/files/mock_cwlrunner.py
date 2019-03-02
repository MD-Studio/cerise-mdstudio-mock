#!/usr/bin/env python3

import json
import os
from pathlib import Path
import shutil
import sys


# get directories
this_dir = Path(__file__).parent
data_dir = this_dir / 'dummy_data'
work_dir = Path(os.getcwd())

# copy dummy output in place
dummy_data = {
        'gromitout': 'gromit.out',
        'gromiterr': 'gromit.err',
        'gromacslog2': '02-PBC.log',
        'gromacslog3': '03-EMv.log',
        'gromacslog4': '04-SOLVATION.log',
        'gromacslog5': '05-EMs.log',
        'gromacslog6': '06-PR-NVT-1.log',
        'gromacslog7': '07-NPT-1.log',
        'gromacslog8': '08-MD-PRE.log',
        'gromacslog9': '09-MD.log',
        'trajectory': 'protein-MD.part0001.trr',
        'gro': 'protein-sol.gro',
        'ndx': 'protein-sol.ndx',
        'top': 'protein-sol.top',
        'mdp': 'md-prod-out.mdp',
        'energy_edr': 'protein-MD.part0001.edr',
        'energy_dataframe': 'energy.ene',
        'energyout': 'getEnergy.out',
        'energyerr': 'getEnergy.err',
        'decompose_dataframe': 'decompose.ene',
        'decompose_err': 'decompose.err',
        'decompose_out': 'decompose.out'}

for file_name in dummy_data.values():
    shutil.copy2(data_dir / file_name, work_dir)

# print stderror
print('Saved mock results to {}'.format(work_dir), stream=sys.stderr)

# print stdout
out_dict = dict()
for variable, file_name in dummy_data.items():
    file_dict = {
            'class': 'File',
            'location': 'file://{}'.format(str(work_dir / file_name))}
    out_dict[variable] = file_dict

print(json.dumps(out_dict))
