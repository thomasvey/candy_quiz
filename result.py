import numpy as np
from matplotlib import pyplot as plt

def calculation(techer, kids, delta):
    # Für alle Eingaben des Lehrers
    for td in techer.time_dots:

        # bestimmte das Zeitfenster
        type(td)
        type(delta)
        dmin = td - delta
        dmax = td + delta
        
        # Überprüfe für jedes Kind
        for k in kids:
            
            # Ergebniswert zurücksetzen
            val = 0

            # überprüfe alle eingaben des Kindes
            for ktd in k.time_dots:

                # wurde eine Eingabe im vorgegebenen Zeitfenster getätigt?
                if(dmin < ktd < dmax):
                    # falls ja, setzte den Ergebniswert auf 1
                    val = 1
                    # breche die Überprüfung ab
                    break
            
            # füge das ergebnis zur ErgebnisListe hinzu
            k.hits = np.append(k.hits, [val])

def show(teacher, kids):
    fig, ax = plt.subplots(len(kids)+1)
    fig.suptitle("Auswertung")
    
    teacher.hits = np.ones(len(teacher.time_dots))
    m =  ['ko','bo','go','ro','co','mo','yo','bo','go','ro','co','mo','yo']
    players = [teacher] + kids
    for i, p in enumerate(players):
        ax[i].text(-0.02, 0.5, p.name, 
                   ha='right', transform=ax[i].transAxes)
        ax[i].text(1.02, 0.5, f'({len([h for h in p.hits if h == 1])})',
                   ha='left',  transform=ax[i].transAxes)
        ax[i].plot(teacher.time_dots,p.hits, m[i])
        ax[i].set_ylim(0.5, 1.5)
        ax[i].yaxis.set_visible(False)
        ax[i].xaxis.set_visible(False)
    
    mng = plt.get_current_fig_manager()
    mng.resize(1920,1080)
    
    plt.show()