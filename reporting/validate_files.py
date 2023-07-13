import colors
import re
import os

# method to validate inputs
def validate_dir():
    # getting path to dir with all required files
    master_folder = input("Path to master folder: ")
    dir_list = os.listdir(master_folder)
    regex = re.compile(r'^AD_(Info\.txt|UserGroupMembers\.csv|Users\.csv)$')
    # important_files = list(filter(regex.match, dir_list))

    get_client_info(f"{master_folder}\\AD_Info.txt")
    return (master_folder)

# method for getting client information
def get_client_info(filename):
    with open(filename, 'r', encoding='utf-16') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            print (f"{colors.clrs.OKGREEN}{line}{colors.clrs.ENDC}")
    continue_ = input(f"{colors.clrs.OKYELLOW}\n\nContinue with this client (y/n)?{colors.clrs.ENDC} ")
    while True:
        if continue_ == 'n':
            exit()
        elif continue_ == 'y':
            return(0)
        else:
            continue_ = input(f"{colors.clrs.FAIL}INVALID INPUT: SELECT y (yes) OR n (no)?{colors.clrs.ENDC} ")
