import json
import matplotlib.pyplot as plt
import os 
import statistics
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

def getFunctions(filename):
    with open(filename+'.py') as experiment:
        functions = []    
        text = experiment.readlines()
        for line in text:
            if "def" in line and 'self' not in line:                
                functions.append(line.split(' ')[1].split('(')[0])
        functions.append('execution')
        return functions

def graphs(file_name,computer_nick):
    os.mkdir('./'+computer_nick+'/'+file_name)
    fig, ax = plt.subplots()

    f = open('./jsons/'+file_name+'_data.json')
    file_profile = json.load(f)
    print(file_profile[''+file_name+'_profile'][0])
        
    for i in file_profile[''+file_name+'_profile']:
        functions = getFunctions(file_name)
        if i['function'] == 'execution':
            mean = []
            name = []
            for j in i['cumulative_time']:
                mean.append(j)
                name.append(len(mean))  
            t = [n for n in name]
            s = [m for m in mean]
            fig, ax = plt.subplots()
            ax.plot(t, s)
            ax.set(xlabel='number of the test', ylabel='time (s)',
                title=i['function'])
            ax.grid()
    w = open('./jsons/'+file_name+'_data_cache.json')
    file_profile = json.load(w)
    print(file_profile[''+file_name+'_profile'][0])
    for i in file_profile[''+file_name+'_profile']:
        if i['function']=='execution':
            mean = []
            name = []
            per = []
            for k in range(len(i['cumulative_time'])):
                per.append(i['cumulative_time'][k])
                if k%5 == 4:
                    name.append(int(k/5+1)) 
                    mean.append(statistics.median(per))
                    per = []
            t = [n for n in name]
            s = [m for m in mean]
            ax.plot(t, s)
            ax.grid()
    plt.savefig('./'+computer_nick+'/'+file_name+'/'+i['function'])

for x in files:
    # graphs(x,COMPUTER_NICK)  
    print(getFunctions(x)  )
    