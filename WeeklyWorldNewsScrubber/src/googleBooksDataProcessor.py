import csv, json, enchant

def to_json(obj):                                             
    if isinstance(obj, counter):                                
        return {'n': obj.name,
                't': obj.getTotal(),
                'y': obj.totals}                       
    raise TypeError(obj.name+ ' is not JSON serializable') 

def to_json_norm(obj):                                             
    if isinstance(obj, counter):                                
        return {'n': obj.name,
                't': obj.getNormTotal(),
                'y': obj.normalized_totals}                       
    raise TypeError(obj.name+ ' is not JSON serializable') 

class counter:
    valToYear = { 0 : 1980, 1 : 1985, 2 : 1990, 3 : 1995, 4 : 2000, 5 : 2005 }
    yearToVal = dict((v,k) for k, v in valToYear.iteritems())
    cldMultiplier = {0 : 9, 1 : 8, 2 : 7, 3 : 6, 4 : 5, 5 : 4, 6 : 3, 7 : 2, 8 : 1}
    
    def __init__(self, name, n, y):
        self.normalized_totals = [0,0,0,0,0,0]
        self.totals = [0,0,0,0,0,0]
        self.totals[self.yearToVal[n]] = 1
        self.normalized_totals[self.yearToVal[n]] = self.cldMultiplier[y]
        self.name = name
    def __repr__(self):
        return str(self.getTotal())
    
    def update(self, n, y):
        self.totals[self.yearToVal[n]] = self.totals[self.yearToVal[n]] + 1
        self.normalized_totals[self.yearToVal[n]] = self.normalized_totals[self.yearToVal[n]] + self.cldMultiplier[y]
        
    def getTotal(self):
        return sum(self.totals)
    
    def getNormTotal(self):
        return sum(self.normalized_totals)
    
    def getVal(self, n):
        return self.totals[self.yearToVal[n]]
    
    def getNormVal(self, n):
        return self.normalized_totals[self.yearToVal[n]]
    
    def getName(self):
        return self.name

raw = csv.reader(open('googleBooksData.dat', 'rb'), delimiter=',', quotechar='|')
stringDictionary = {}
for r in raw:
    #if the key doesn't exist, add it
    processName = r[0].lower().strip('"').strip("'s").strip('_').strip('.').strip('-')
    processYear = int(r[2].strip(' '))
    processCloud = int(r[1].strip(' '))
    if processName not in stringDictionary:
        stringDictionary[processName] = counter(processName, processYear, processCloud)
    else:  
        stringDictionary[processName].update(processYear, processCloud)

#ok, so the usefulness of the dictionary has passed, stuff dictionary into a list
sorted_by_val = []
for val in stringDictionary.values():
    sorted_by_val.append(val)
#sort it
sorted_by_val = sorted(sorted_by_val, key=lambda v: v.getTotal(), reverse=True)

#write out the normalized data
f = open('wwn_flat.json', mode='w')
json.dump(sorted_by_val, f, separators=(',',':'), default=to_json)
f.close();
#write out the normalized data
f = open('wwn_norm.json', mode='w')
json.dump(sorted_by_val, f, separators=(',',':'), default=to_json_norm)
f.close();

sorted_by_val_single = sorted_by_val
#find only single words
for val in sorted_by_val_single:
    #do all the words in sorted_by_val.name agree with a spell checker?
    if len(val.name.strip(' ').replace('-', ' ').split(' ')) != 1:
        sorted_by_val_single.remove(val)

f = open('wwn_norm_single.json', mode='w')
json.dump(sorted_by_val_single, f, separators=(',',':'), default=to_json_norm)
f.close();

sorted_by_val_improper = sorted_by_val
d = enchant.Dict("en_US")
#remove proper nouns and non-engilsh words and phrases
for val in sorted_by_val_improper:
    #do all the words in sorted_by_val.name agree with a spell checker?
    for each in val.name.strip(' ').replace('-', ' ').split(' '):
        if not d.check(each.capitalize()):
            sorted_by_val_improper.remove(val)
            break
        
f = open('wwn_norm_improper.json', mode='w')
json.dump(sorted_by_val_improper, f, separators=(',',':'), default=to_json_norm)
f.close();
      
