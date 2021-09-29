# create a new file to write to
new_file='Resources_Election_Analysis\elec_new_file.txt'

#open the file in W mode
# elec_new_file=open(new_file,'w')
###
#open the file in W mode using the with function instead (you can now omit the final sstep below, of closing the file)
with open(new_file,'w') as txt_file:

#write some data to the file
# elec_new_file.write("Hello World")
    txt_file.write("Hello World \nHello World 2")

#open the file in W mode using the with function
with open(elec_outcome,'w') as txt_file:
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

#close the file
# elec_new_file.close()



