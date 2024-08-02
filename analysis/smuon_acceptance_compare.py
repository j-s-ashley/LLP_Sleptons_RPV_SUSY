import numpy as np
import yaml

# Read OG data file
# TODO Replace relpath
og_file = "analysis/HEPData-ins1831504-v2-Smuon_acceptance.yaml"
with open(og_file, 'r') as f:
	og_data = yaml.load(f, Loader=yaml.SafeLoader) 

# The YAML file lists acceptance values as 'dependent_variables'
# and mass and lifetime values as 'independent_variables'
og_acceptance_dicts = og_data.get('dependent_variables', {})[0].get('values')
og_mass_dicts = og_data.get('independent_variables', {})[0].get('values')
og_lifetime_dicts = og_data.get('independent_variables', {})[1].get('values')

# Each entry in the above lists is a dictionary,
# we only need the values
og_acceptance_list = []
og_mass_list = []
og_lifetime_list = []

for a in og_acceptance_dicts:
	for key, value in a.items():
		 og_acceptance_list.append(value)

for m in og_mass_dicts:
	for key, value in m.items():
		og_mass_list.append(value)

for t in og_lifetime_dicts:
	for key, value in t.items():
		og_lifetime_list.append(value)

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

print(type(og_acceptance_list[0]))
