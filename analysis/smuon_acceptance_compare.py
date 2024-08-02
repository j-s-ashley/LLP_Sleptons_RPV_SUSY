import numpy as np
import yaml

# --- CSV ---
#og_file = "HEPData-ins1831504-v2-Smuon_acceptance.csv"
#np_og_data = np.genfromtxt(og_file, delimiter=',')
#og_data = np.ndarray.tolist(np_og_data)

# Removes header line from numpy array
#del(og_data[0])

# --- YAML ---
og_file = "analysis/HEPData-ins1831504-v2-Smuon_acceptance.yaml"
with open(og_file, 'r') as f:
	og_data = yaml.load(f, Loader=yaml.SafeLoader) 

# The YAML file lists acceptance values as 'dependent_variables'
# and mass and lifetime values as 'independent_variables'
og_acceptance_list = og_data.get('dependent_variables', {})[0].get('values')
og_mass_list = og_data.get('independent_variables', {})[0].get('values')
og_lifetime_list = og_data.get('independent_variables', {})[1].get('values')

og_data_list = []

for i, acc in enumerate(og_acceptance_list):
	list_entry = [acc, og_mass_list[i], og_lifetime_list[i]]
	og_data_list.append(list_entry)

#TODO All this section should be read in from RESULTS file
sparticle_mass = 400 #GeV
sparticle_lifetime = 0 #log_10(ns)
sparticle_acceptance = 0
uncertainty = 0

mass_bin = 0
lifetime_bin = 0
og_acceptance = 0

#for row in og_data:
#    if sparticle_mass <= row[0]:
#        mass_bin = row[0]
#        if sparticle_lifetime <= row[1]:
#            lifetime_bin = row[1]
#            og_acceptance = row[2]
#            break

#print('Mass bin =', mass_bin)
#print('Lifetime bin =', lifetime_bin)
#print('Acceptance in original paper =', og_acceptance)

print(og_data_list)
