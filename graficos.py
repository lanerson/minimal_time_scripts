import json
import matplotlib.pyplot as plt
import os 
import statistics
from inter import encontrar_interseccoes
import pandas as pd

COMPUTER_NICK = 'graphs'
a = sorted(os.listdir('./jsons'))
files = []
for i in range(0,len(a),2):
    file = ''
    for k in range(len(a[i])):
        if a[i][k] == a[i+1][k]:
            file += a[i][k]
    files.append(file[0:len(file)-5])
    file = ''
print(files)

TAM = 0
with open("vals.txt") as file: TAM = len(file.readlines())

TAM*=5

def getFunctions(filename):
    with open(filename+'.py') as experiment:
        functions = []    
        text = experiment.readlines()
        for line in text:
            if "def" in line and 'self' not in line:                
                functions.append(line.split(' ')[1].split('(')[0])
        functions.append('execution')
        functions.remove('main')
        return functions

def graphs(file_name,computer_nick):
    if not os.path.isdir('./'+computer_nick+'/'+file_name):
        os.mkdir('./'+computer_nick+'/'+file_name)
    # fig, ax = plt.subplots()

    f = open('./jsons/'+file_name+'_data.json')
    file_profile = json.load(f)
    # print(file_profile[''+file_name+'_profile'][0])
    data1 = [] 
    _data1 = {}
    functions = getFunctions(file_name)   
    print("funcoes ", functions)     
    for i in file_profile[''+file_name+'_profile']:
    
        if i['function'] in functions:
            # fig, ax = plt.subplots()
            mean = []
            name = []
            for j in i['cumulative_time']:
                mean.append(j)
                name.append(len(mean))  
            t = [n for n in name]
            s = [m for m in mean]
            _data1.update({i['function']: s})
            data1.append([t,s])
            # ax.plot(t, s, label=i['function'])
            # ax.set(xlabel='number of the test', ylabel='time (s)',
            #     title=i['function'])
    f.close()
    w = open('./jsons/'+file_name+'_data_cache.json')
    file_profile_ = json.load(w)
    # print(file_profile[''+file_name+'_profile'][0])
    data2 = []
    _data2 = {}
    for i in file_profile_[''+file_name+'_profile']:
        if i['function'] in functions:
            mean = []
            name = []
            per = []                 
            if len(i['cumulative_time']) == TAM:            
                for k in range(len(i['cumulative_time'])):
                    per.append(i['cumulative_time'][k])
                    if k%5 == 4:
                        name.append(int(k//5+1)) 
                        mean.append(statistics.median(per))
                        per = []
                                
                t = [n for n in name]
                s = [m for m in mean]                
                data2.append([t,s])
                _data2.update({i['function']: s})
            else:                
                for j in i['cumulative_time']:
                    mean.append(j)
                    name.append(len(mean))  
                t = [n for n in name]
                s = [m for m in mean]
                data2.append([t,s])
                _data2.update({i['function']: s})
    
    w.close()    
    df = pd.DataFrame(_data1)
    df.to_csv("data/"+file_name+".csv")
    df = pd.DataFrame(_data2)
    df.to_csv("data/"+file_name+"_cache"+".csv")
    return
    for i,j,k in zip(data1,data2,functions):
        fig, ax = plt.subplots()
        ax.plot(i[0],i[1], label=k+'--no-cache')
        ax.plot(j[0],j[1], label=k+'_cache')
        ax.set(xlabel='number of the test', ylabel='time (s)',
                title=k)
        # inters = encontrar_interseccoes(i[1],j[1])
        ax.grid()
        ax.legend()
        plt.savefig('./'+computer_nick+'/'+file_name+'/'+k)

        plt.close()
    
graphs(files[0], COMPUTER_NICK)    
exit()
for x in files:
    graphs(x,COMPUTER_NICK)  
    
