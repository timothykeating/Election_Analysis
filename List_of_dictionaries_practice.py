voting_data=[{'county':'Arapahoe','registered_voters':422829},
{'county':'Denver','registered_voters':463353},
{'county':'Jefferson','registered_voters':432438}]

for county_dic in voting_data:
    
    # print(county_dic)
    # for voters in county_dic.values():
    #     print(voters)
    # print(county_dic.values())
    # for value in county_dic:
    #     print(value)
    # print(county_dic['registered_voters'])
    # print(county_dic['county'])
    # for key,value in county_dic.items():
    #     print(value)

    print(f'{county_dic["county"]} county has {county_dic["registered_voters"]:,} registered voters')
   


