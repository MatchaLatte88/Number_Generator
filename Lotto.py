import random
from decimal import Decimal



iter_allowed = 6000 # Maximale Loop Iterations

class Dataset:
  def __init__(self, name, size, max_num, samples, min_perc, lowest, singles):
    self.name = name
    self.size = size
    self.max_num = max_num
    self.samples = samples
    self.min_perc = min_perc
    self.numbers = []
    self.counter = 0
    self.lowest = lowest
    self.range = range(self.lowest, (max_num + 1))
    self.singles = singles
    self.infinity_counter = 0

  def reset(self):
    self.numbers = []
    self.counter = 0 
    self.infinity_counter = 0

  def go(self):
    #print("\n",self.name,"\n")
    while len(self.numbers) < self.samples and self.infinity_counter < iter_allowed:
      min_prop(self)
      self.infinity_counter += 1
    if len(self.numbers) == self.samples:
      #print(self.numbers)
      return self.numbers
      
    elif len(self.numbers) > self.samples:
      #print("too many numbers. Got ", len(self.numbers))
      #print(self.numbers)
      return self.numbers
      
    else:
      return "Not enough numbers."

      #print("not enough numbers. Only got ", len(self.numbers))

# Klassenobjekte definieren:
Hauptzahlen = Dataset("Hauptzahlen", 8888, 50, 5, 2.6, 1, True)
Zusatzzahlen = Dataset("Zusatzzahlen", 8888, 12, 2, 9.4, 1, True)
Traumhaus = Dataset("Los Nummer", 888, 9, 7, 10.3, 0, False)


# Dataset Liste erstellen:
def create_dataset(dataset):
  lst = []
  while len(lst) < dataset.size:
    nums = lst.append(random.randint(dataset.lowest, len(dataset.range)))
  return lst

# Prozentuale Anteile ausrechnen und als Dictionary ausgeben:
def get_perc(dataset):
  perc = {}
  ds = create_dataset(dataset)
  for n in list(dataset.range):
    #print(n, ds.count(n))
    perc[n] = ((ds.count(n) / dataset.size)*100)
  return perc

# Dictionary durchlaufen und Zahlen mit Prozentzahl über Grenzwert zu Numbers-Liste hinzufügen:
def min_prop(dataset):
  counting = (dataset.counter + dataset.lowest)
  pers_dict = get_perc(dataset)#DICTIONARY
  values = list(pers_dict.values())#Liste aller Prozenten
  for p in values: # p = prozentzahl
    #print(counting) #test
    #print(p) #test
    if p > dataset.min_perc:
        if dataset.singles == True:
            if counting not in dataset.numbers: 
                dataset.numbers.append(counting)
                #print("Adding", counting) #test
        else:
            dataset.numbers.append(counting)
            #print("Adding", counting) #test           
    counting += 1



# Ausführung der Klassenfunktionen zu den Objekten:
""" print("\n----------EURO JACKPOT---------")
Hauptzahlen.go()
Zusatzzahlen.go()
print("\n----------Traumhaus---------")
Traumhaus.go() """

#for i in range(0,10):
    #Traumhaus.go()
   # Traumhaus.reset()
