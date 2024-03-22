import re

replace_dict = {
    'Torchinsky2014ASymmetries': 'torchinsky_low_2014',
    'Fichera2020SecondSymmetry': 'fichera_second_2020',
    'Li2022High-pressureTaAs': 'li_high-pressure_2022',
    'Shan2021GiantEngineering': 'shan_gian_2021',
    'Boyd1992NonlinearOptics': 'boyd',
    'Birss1966SymmetryMagnetism': 'birss',
    'Petersen2006Nonlinear7': 'petersen_nonlinear_2006',
    'Fichera2023Light-inducedSemiconductor': 'camn2bi2',
    'Argibay2010AsymmetricEnvironment': 'argibay_asymmetric_2010',
    'Ducuing1963ObservationCrystals': 'ducuing_observation_1963',
}

with open('ch4.tex', 'r') as fh:
    lines = fh.readlines()

for i, line in enumerate(lines):
    match = re.findall('cite.{.*?}', line)
    if match:
        print(match)

commands = []
for k, v in replace_dict.items():
    commands.append(f'sed -i "s/{k}/{v}/g" ch4.tex')
print('\n'.join(commands))
