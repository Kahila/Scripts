import os
import colors

# method for getting computer information
def get_computer_info(filename, start, end):
    data = []
    with open(filename, 'r', encoding='utf-16') as file:
        while True:
            line = file.readline().strip()
            if line == start:
                while True:
                    line = file.readline().strip()
                    if line.split(':', 1)[0].strip() == "Name":
                        data.append((line.split(':', 1)[1].strip()))
                        while True:
                            line = file.readline().strip()

                            if file.tell() == os.path.getsize(filename):
                                break
                            if len(line.split(':', 1)) == 1:
                                continue

                            index_two = (line.split(':', 1)[1].strip())
                            index_one = line.split(':', 1)[0].strip()

                            if index_one == "Name":
                                data.append(index_two)
                            elif index_one == "OperatingSystem":
                                data.append(index_two)
                            elif index_one == "LastLogonDate":
                                data.append(index_two)
                            elif index_one == "PasswordLastSet":
                                data.append(index_two)
                            elif index_one == "Enabled":
                                data.append(index_two)
                            if line == end:
                                break
                        break
                break
    write_to_file(data, start)

# write data to file
def write_to_file(data, start):
    WRITE_TO = open("AD_Info.adoc", "a");
    WRITE_TO.write((f'.{start}\n[width="100%",cols="^1h,,,,", options="header"]\n|====================\n| Name | OperatingSystem | LastLogonDate  | PasswordLastSet | Enabled\n'))
    for entry in data:
        WRITE_TO.write((f"| {entry} "))
    WRITE_TO.write("\n|====================\n\n")
    WRITE_TO.close()

    print (f"{colors.clrs.OKGREEN}{start} saved collected: .\AD_Info.adoc{colors.clrs.ENDC}")