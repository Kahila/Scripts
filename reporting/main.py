import validate_files
from art import text2art
import ad_Info
import admin_groups

def main():
    print(text2art("Cybercom"))
    path_ = validate_files.validate_dir()
    # ad_Info.get_computer_info(f"{path_}\\AD_Info.txt", "Computer information:", "Server information:")
    # ad_Info.get_computer_info(f"{path_}\\AD_Info.txt", "Server information:", "")
    admin_groups.get_admins(path_)

if __name__== "__main__" :
    main()