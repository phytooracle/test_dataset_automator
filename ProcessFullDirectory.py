#!/usr/bin/env python3
"""
Author : Jeffrey Demieville
Date   : 2023-06-20
Purpose: Test Dataset Generation
"""

import os
import sys
import argparse
import subprocess as sp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='ProcessFullDirectory',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-p',
                        '--path',
                        help='path containing level 0 data to process',
                        type=str,
                        required=True)
                        # Example: /iplant/home/shared/phytooracle/season_14_sorghum_yr_2022/level_0/scanner3DTop

    parser.add_argument('-u',
                        '--user',
                        help='User account to use for data transfer',
                        type=str,
                        required=True)
                        # Example: jdemieville

    parser.add_argument('-n',
                        '--number',
                        help='Number of measurements to include in test dataset',
                        type=str,
                        required=True)
                        # Example: 90
                        
    return parser.parse_args()


#-------------------------------------------------------------------------------
def get_file_list(data_path):
    '''
    List all files in path
    
    Input:
        - data_path: path to the input data on CyVerse data store
    Output: 
        - List of files contained within data_path
    '''
    result = sp.run(f'ils {data_path}', stdout=sp.PIPE, shell=True)
    files = result.stdout.decode('utf-8').split('\n')

    return files


#-------------------------------------------------------------------------------
def generate_test_filename(infile):
    '''
    Generate a filename for the test dataset output.
    
    Input:
        - infile: input filename string
    Output: 
        - outfile: output filename string
    '''
    split_filename = infile.split('-')
    #split_filename[1] = "22" + split_filename[1][2:] #replace first two characters of year with 22
    split_filename[3] = split_filename[3][:4] + "00" #replace hour component
    split_filename[4] = "00" #replace minute component
    split_filename[5] = "00" #replace second components
    split_filename[6] = "000" + split_filename[6][3:-7] #replace millisecond component, remove extension
    outfile = split_filename[0] + '-' + split_filename[1] + '-' + split_filename[2] + '-' + split_filename[3] + '-' + split_filename[4] + '-' + split_filename[5] + '-' + split_filename[6]

    return outfile
    
    
#-------------------------------------------------------------------------------
def run_automator(input_file, username, output_filename, number):
    '''
    Run the automator
    
    Input:
        - input_file: full name of the input file, including extension
        - username: username to use for file download and upload
        - ouput_filename: name to use for the output test dataset, excluding extension
        - number: number of directories to include in the test dataset
    Output: 
        - Uploads test dataset to CyVerse datastore
    '''
    result = sp.run(["./automator.sh", "-p", input_file, "-u", username, "-t", output_filename, "-n", number])
    files = result.stdout.decode('utf-8').split('\n')

    return files


#-------------------------------------------------------------------------------
def main():
    print("getting args")
    args = get_args()
    
    print("getting file list")
    files = get_file_list(args.path)
    print("file list\n", files)
   
    # Iterate through all dates within this season
    for filename in files:
        print("input filename: ", filename)
        if filename.endswith(".tar.gz"):
            outfile = generate_test_filename(filename)
            print("outfile", outfile)
            run_automator(filename, args.user, outfile, args.number)


# --------------------------------------------------
if __name__ == '__main__':

    main()
