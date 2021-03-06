# By Bobby Richter
# License MIT
# :)

import os
import subprocess

source_directory = './'
dest_directories = {
  'ogg': './output/ogg',
  'mp3': './output/mp3'
}

ignore_files = [
  '.DS_Store'
]

ignore_directories = [
  'output',
  '.git'
]

accepted_input_suffixes = [
  '.wav'
]

os.listdir
input_files = []

for root_path, directories, files in os.walk(source_directory, topdown=True):
  directories[:] = [d for d in directories if d not in ignore_directories]
  root_path = root_path[len(source_directory):]
  input_files += [{'path': root_path, 'file': f} for f in files if f not in ignore_files and len([suffix for suffix in accepted_input_suffixes if f.endswith(suffix)]) > 0]

  print(input_files)

for input_file_description in input_files:
  input_path = input_file_description['path']
  input_file = input_file_description['file']

  for output_type in dest_directories:
    full_input_path = source_directory + '/' + input_path + '/' + input_file
    output_file = input_file + '.' + output_type
    dest_directory = dest_directories[output_type] + '/' + input_path
    full_output_path = dest_directory + '/' + output_file

    if not os.path.exists(dest_directory):
      os.makedirs(dest_directory)

    print('Processing ' + full_input_path + ' -> ' + full_output_path)
    subprocess.call(['ffmpeg', '-i', full_input_path, full_output_path])

