# script for collecting data from http://htmlbook.ru website

import requests

def property_list():
    ans=requests.get('http://htmlbook.ru/css/').text.split('<div class="field-item even">')[1].split('<h2>Значения свойств</h2>')[0]
    lst=ans.split('<li>')[1:]
    lst2=[]
    for i in lst:
        lst2.append(i.split('</li>')[0].split('>')[-2].split('<')[0].strip(':').rstrip(')').rstrip('(').lstrip(':'))
    return lst2

def property_info(property_name):
  try:  
    ans=requests.get('http://htmlbook.ru/css/'+property_name).text
    try:
        ans=ans.split('<table class="data browser">')[1].split('</table>')[0].replace('\n','')
    except:
        return ''

    arr=[]

    s=0
    for i in ans.split('td'):
        if s%2==1:
            temp=i.split('</span></')[0]
            if 'colspan=' in temp:
                temp=temp.split('colspan=')[1]
                temp=temp.split('>')
                try:
                    temp[0]=int(temp[0].strip('"').strip("'"))
                except:
                    return ''
                temp.pop(1)
            else:
                temp=[1,temp.split('>')[-1]]
            arr.append(temp)
        s+=1
                
    browsers=[]
    for i in arr[:7]:
            browsers.append(i)

    versions=[]
    for i in arr[7:]:
        versions.append(i)

    for i in range(len(versions)):
        versions[i]=versions[i][1]

    browser_names=[]
    browser_nums=[]
    for i in browsers:
        browser_names.append(i[1])
        browser_nums.append(i[0])

    browser_versions_2=[]

    for i in browser_nums:
        t=[]
        for j in range(i):
            t.append(versions.pop(0))
        browser_versions_2.append(t)

    dic={}
    for i in range(len(browser_names)):
        dic[browser_names[i]]=browser_versions_2[i]

    return dic
  finally:
    pass

resdict={}
num=0
amount=len(property_list())
for i in property_list():
    print(str(num)+'/'+str(amount))
    pinf=property_info(i)
    if pinf:
        resdict[i]=property_info(i)
        print(property_info(i))
    num+=1

print(len(resdict))
import json
with open('result.json', 'w') as fp:
    json.dump(resdict, fp)
