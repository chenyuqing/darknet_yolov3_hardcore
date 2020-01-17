import os
################################需要修改的参数
dir_file_path = "."  ##这个为train.txt val.txt test.txt存放的路径
train_filename =  "train8.txt"
val_filename = "val8.txt"
test_filename = "test8.txt"
#只适合jpg png等3字母结尾，标签为txt的情况
################################
############# train
label0 = 0
label1 = 0
label2 = 0
label3 = 0
label4 = 0
label5 = 0
label6 = 0
label7 = 0
label8 = 0
label9 = 0
label10 = 0
label11 = 0
label12 = 0
label13 = 0
label14 = 0

with open(dir_file_path+"/"+train_filename,"r") as f :
    test_lines = f.readlines()
for test_line in test_lines :
    if os.path.exists(test_line[:-5]+".txt") :
        with open(test_line[:-5]+".txt","r") as f_l :
            f_l_lines = f_l.readlines()
        for f_l_line in f_l_lines :
            if f_l_line[0] == "0" :
                label0 = label0 + 1
            elif f_l_line[0] == "2" :
       	        label2 = label2 + 1 
            elif f_l_line[0] == "3" :
                label3 = label3 + 1
            elif f_l_line[0] == "4" :
                label4 = label4 + 1
            elif f_l_line[0] == "5" :
                label5 = label5 + 1
            elif f_l_line[0] == "6" :
                label6 = label6 + 1
            elif f_l_line[0] == "7" :
                label7 = label7 + 1
            elif f_l_line[0] == "8" :
                label8 = label8 + 1
            elif f_l_line[0] == "9" :
                label9 = label9 + 1
            elif f_l_line[0:2] == "10" :
                label10 = label10 + 1           
            elif f_l_line[0:2] == "11" :
                label11 = label11 + 1
            elif f_l_line[0:2] == "12" :
                label12 = label12 + 1
            elif f_l_line[0:2] == "13" :
                label13 = label13 + 1
            elif f_l_line[0:2] == "10" :
                label10 = label10 + 1
            elif f_l_line[0:2] == "11" :
                label11 = label11 + 1
            elif f_l_line[0:2] == "12" :
                label12 = label12 + 1
            elif f_l_line[0:2] == "13" :
                label13 = label13 + 1
            elif f_l_line[0:2] == "14" :
                label14 = label14 + 1
            elif f_l_line[0] == "1" :
                label1 = label1 + 1
        
print (train_filename[:-4] + " :")
print ("all picture is ",len(test_lines))
print ("label0 = {0}".format(label0))
print ("label1 = {0}".format(label1))
print ("label2 = {0}".format(label2))
print ("label3 = {0}".format(label3))
print ("label4 = {0}".format(label4))
print ("label5 = {0}".format(label5))
print ("label6 = {0}".format(label6))
print ("label7 = {0}".format(label7))
print ("label8 = {0}".format(label8))
print ("label9 = {0}".format(label9))
print ("label10 = {0}".format(label10))
print ("label11 = {0}".format(label11))
print ("label12 = {0}".format(label12))
print ("label13 = {0}".format(label13))
print ("label14 = {0}".format(label14))
print ()

############# val
label0 = 0
label1 = 0
label2 = 0
label3 = 0
label4 = 0
label5 = 0
label6 = 0
label7 = 0
label8 = 0
label9 = 0
label10 = 0
label11 = 0
label12 = 0
label13 = 0
label14 = 0

with open(dir_file_path+"/"+val_filename,"r") as f :
    test_lines = f.readlines()
