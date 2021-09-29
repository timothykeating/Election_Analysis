cou_dic={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}
# print(cou_dic)
# for county in cou_dic.keys():
#     print(county)
# for values in cou_dic.values():
#     print(values)

# print(cou_dic['Denver'])

# for key,value in cou_dic.items():
#     print(key,value)

# for county, voters in cou_dic.items():
#     print(str(county)+' county has '+str(voters)+' registered voters')

for county, voters in cou_dic.items():
    print(f'{county} county has {voters:,} registered voters')