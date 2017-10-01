'''
This file is responsible for manipulatingand outputting
the data
'''
import csv

def read_csv_data():
    '''
    This method opens up read the csv and manipulates it
    '''
    with open('sample_data.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        total_biomas = []
        names = []
        harversting_date = []
        harvest_plants = []
        for row in reader:
            total_biomas.append(row[11])
            names.append(row[0])
            harversting_date.append(row[7])
            harvest_plants.append(row[10])
        del total_biomas[0]
        del names[0]
        del harversting_date[0]
        del harvest_plants[0]

        '''
        find the max value and the index
        and extract the name from the list
        '''
        max_value = max(total_biomas)
        max_index_value = total_biomas.index(max_value)
        print("The farmer with the highest biomas Fwt is {}".format(names[max_index_value]))

        '''
        find the Min value and the index
        and extract the name from the list'''

        min_value = min(total_biomas)
        min_index_value = total_biomas.index(min_value)
        print("The farmer with the lowest biomas Fwt is {}" .format(names[min_index_value]))


        '''
        sorted harvesting date
        '''
        print(sorted(harversting_date))


        '''
        avarage of harvest plants
        '''
        harvest = list(map(int, harvest_plants))
        avarage  = (sum(harvest)/float (len(harvest)))
        print("The avarage of No of plants is{}".format(avarage))

read_csv_data()
