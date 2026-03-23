import subprocess
import random
from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate a random word
random_word = fake.word()
random_word2 =fake.word()
title = random_word+" "+random_word2
print(title)

interval_names = ["pryma ", "sekunda mała ", "sekunda wielka", "tercja mała", "tercja wielka", "kwarta czysta","kwinta zmniejszona", "kwinta czysta", "seksta mała", "seksta wielka", "septyma mała", "septyma wielka","oktawa czysta"]

def insert_text_in_spaces(s, text):
    return s.replace(' ', f' {text} ')

def get_octave(user_number1, user_number2):
    
    '''Funkcja pobierająca oktawą z jakiej pochodzi najniższy i najwyższy  dźwiek'''
    
    user_number = int(user_number1)-1
    octaves = [",,,",",,",","," ","'","'","''","'''"]
    
    if user_number <= 3:
        key = "bass"
    elif user_number > 3:
        key = 'violin'
        
    user_number = int(user_number2)-1
    octaves = [",,,",",,",","," ","'","'","''","'''"]
    low_octave = octaves[user_number1-1]
    high_octave = octaves[user_number2-1]
    
    return key, low_octave, high_octave

def get_weights(interval_names):
    '''Dunkcja pobierająca prawdopodobieństwa kolejnych interwałów'''
    interval_weigths = []
    for i in interval_names:
        val = int(input(f"Podaj wagę dla interwału {i}: "))
        interval_weigths.append(val)
    
    interval_steps_up_all = []
    interval_steps_up = [j for j in range(0,len(interval_names))]
    interval_steps_down = [j for j in range(1,len(interval_names))]
    
    interval_steps_down_all = []
    for j in range(0,len(interval_names)):
        for k in range(0,interval_weigths[j]):
            interval_steps_up_all.append(interval_steps_up[j])
    for j in range(1,len(interval_names)-1):
        for k in range(0,interval_weigths[j]):
            
            interval_steps_down_all.append(interval_steps_down[11-j])
        
    interval_steps_down_all = [-i for i in (interval_steps_down_all)]

    interval_weights_up = interval_weigths
    interval_weights_down = interval_weigths.reverse()
    
    # interval_steps_up = [j for j in range(1,len(interval_names_up))+1]
    # interval_steps_down = [-j for j in range(1,len(interval_names_down))+1]
    
    
    return interval_steps_up_all, interval_steps_down_all
        

def change_probability(av_notes,min_note):
    
    '''Funckja manipulująca prawdopodobieństwem wystąpeniea poszczególnych wysokości'''
    list_of_weights=[]
    for i in range(0,12):
        weight = int(input(f"Podaj mnożnik dla {i+1} dźwięku 1-c,2-cis,itd)): "))
        list_of_weights.append(weight)
    
    list_of_weights_start = list_of_weights[min_note:]
    while True:
        if len(list_of_weights_start) < len(av_notes):
            list_of_weights_start = list_of_weights_start+list_of_weights
            continue
        else:
            list_of_weights_start = list_of_weights_start[:len(av_notes)]
            break
    idx = 0
    for i in list_of_weights_start:
        for j in range(0,i):
            av_notes.append(av_notes[idx])
        idx = idx + 1
    return av_notes

def create_bar(time,melody,notes,val_of_notes, pause_probability):
    
    """Tutaj powstaje bezpośrednio lista nut"""
    rythm = []
    space = 4*time 
    while space != 0: #sprawdzamy czy jest jeszcze miejsce w takcie
        pp = random.randint(1,100) #losowanie czy występuje w tym momencie pauza
        if pp<=pause_probability:
            p = random.randint(0,len(pauses)-1) # losujemy element z listy nut 
            if val_of_pauses[p]<=space:
                rythm.append(pauses[p])
                space = space - val_of_pauses[p]
        else:
            r = random.randint(0,len(notes)-1) # losujemy element z listy nut 
            if val_of_notes[r]<=space:
                rythm.append(notes[r])
                space = space - val_of_notes[r]
    return rythm
'''Pytania do użytkownika'''
def user_questions():
    time = int(input('Zadaj metrum przez podanie liczby n (n/4): '))
    bars = int(input('Zadaj liczbę taktów: '))

    pause_probability = int(input('Zadaj prawdopodobieństwo wystąpienia pauzy: [%]'))
    min_octave = int(input('Podaj numer oktawy z jakiej ma pochodzić najniższy dźwięk (subkontra-1, kontra-2, wielka-3, mała-4, razkreślna-5 dwukreślna-6,trzykreślna-7,czterokreślna-8 ): '))
    max_octave = int(input("Podaj z jakiej oktawy ma pochodzić najwyższy dźwięk: (subkontra-1, kontra-2, wielka-3, mała-4, razkreślna-5 dwukreślna-6,trzykreślna-7,czterokreślna-8 ): "))
    min_note = int(input("Podaj jaki ma być najniższy używany przez generator dźwięk: (c-1 itd...) "))
    max_note = int(input("Podaj jaki ma być najwyższy dźwięk używany przez generator: (c-1 itd...) "))
    max_note = 12 - max_note
    
    key, low_octave, high_octave=get_octave(min_octave,max_octave)
    
    octaves_number = max_octave-min_octave
    
    return time, bars, pause_probability, low_octave, min_note, high_octave, max_note,key,octaves_number

