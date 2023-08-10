# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"10209","system":"med"},{"code":"11610","system":"med"},{"code":"12734","system":"med"},{"code":"18249","system":"med"},{"code":"18670","system":"med"},{"code":"19046","system":"med"},{"code":"19193","system":"med"},{"code":"19402","system":"med"},{"code":"19413","system":"med"},{"code":"20903","system":"med"},{"code":"22020","system":"med"},{"code":"22647","system":"med"},{"code":"22828","system":"med"},{"code":"28837","system":"med"},{"code":"31519","system":"med"},{"code":"31556","system":"med"},{"code":"3159","system":"med"},{"code":"32651","system":"med"},{"code":"33471","system":"med"},{"code":"33718","system":"med"},{"code":"33735","system":"med"},{"code":"34963","system":"med"},{"code":"36011","system":"med"},{"code":"37682","system":"med"},{"code":"37719","system":"med"},{"code":"38813","system":"med"},{"code":"41547","system":"med"},{"code":"42304","system":"med"},{"code":"42462","system":"med"},{"code":"42708","system":"med"},{"code":"43939","system":"med"},{"code":"44561","system":"med"},{"code":"45370","system":"med"},{"code":"45886","system":"med"},{"code":"48767","system":"med"},{"code":"51507","system":"med"},{"code":"51515","system":"med"},{"code":"55092","system":"med"},{"code":"55598","system":"med"},{"code":"56990","system":"med"},{"code":"5703","system":"med"},{"code":"57241","system":"med"},{"code":"5744","system":"med"},{"code":"59423","system":"med"},{"code":"60067","system":"med"},{"code":"60753","system":"med"},{"code":"61208","system":"med"},{"code":"61310","system":"med"},{"code":"62608","system":"med"},{"code":"64923","system":"med"},{"code":"66236","system":"med"},{"code":"66664","system":"med"},{"code":"66921","system":"med"},{"code":"67591","system":"med"},{"code":"67761","system":"med"},{"code":"68123","system":"med"},{"code":"68139","system":"med"},{"code":"69776","system":"med"},{"code":"70111","system":"med"},{"code":"70185","system":"med"},{"code":"70755","system":"med"},{"code":"7134","system":"med"},{"code":"7137","system":"med"},{"code":"72780","system":"med"},{"code":"732","system":"med"},{"code":"733","system":"med"},{"code":"737","system":"med"},{"code":"7442","system":"med"},{"code":"7609","system":"med"},{"code":"7634","system":"med"},{"code":"8312","system":"med"},{"code":"85947","system":"med"},{"code":"86071","system":"med"},{"code":"86773","system":"med"},{"code":"8679","system":"med"},{"code":"87849","system":"med"},{"code":"8942","system":"med"},{"code":"92419","system":"med"},{"code":"92927","system":"med"},{"code":"93618","system":"med"},{"code":"93828","system":"med"},{"code":"9414","system":"med"},{"code":"96537","system":"med"},{"code":"96804","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stable-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stable-angina-performed---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stable-angina-performed---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stable-angina-performed---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
