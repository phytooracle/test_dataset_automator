# Test Dataset Automator
This script is used to create test datasets for scans of different sensors such as RGD, 3D, IR etc.  

## Usage - Python Script
Use the python script when you want to recursively generate test datasets for all scans within a directory.<br/>
```python3 ProcessFullDirectory.py -p <path containing multiple scan dates> -u <netid> -n <#> -r  ``` <br/>
```python3 ProcessFullDirectory.py -p <path containing multiple scan dates> -u <netid> -n <#>```

### Flags - Python Script
-p: This flag is used to specify the **source path** containing scan directories.<br />
-- Example: /iplant/home/shared/phytooracle/season_14_sorghum_yr_2022/level_0/scanner3DTop would permit processing of all datasets within this directory.<br />
-n: This flag should be followed by the number of sub-directories from the example scan that should be included in the test dataset <br />
-u: This flag should be followed by the username of the user running this script. Used for accessing the xdisk  <br />
-r **(OPTIONAL)**: This flag is used to make the program choose files for the test dataset from a random position (default: from the middle of the scan)

## Usage - Shell Script
* For choosing files from the center of the field/scan (Normally used for checking the pipeline) </br>
```./automator.sh -p [pathname] -u [username] -t [test_dataset_name(DON'T INCLUDE .tar.gz)] -n [number_of_files]```
* For choosing files from a random position in the field/scan (Normally used for creating training datasets) </br>
```./automator_random.sh -p [pathname] -u [username] -t [test_dataset_name(DON'T INCLUDE .tar.gz)] -n [number_of_files]```

### Flags - Shell Script
-p: This flag is used to specify the **source path** for the example scan used to create the test dataset.<br />
-n: This flag should be followed by the number of sub-directories from the example scan that should be included in the test dataset <br />
-u: This flag should be followed by the username of the user running this script. Used for accessing the xdisk  <br />
-t: This flag is used to specify the name of the test dataset to be created. Do not include .tar.gz in this name, that would be added by the script <br />

***Note:*** 
* This script is expected to work only on the UA HPC, and might require modifications in order to be functional on other systems.</br>
* Also, before running the shell script, it might be necessary to run the following command in the directory that has it. </br>
``` chmod 755 automator.sh ```