def start_melody(time,min_note,min_octave,key):
    
    fake = Faker()

    
    random_word = fake.word()
    random_word2 =fake.word()
    title = random_word+" "+random_word2
    
    all_notes = ["c", "cis", "d", "dis" , "e", "f", "fis", "g", "gis","a","ais", "b"]
    octaves = [",,,",",,",","," ","'","'","''","'''"]
    melody=[
        '\header {\n'
  f'title = " {title}"\n'
'}\n'
        f"\\fixed {all_notes[(min_note-1)]}{min_octave}""{" "\n"
            
    f'\clef {key} \n '
    f'\ottava #0\n'
    f'\\time {time}/4 \n']
    return melody

def get_av_notes(min_note,max_note,octaves_number):
    all_notes = ["c", "cis", "d", "dis" , "e", "f", "fis", "g", "gis","a","ais", "b"]
    new_octave = ["c", "cis", "d", "dis" , "e", "f", "fis", "g", "gis","a","ais", "b"]
    for i in range(0,octaves_number):
        new_octave = [f"{j}'" for j in new_octave ]
        all_notes = all_notes+new_octave
    all_notes = all_notes[min_note:]
    all_notes = all_notes[:len(all_notes)-max_note]
  
    return all_notes

def get_melody(all_notes,intervals_up,intervals_down,rythm): #potrzebujemy liste wszystkich dostepnych nut po kolei, liste interwałów po wagowaniu, rythm->przygotowany wcześniej szbalon rytmiczny który zamienimy w melodię
    notes_number = 0
    for i in rythm:
        if i == 'f':
            notes_number = notes_number+1
            

    melody = []
    current_position=0
    max_position = len(all_notes)-1
    notes_to_add = []
    for i in range(0,notes_number):
        
        rd = random.randint(0,1)
        if rd == 0 or current_position== 0:
            while True:
                interv = random.randint(0,len(intervals_up)-1)
                if current_position+intervals_up[interv]<=max_position:
                 
                    new_note=all_notes[current_position+intervals_up[interv]]
                    notes_to_add.append(new_note)
                    current_position = current_position+intervals_up[interv]
                    break
            #idziemy melodią w górę
        elif rd==1 or current_position ==max_position:
            while True:
                
                interv = random.randint(0,len(intervals_down)-1)
                if current_position+intervals_down[interv]>=0:
                    new_note=all_notes[current_position+intervals_down[interv]]
                    notes_to_add.append(new_note)
                    break
                    
                        
    idx = 0     
    rythm_and_melody=""
    for i in range(0,len(rythm)):
        if rythm[i] == "f":
            rythm_and_melody+=notes_to_add[idx]
            idx +=1
        else:
            rythm_and_melody+=rythm[i]
            continue
        
                #idziemy w dół
        ########################Tutaj skończone#############################
        #1. Działa tworzenie rytmu
        #2.Do zrobienia algorytm tworzenia melodii
        #3. f z wartości rytminczych do podmianki
    octave_changer ="\ottava #0"    
    rythm_and_melody = insert_text_in_spaces(rythm_and_melody,octave_changer    )    
    return rythm_and_melody
    


notes  = ["f1 ","f2 ","f4 ","f8 ", "f16 ",
           "f2. ","f4. ","f8. "
           ]

pauses = ["r1 ","r2 ","r4 ","r8 ", "r16 "]
notes = notes+notes
bindings = ["f1~ ","f2~ ","f4~ ","f8~ ", "f16~ ",
           "f2.~ ","f4.~ ","f8.~ ",
           ]
notes = notes + bindings
val_of_notes = [16, 8, 4, 2, 1, 12, 6, 3]
val_of_pauses = [16 ,8 ,4 ,2 ,1]
val_of_notes = val_of_notes +val_of_notes
val_of_bindings = [16, 8, 4, 2, 1, 12, 6, 3]
val_of_notes=val_of_notes+ val_of_bindings



time, bars, pause_probability, low_octave, min_note, high_octave, max_note,key,octaves_number = user_questions()
interval_steps_up_all, interval_steps_down_all = get_weights(interval_names)

melody = start_melody(time,min_note,low_octave,key)

rythm =[]
for i in range(1,bars+1):           
    bar = create_bar(time,melody,notes,val_of_notes, pause_probability)    
    rythm =rythm+bar
rythm = ''.join(rythm)
all_notes= get_av_notes(min_note,max_note,octaves_number)    
# av_notes = change_probability(all_notes,min_note)
rythm_and_melody=get_melody(all_notes,interval_steps_up_all,interval_steps_down_all,rythm)  

melody.append('\n')
melody.append(rythm_and_melody)
melody.append('\n \\bar "||"\n'
        '}')

zad_zal = open("zad_zal.ly", 'w')

font_config = ['\paper {\n',
'#(set-paper-size "a4")\n',
'}\n',
'\layout {\n',
'indent = 0\in\n',
'ragged-last = ##f\n',
'\context {\n',
'\Score\n',
'\\remove "Bar_number_engraver"\n',
'}\n',
'}\n']



zad_zal.writelines(font_config)
zad_zal.writelines(melody)
zad_zal.close()
result = subprocess.run('lilypond zad_zal.ly', shell=True)