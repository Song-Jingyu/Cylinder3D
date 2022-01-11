import os
import yaml

raw_dataset_dir = '/media/sdb1/shared_data'
dataset_dir = './carla_data'
sequence_dir = os.path.join(dataset_dir, 'sequences')
sequence_ref_dict = {}
is_cylindrical = True
sequence_ref_dict['is_cylindrical'] = is_cylindrical




os.system(f'ls {raw_dataset_dir}')

# make directory

os.system(f'mkdir {dataset_dir}')
os.system(f'mkdir {sequence_dir}')

if is_cylindrical:
    coordinate = 'cylindrical'
else:
    coordinate = 'cartesian'

# os.system(os.path.join(raw_dataset_dir, 'Train'))
sequences = sorted(os.listdir(os.path.join(raw_dataset_dir, 'Train')))
for i in range(len(sequences)):
    sequence_ref_dict[i] = sequences[i]
    
    os.system(f'ln -s {raw_dataset_dir}/Train/{sequences[i]}/{coordinate} {os.path.join(sequence_dir, str(i).zfill(2))}')
    # generate soft links


print(sequence_ref_dict)
with open(os.path.join(dataset_dir, 'carla_seq.yaml'), 'w') as outfile:
    yaml.dump(sequence_ref_dict, outfile)