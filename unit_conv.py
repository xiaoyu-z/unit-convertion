__author__ = 'zhengxiaoyu'
distance_convert_list_based_on_m = [['ft', 3.281], ['cm', 100], ['mm', 1000], ['mi', 0.0006214], ['yd', 1.094],
                                    ['km', 0.001], ['in', 39.37], ['m', 1]]
volumes_convert_list_based_on_ml = [['floz', 0.03381], ['qt', 0.001057],['cup', 0.1] ,['mL',1],
                                     ['L', 0.001], ['gal', 0.000264172051242], ['pint', 0.002113376]]
weights_convert_list_based_on_g = [['lb', 0.00220462262185], ['mg', 1000], ['kg', 0.001], ['oz',0.03527396], ['g', 1]]

final_list = [distance_convert_list_based_on_m,volumes_convert_list_based_on_ml,weights_convert_list_based_on_g]
def convert_to_target(target_unit, amount, unit_convert_list):
    '''
    :return the amount converted from base unit to target unit
    >>> convert_to_target('km',1000,distance_convert_list_based_on_m)
    1.0
    '''
    for i in unit_convert_list:
        if i[0]==target_unit:
            return amount*i[1]

def convert_to_base(input_unit, amount, unit_convert_list):
    '''
    :return the amount converted from input unit to base unit
    >>> convert_to_base('L',1,volumes_convert_list_based_on_ml)
    1000.0
    '''
    for i in unit_convert_list:
        if i[0] == input_unit:
            return amount/i[1]

def find_category(input_unit):
    '''
    :return the category of the different unit
    return -1 if it is not in the list
    >>> find_category('w')
    -1
    >>> find_category('cm')
    0
    '''

    for i in final_list:
        for k in i:
            if input_unit == k[0]:
                return final_list.index(i)
    return -1
def print_result(origin_unit, target_unit, input_amount, result_amount):
    '''

    :print the output
    >>> print_result('cm','ft',12, 20)
    12 cm = 20.0 ft
    '''
    print  input_amount, origin_unit,"=",round(result_amount, 6), target_unit

def read_and_convert():
    '''
    conbination of functions above to convert
    '''
    input = raw_input("Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]:").split()

    if len(input) == 1 and input[0] == 'q':
        exit()
    if len(input) == 4 and input[2] == 'in':
        orgin_category = find_category(input[1])
        target_caregory = find_category(input[3])
        #print orgin_category,target_caregory
        if(orgin_category==target_caregory and orgin_category>=0):
            try: float(input[0])
            except ValueError: print "amount should be number"
            else:
                result =  convert_to_target(input[3],
                convert_to_base(input[1],float(input[0]),final_list[orgin_category]),
                final_list[target_caregory])
                print_result(input[1],input[3],input[0],result)
            #except:print "amount shoulf be number"
        else:
            print("category error, check the two units")
    else:
        print('input error, please use correct format')


import sys
if __name__ == '__main__':
    print "Welcome to our Python-powered Unit Converter v1.0 by Xiaoyu\n"\
          "You can convert Distances , Weights , Volumes to one another, but only\n"\
          "within units of the same category, which are shown below. E.g.: 1 mi in ft"
    print "Distances: ft cm mm mi m yd km in\nWeights: lb mg kg oz g\nVolumes: floz qt cup mL L gal pint\n"
    while( True ):
        read_and_convert()


