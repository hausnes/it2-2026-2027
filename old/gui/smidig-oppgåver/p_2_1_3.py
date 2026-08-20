import tkinter as tk
from tkinter import ttk
from tkinter import font

aktiviteter = [
    {'aktivitet':'Aerobics'  , 'kcal_pr_time': 814},
    {'aktivitet':'Bordtennis', 'kcal_pr_time': 236},
    {'aktivitet':'Fotball'   , 'kcal_pr_time': 510},
    {'aktivitet':'Golf'      , 'kcal_pr_time': 244},
    {'aktivitet':'Jogging'   , 'kcal_pr_time': 666}
]

def beregn():
    i = aktivitet_cb.current()
    if i!=-1:
        aktivitet = aktiviteter[i]['aktivitet']
        kcal_pr_time = aktiviteter[i]['kcal_pr_time']
    else:
        resultat.configure(text='Du må velge en aktivitet.') 
        return
    i = intensitet_var.get()
    if i!=-1:
        intensitet = intensiteter[intensitet_var.get()][1]
        faktor = intensiteter[intensitet_var.get()][2]
    else:
        resultat.configure(text='Du må velge en intensitet.') 
        return     
    try:
        timer = int(minutter.get())/60
    except:
        resultat.configure(text='Oppgi antall minutter som heltall.') 
        return
    mld  = 'Aktivitet: ' + aktivitet
    mld += '\nIntensitet: ' + intensitet
    mld += '\nTimer: ' + f'{timer:4.2f}'
    kcal = kcal_pr_time*faktor*timer 
    mld += '\nKaloriborbruk: ' + f'{kcal:4.0f} kcal'
    resultat.configure(text=mld)

root = tk.Tk()
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Arial',size=15)
root.option_add('*TCombobox*Listbox.font', ('Arial',15)) 

root.geometry('450x500')
root.resizable(False, False)
root.title('Trenngskalkulator')

aktivitet_sel = tk.StringVar()
aktivitet_cb  = ttk.Combobox(root,
    textvariable=aktivitet_sel,font='Arial 15')
cb_values = []
for a in aktiviteter:
    cb_values.append(a['aktivitet'] +
         ' (' + str(a['kcal_pr_time'])+' kcal/time)')    
aktivitet_cb['values'] =  cb_values
aktivitet_cb['state'] = 'readonly'
aktivitet_cb.set('Velg aktivitet')
aktivitet_cb.pack(fill=tk.X, padx=25)

tk.Label(text='Velg intensitet',anchor='w') \
    .pack(padx=25,pady=(15,0),fill=tk.X)
intensiteter = [[0,'Lav',0.8],[1,'Middels',1],[2,'Høy',1.2]]
intensitet_var = tk.IntVar()
for el in intensiteter:
    tk.Radiobutton(root,text=el[1], 
        variable=intensitet_var,
        value=el[0],anchor='w') \
        .pack(padx=40,pady=5,fill=tk.X)
intensitet_var.set(-1)

tk.Label(text='Oppgi varigheten på treningen i minutter') \
    .pack(padx=(25,0),pady=(15,0),anchor='w')
minutter = tk.Entry(font='Arial 15')
minutter.pack(padx=40,pady=5,anchor='w')

tk.Button(text='Beregn kaloriforbruk', command=beregn,
    padx=10, bg='#cacaca') \
    .pack(padx=40,pady=5,anchor='w')

resultat = tk.Label(borderwidth=2,relief='sunken', justify=tk.LEFT,
    bg='white',height=100,width=100,anchor='w', padx=10)
resultat.pack(padx=40,pady=(5,25))
root.mainloop()

# Smidig IT-2 © TIP AS 2024