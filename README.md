# Test Dataset Automator
This script is used to create test datasets for scans of different sensors such as RGD, 3D, IR etc. . 

## Usage - Python Script
Use the python script when you want to recursively generate test datasets for all scans within a directory.
```python3 ProcessFullDirectory.py -p <path containing multiple scan dates> -u <netid> -n <#>```

### Flags - Python Script
-p: This flag is used to specify the **source path** containing scan directories.<br />
-- Example: /iplant/home/shared/phytooracle/season_14_sorghum_yr_2022/level_0/scanner3DTop would permit processing of all datasets within this directory.<br />
-n: This flag should be followed by the number of sub-directories from the example scan that should be included in the test dataset <br />
-u: This flag should be followed by the username of the user running this script. Used for accessing the xdisk  <br />

## Usage - Shell Script
```./automator.sh -p [pathname] -u [username] -t [test_dataset_name(DON'T INCLUDE .tar.gz)] -n [number_of_files]```

### Flags - Shell Script
-p: This flag is used to specify the **source path** for the example scan used to create the test dataset.<br />
-n: This flag should be followed by the number of sub-directories from the example scan that should be included in the test dataset <br />
-u: This flag should be followed by the username of the user running this script. Used for accessing the xdisk  <br />
-t: This flag is used to specify the name of the test dataset to be created. Do not include .tar.gz in this name, that would be added by the script <br />

***Note:*** This script is expected to work only on the UA HPC, and might require modifications in order to be functional on other systems. 
