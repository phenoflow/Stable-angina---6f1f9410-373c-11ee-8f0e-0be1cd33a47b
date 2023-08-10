# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"G33z700","system":"readv2"},{"code":"12804","system":"med"},{"code":"13185","system":"med"},{"code":"1414","system":"med"},{"code":"1430","system":"med"},{"code":"14782","system":"med"},{"code":"15349","system":"med"},{"code":"15373","system":"med"},{"code":"18125","system":"med"},{"code":"19542","system":"med"},{"code":"20095","system":"med"},{"code":"24540","system":"med"},{"code":"25842","system":"med"},{"code":"26863","system":"med"},{"code":"28554","system":"med"},{"code":"29902","system":"med"},{"code":"39546","system":"med"},{"code":"45960","system":"med"},{"code":"54535","system":"med"},{"code":"7696","system":"med"},{"code":"9555","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stable-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["angina---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["angina---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["angina---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
