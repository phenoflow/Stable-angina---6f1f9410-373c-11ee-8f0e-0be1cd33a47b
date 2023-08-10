# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"322..00","system":"readv2"},{"code":"3222","system":"readv2"},{"code":"322Z.00","system":"readv2"},{"code":"G33z400","system":"readv2"},{"code":"26965","system":"med"},{"code":"26967","system":"med"},{"code":"26973","system":"med"},{"code":"35287","system":"med"},{"code":"42104","system":"med"},{"code":"46230","system":"med"},{"code":"8246","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stable-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stable-angina-ischaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stable-angina-ischaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stable-angina-ischaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
