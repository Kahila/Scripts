import datetime
import csv
import datetime

# convert csv data to json
def get_data(csv_file_path):
    domain_admins = []
    csv_file = open(csv_file_path, encoding='utf-8')
    with csv_file as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            domain_admins.append(row)
    csv_file.close()
    return (domain_admins)

# method for getting domain admin users
def get_admins(csv_file_path):
    domain_admins = get_data(f"{csv_file_path}\\Privileged Users\\Domain Admins.csv")
    admins = get_data(f"{csv_file_path}\\Privileged Users\\Administrators.csv")
    account_ops = get_data(f"{csv_file_path}\\Privileged Users\\Account Operators.csv")
    remote_desk_usrs = get_data(f"{csv_file_path}\\Privileged Users\\Remote Desktop Users.csv")
    server_ops = get_data(f"{csv_file_path}\\Privileged Users\\Server Operators.csv")

    all_users = get_data(f"{csv_file_path}\\AD_Users.csv")

    write_to_file(domain_admins, "Domain Admins Group", all_users)
    write_to_file(admins, "Administrators Group", all_users)
    write_to_file(account_ops, "Account Operators Group", all_users)
    write_to_file(remote_desk_usrs, "Remote Desktop Group", all_users)
    write_to_file(server_ops, "Server Operators Group", all_users)

def get_account_info(samAccountName, all_users):
    for entry in all_users:
        if samAccountName == entry['SamAccountName']:
            return(entry)
        
# Get range between dates
def get_max_password_age(password_set_date, max_password_age_policy):
    if password_set_date == "Never changed":
        return (password_set_date)
    
    passwordLastSet = datetime.datetime.strptime(password_set_date, "%Y-%m-%d %H:%M")
    today = datetime.datetime.today()
    result_age = today - passwordLastSet

    if max_password_age_policy > result_age:
        return (password_set_date)

    return (f"`{password_set_date}`")

# write to adoc file
def write_to_file(json_data, group_name, all_users):
    subgroups = []
    WRITE_TO = open("admin_group_tables.adoc", "a");
    WRITE_TO.write((f'.{group_name}\n[width="100%",cols="^1h,,,,", options="header"]\n|====================\n| Account | Password Last Set | Last Logon Timestamp | Account Last Modified | Password Status\n'))
    for entry in json_data:
        if entry["objectClass"] == "user":
            info = get_account_info(entry["SamAccountName"], all_users)
            WRITE_TO.write((f"| {info['SamAccountName']} | {info['PasswordLastSet']} | {info['lastLogonTimestamp']} | {info['modifyTimeStamp']} | [NOT CRACKED] \n"))
        elif entry["objectClass"] == "group":
            subgroups.append(entry['SamAccountName'])
    WRITE_TO.write("|====================\n\n")
    if len(subgroups) > 0:
        WRITE_TO.write(f"\n\nsubgroups found | {subgroups}\n\n")
    WRITE_TO.close()


