Argomenti = ["Matematica", "Storia"   ]
contatore = 0

if ( (len(Argomenti)) < 5  ):
  print( "stai per aggiungere le materie mancanti" )

  while( contatore != 3  ):
    
     y = input('Inserisci la tua materia: ')
     contatore +=1

     Argomenti.append(y)
     if(contatore == 3 ):
       for x in Argomenti:
         print(x)
       
 
contatore = 0         