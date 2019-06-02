import os
from cudatext import *
import json

data_folder_name=os.path.dirname(os.path.abspath(__file__))

default_browsers='IE {Internet Explorer}; Chr {Chrome}; Op {Opera}; Sf {Safari}; Mz {Firefox}; An {Android}; iOS {iOS}'

def short_name(name):
    names_pairs=ini_read(fn_config,'op','info',default_browsers).split(';')
    names_dict={}                                                          
    for i in names_pairs:                                                  
        full=i.split('{')[1].split('}')[0]                                 
        short=i.split('{')[0].strip()                                      
        names_dict[full]=short                                             
    if not name in names_dict:                                             
        return name                                                        
    return names_dict[name]                                                

def arr_to_str(arr):
    res=arr[0].rstrip('+')
    for i in arr[1:]:
        res+='/'+i.rstrip('+').rstrip('+</;')
    return res

def get_data_by_property(prop):
    global res
    if prop in res:
        out=ini_read(fn_config,'op','info',default_browsers)
        replacing=[]
        rp=res[prop]
        for i in out.split('{')[1:]:
            replacing.append(i.split('}')[0])
        for i in replacing:
            if len(rp[i])>0 and not rp[i]==['']:
                set=arr_to_str(rp[i])
                set=set.replace('.0','')
                out=out.replace('{'+i+'}',set)
            else:
                out=out.replace('{'+i+'}','-')
        if out.endswith('</;'):
            out=out[:-3]
        if out.endswith('+</'):
            out=out[:-3]    
        return out
        for i in rp:
            if len(rp[i])>0 and not rp[i]==['']:
                out+=short_name(i)+' '+arr_to_str(rp[i]).replace('.0','')+';'
            else:
                out+=short_name(i)+' -;'
        if out.endswith('</;'):
            out=out[:-3]
        return out
    return False

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_css_property_info.ini')

class Command:
    
    def __init__(self):
        global res#=json.load(open('result.json','r'))
        res=json.load(open(data_folder_name+os.sep+'data.json','r'))

    def config(self):
        if not os.path.exists(fn_config):
            ini_write(fn_config,'op','info',default_browsers)
            ini_write(fn_config,'op','status_alt','0')
        file_open(fn_config)
        pass
                
    def on_caret(self, ed_self):
        x,y,x1,y1=ed_self.get_carets()[0]
        #print(ed_self.get_carets()[0][2])
        if not y==y1:
            return
        if not (x1==-1):
            if x>x1:
                x,x1=x1,x
            #print(str(x)+' '+str(y)+' '+str(x1)+' '+str(y1))
            text=ed_self.get_text_substr(x,y,x1,y1)
            if text:
                res=get_data_by_property(text)
                if res:
                    if ini_read(fn_config,'op','status_alt','0')=='1':
                        msg_status_alt(res,5)
                    else:
                        msg_status(res)# font-size
