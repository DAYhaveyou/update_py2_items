# coding=utf-8
import MySQLdb as mdb
import yaml_get as yl
import os
import time
import yaml
import yaml_db as test_db


def connect():
    conn = mdb.connect(host='10.25.10.249', user='huacheng', passwd='huacheng123', db='LI_DataBase_ver2')
    sql = 'show tables'
    cursor = conn.cursor()
    cursor.excute(sql)

    val = cursor.fetchall()

    conn.close()
    print val


def test_unit(table, message):
    dir_name1 = '/home/liziqiang/Desktop/SHOWyou/j_zs_WH_WOBV_DX_QG_GZ_20180102-81542_grid.yaml'
    file_names = os.listdir(dir_name1)
    yaml_file = ""
    file_num = 0
    is_yaml = 0
    print "1 is ok"
    for file_s in file_names:
        if '.yaml' in file_s:
            print file_s[-5:]
            yaml_file = file_s
            is_yaml = 1
            break
            # f_yaml = open(yaml_file)
    print yaml_file
    print file_names[0]
    print len(file_names)

    yaml_file = dir_name1 + '/' + yaml_file
    if is_yaml == 0:
        print "can't find the yaml file"
        return

    # f_yaml = open(yaml_file)
    print "Please wait to get the yaml data! name:\t %s" % yaml_file
    g_t1 = time.time()
    f_value = open(yaml_file)
    raw_values = yaml.load(f_value)
    g_t2 = time.time()
    print "Load yaml over! Cost time: %.3f" % (g_t2 - g_t1)
    g_all_length = len(raw_values)
    print g_all_length-2
    for i in range(2, g_all_length):
        value_temp = yl.deal_val_strategy(raw_values[i])
        temp_id = test_db.insert_yaml(table1, message, value_temp)
        if value_temp[10] in file_names:
            file_num += 1
        print "NUM: ", temp_id
    print "The total file number: ", file_num


def test_unit1(table, message):
    '''
    dir_name1 = '/home/liziqiang/Desktop/SHOWyou/j_zs_WH_WOBV_DX_QG_GZ_20180102-81542_grid.yaml'
    file_names = os.listdir(dir_name1)
    yaml_file = ""
    file_num = 0
    is_yaml = 0
    print "1 is ok"
    for file_s in file_names:
        if '.yaml' in file_s:
            print file_s[-5:]
            yaml_file = file_s
            is_yaml = 1
            break
            # f_yaml = open(yaml_file)
    print yaml_file
    print file_names[0]
    print len(file_names)

    yaml_file = dir_name1+'/'+yaml_file
    if is_yaml == 0:
        print "can't find the yaml file"
        return
    '''
    yaml_file = "5PP5LY1.yaml"
    print "Please wait to get the yaml data! name:\t %s" % yaml_file
    g_t1 = time.time()
    f_value = open(yaml_file)
    raw_values = yaml.load(f_value)
    g_t2 = time.time()
    print "Load yaml over! Cost time: %.3f" % (g_t2 - g_t1)
    g_all_length = len(raw_values)

    for i in range(2, g_all_length):
        # g_t3 = time.time()
        # value_temp = yl.deal_val_strategy(raw_values[i])
        value_temp = yl.deal_val_strategy(raw_values[i])
        if len(value_temp) < 11:
            print "Wrong!"
            return
        temp_id = test_db.insert_yaml(table, message, value_temp)

        # g_t4 = time.time()
        # print "Num %d cost %f s" % (temp_id, (g_t4 - g_t3))
        # print "Num ", temp_id, " cost ", (g_t4 - g_t3), "s"
        # if value_temp[10] in file_names:
        #    file_num += 1
        # print "The total file number: ", file_num


def test_unit3():
    yaml_file = "5PP5LY1.yaml"
    print "Please wait to get the yaml data! name:\t %s" % yaml_file
    g_t1 = time.time()
    f_value = open(yaml_file)
    raw_values = yaml.load(f_value)
    g_t2 = time.time()
    print "Load yaml over! Cost time: %.3f" % (g_t2 - g_t1)
    g_all_length = len(raw_values)
    '''
    val = yl.deal_val_strategy(raw_values[178])
    for i in val:
        print i
    val1 = yl.deal_val_strategy(raw_values[179])
    for i in val1:
        print i
    '''

    val2 = yl.deal_val_strategy(raw_values[181])
    test_db.insert_yaml(table1, message1, val2)
    for i in val2:
        print i
    print raw_values[181][2]['Optimum']


def get_the_value_to_test(table, message):
    sql1 = "select back_test_value from " + table + "where csv1_id = 1000"
    sql = "select optimum_values from " + table + " where csv1_id = 1000"
    conn = mdb.connect(host='10.25.10.249', user='huacheng', passwd='huacheng123', db='LI_DataBase_ver2')
    cursor = conn.cursor()
    cursor.execute(sql)

    val = cursor.fetchone()

    conn.close()
    print val[0]
    test1 = yl.deal_data5_of_unknown(val[0])

    if str(test1) == val[0]:
        print "good!"
    else:
        print "-_-!"
    return val[0]


def get_name_table_name(str):
    flag = 0
    index = 7
    str = str[:-5]
    str1 = str[:8]
    # str1 += str[7]
    for i in str[8:]:
        if i.islower():
            str1 += i
            index += 1
            continue
        if i == '_':
            str1 += i
            index += 1
            continue
        if i.isupper():
            if str1[index] == '_':
                str1 += i
                index += 1
                continue

        else:
            str1 += i
            index += 1
    str1 = str1.replace('-', "_")
    str1 = str1.replace('.', "_")

    return str1


def test_unit5(file_name):
    f = open(file_name, 'w')

    values = ['show me!', 'let me know', 'good!']
    for i in values:
        f.write(i+'\n')
    f.close()


table1 = 'yaml_table'
message1 = ['127.0.0.1', 'root', '7ondr', 'testpy']
# test_unit1(table1, message1)
# test_unit3()

# print float('inf')
# a = [float('inf')]
# print a[0]*float('-inf')


message2 = ["10.25.10.249", "huacheng", "huacheng123", "LI_DataBase_ver2"]
table1 = 'yaml_test_table_ver2'
names = 'OCBJ5Y.rb_zs_TB_WOBV_DX_QG_GZ_ADC_DK_20180323-102633_grid.yaml'
# test_unit(table1, message2)
# get_the_value_to_test(table1, message2) ok




