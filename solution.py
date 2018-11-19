import urllib.request

with open('input.txt') as f_in:
    with open('output.txt', 'w') as f_out:
        f_out.write("{:<20}".format('NAME') + "{:<8}".format('COMP')
                       + "{:<9}".format('ATT') + "{:<9}".format('YDS') + "{:<6}".format('TD')
                       + "{:<7}".format('INT') + "{:<50}".format('    PR') + '\n')
        line = f_in.readlines()
        i = 0
        for i in line:
            url = i
            f = urllib.request.urlopen(url)
            s = f.read()
            text = str(s)
            part_name = text.find("player-name")
            name = text[text.find('>', part_name) + 1:text.find('&', part_name)]
            part_attainment = text.find('player-totals')
            attainment = text[text.find('</td>', part_attainment)
                              + 5:text.find('</tr>', part_attainment)]
            attainment = attainment.replace('/', '')
            attainment = attainment.replace('t', '')
            attainment = attainment.replace('n', '')
            attainment = attainment.split('<d>')

            COMP = attainment[1].replace(',', '')
            ATT = attainment[3].replace(',', '')
            YDS = attainment[7]
            TD = attainment[11].replace(',', '')
            INT = attainment[13].replace(',', '')
            PR = attainment[19].replace(',', '')

            f_out.write('{:20} {:7} {:7} {:7} {:7} {:7} {:5}'.format(name, COMP, ATT, YDS, TD, INT, PR))
            f_out.write('\n')
