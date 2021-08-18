dic= {'K1': {'Name':'Ram', 'Age':25, 'Loaction': 'Salem'},
      'K2': {'Name':'Vijay', 'Age':26, 'Loaction': 'Illampillai'},
      'K3': {'Name':'Arul', 'Age':25, 'Loaction': 'Iddapaddi'}
      }

print(dic)

dic['K1']['Note']='Studied in Tharamangalam'
print(dic)
dic['K4']={'Name': 'Jeevith', 'Age':25, 'Location':'SteelPlant'}
print(dic)
print(dic['K4']['Location'])