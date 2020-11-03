# Exercise 12.3
# Think Python
# Chapter 12 - Tuples
# Exercise 3

# Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. 
# Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

def most_frequent(s):

    # create a dictionary with keys of letters and values of letter frequency
    histogram = dict()

    for letter in s:
        letter = letter.lower()
        histogram[letter] = histogram.get(letter, 0) + 1

    # create a list of tuples: frequency, letter
    frequencies = []

    for k in histogram:
        frequencies += [(histogram[k], k)]

    frequencies.sort(reverse=True)

    for t in frequencies:
        print(t[1])


if __name__ == "__main__":

    # english sample
    english = "Cellular immunity is a complex but potentially very significant piece of the Covid-19 puzzle, and it’s important that more research be done in this area. However, early results show that T-cell responses may outlast the initial antibody response, which could have a significant impact on Covid vaccine development and immunity research."

    # spanish sample
    spanish = "En ocasiones olvidamos que el ayuno intermitente tiene dos partes. Una es evidentemente en la que ayunamos: durante determinadas horas del día, que en el caso de Pataky son 16 horas, no está permitido comer nada sólido. Pero sí se pueden tomar líquidos, ya que mantenerse hidratada es esencial para que nuestro cuerpo funcione de una forma adecuada."

    # italian sample
    italian = "Negli sguardi del popolo della Rossalleggi la fierezza di appartenere a una leggenda. Entri nel cuore della Ferrari e vedi l’ultimo modello della ‘ Roma’ che sta salendo sulla rampa di un camion (\"parte per la consegna a un cliente\"), mentre a destra si erge il ‘Centro sviluppo prodotto’ progettato da Fuksas (\"nel 2019 sono state realizzate non più di 10.131 auto\", l’esclusività, il rimanere sotto gli ordinativi effettivi è parte fondamentale del valore Ferrari). Quindi è la volta delle linee di montaggio dove prendono vita 35-40 vetture al giorno e, subito dopo, della fucina delle idee commissionata da Sergio Marchionne per inserire in un unico edificio quattro componenti strategiche: Ferrari Design (che include un’ottantina di progettisti e designers delle auto), la Modelleria per la predisposizione delle scocche, il Taylor Made e l’Atelier per la personalizzazione dei modelli."

    most_frequent(italian)