for test_line in test_lines :
    if os.path.exists(test_line[:-5]+".txt") :
    	with open(test_line[:-5]+".txt","r") as f_l :
            f_l_lines = f_l.readlines()
    	for f_l_line in f_l_lines :
            if f_l_line[0] == "0" :
            	label0 = label0 + 1
            elif f_l_line[0] == "2" :
            	label2 = label2 + 1
            elif f_l_line[0] == "3" :
            	label3 = label3 + 1
            elif f_l_line[0] == "4" :
                label4 = label4 + 1
            elif f_l_line[0] == "5" :
            	label5 = label5 + 1
            elif f_l_line[0] == "6" :
            	label6 = label6 + 1
            elif f_l_line[0] == "7" :
            	label7 = label7 + 1
            elif f_l_line[0] == "8" :
            	label8 = label8 + 1
            elif f_l_line[0] == "9" :
            	label9 = label9 + 1
            elif f_l_line[0:2] == "10" :
                label10 = label10 + 1
            elif f_l_line[0:2] == "11" :
                label11 = label11 + 1
            elif f_l_line[0:2] == "12" :
                label12 = label12 + 1
            elif f_l_line[0:2] == "13" :
                label13 = label13 + 1
            elif f_l_line[0:2] == "10" :
                label10 = label10 + 1
            elif f_l_line[0:2] == "11" :
                label11 = label11 + 1
            elif f_l_line[0:2] == "12" :
                label12 = label12 + 1
            elif f_l_line[0:2] == "13" :
                label13 = label13 + 1
            elif f_l_line[0:2] == "14" :
                label14 = label14 + 1
            elif f_l_line[0] == "1" :
                label1 = label1 + 1

print (val_filename[:-4] + " :")
print ("all picture is ",len(test_lines))
print ("label0 = {0}".format(label0))
print ("label1 = {0}".format(label1))
print ("label2 = {0}".format(label2))
print ("label3 = {0}".format(label3))
print ("label4 = {0}".format(label4))
print ("label5 = {0}".format(label5))
print ("label6 = {0}".format(label6))
print ("label7 = {0}".format(label7))
print ("label8 = {0}".format(label8))
print ("label9 = {0}".format(label9))
print ("label10 = {0}".format(label10))
print ("label11 = {0}".format(label11))
print ("label12 = {0}".format(label12))
print ("label13 = {0}".format(label13))
print ("label14 = {0}".format(label14))
print ()


############# test
label0 = 0
label1 = 0
label2 = 0
label3 = 0
label4 = 0
label5 = 0
label6 = 0
label7 = 0
label8 = 0
label9 = 0
label10 = 0
label11 = 0
label12 = 0
label13 = 0
label14 = 0

with open(dir_file_path+"/"+test_filename,"r") as f :
    test_lines = f.readlines()
for test_line in test_lines :
    if os.path.exists(test_line[:-5]+".txt") :
        with open(test_line[:-5]+".txt","r") as f_l :
            f_l_lines = f_l.readlines()
        for f_l_line in f_l_lines :
            if f_l_line[0] == "0" :
                label0 = label0 + 1
            elif f_l_line[0] == "2" :
                label2 = label2 + 1
            elif f_l_line[0] == "3" :
                label3 = label3 + 1
            elif f_l_line[0] == "4" :
                label4 = label4 + 1
            elif f_l_line[0] == "5" :
                label5 = label5 + 1
            elif f_l_line[0] == "6" :
                label6 = label6 + 1
            elif f_l_line[0] == "7" :
                label7 = label7 + 1
            elif f_l_line[0] == "8" :
                label8 = label8 + 1
            elif f_l_line[0] == "9" :
                label9 = label9 + 1
            elif f_l_line[0:2] == "10" :
                label10 = label10 + 1
            elif f_l_line[0:2] == "11" :
                label11 = label11 + 1
            elif f_l_line[0:2] == "12" :
                label12 = label12 + 1
            elif f_l_line[0:2] == "13" :
                label13 = label13 + 1
            elif f_l_line[0:2] == "10" :
                label10 = label10 + 1
            elif f_l_line[0:2] == "11" :
                label11 = label11 + 1
            elif f_l_line[0:2] == "12" :
                label12 = label12 + 1
            elif f_l_line[0:2] == "13" :
                label13 = label13 + 1
            elif f_l_line[0:2] == "14" :
                label14 = label14 + 1
            elif f_l_line[0] == "1" :
                label1 = label1 + 1

print (test_filename[:-4] + " :")
print ("all picture is ",len(test_lines))
print ("label0 = {0}".format(label0))
print ("label1 = {0}".format(label1))
print ("label2 = {0}".format(label2))
print ("label3 = {0}".format(label3))
print ("label4 = {0}".format(label4))
print ("label5 = {0}".format(label5))
print ("label6 = {0}".format(label6))
print ("label7 = {0}".format(label7))
print ("label8 = {0}".format(label8))
print ("label9 = {0}".format(label9))
print ("label10 = {0}".format(label10))
print ("label11 = {0}".format(label11))
print ("label12 = {0}".format(label12))
print ("label13 = {0}".format(label13))
print ("label14 = {0}".format(label14))

print ()


