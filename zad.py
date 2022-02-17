
import random   
from datetime import date

entry_start = "\n===Biblioteka filmów===\n"

movies=[]

class Film:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        # Variables
        self.liczba_odtworzeń = 0

    def play(self, step = 1):
        self.liczba_odtworzeń += step

    def __str__(self):
        return f'tytul:{self.tytul}, rok:{self.rok_wydania}, gatunek:{self.gatunek}, odtworzen:{self.liczba_odtworzeń} '

    def __repr__(self):
        return f'tytul:{self.tytul}, rok:{self.rok_wydania}, gatunek:{self.gatunek}, odtworzen:{self.liczba_odtworzeń} '

class Serial(Film):
    def __init__(self, numer_sezonu, numer_odcinka, *args, reverse=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_sezonu = numer_sezonu
        self.numer_odcinka = numer_odcinka
        
    def __str__(self):
        txt = super().__str__()
        return f'sezon:{self.numer_sezonu:>02}, odcinek:{self.numer_odcinka:>02} ' + txt

    def __repr__(self):
        txt = super().__repr__()
        return f'sezon:{self.numer_sezonu:>02}, odcinek:{self.numer_odcinka:>02} ' + txt

def get_movies():
    selected = [x for x in movies if isinstance(x, Film) and not isinstance(x, Serial)]
    selected = sorted(selected, key=lambda x: x.liczba_odtworzeń, reverse=True) 
    print(selected)

def get_series():
    selected = [x for x in movies if isinstance(x, Serial)]
    selected = sorted(selected, key=lambda x: x.liczba_odtworzeń, reverse=True) 
    print(selected)

def search_movie():
    search_movie = input('Szukany tytul filmu albo serialu: ')
    for movie in movies:
        if movie.tytul == search_movie:
            return movie

def generate_views():
    movie = random.choice(movies)
    i = random.randint(1, 100)
    movie.play(i)
    return movie

def generate_views_10():
    for i in range (10):
        print(generate_views())
   
def top_titles():
    print(f'Najpopularniejsze filmy i seriale dnia: {str(date.today())}')
    selected = [x for x in movies if isinstance(x, Film)]
    if movies == Film:
        selected = sorted(get_movies(), lambda x: x.liczba_odtworzeń, reverse=True)
    elif movies == Serial:
        selected = sorted(get_series(), lambda x: x.liczba_odtworzeń, reverse=True)
    print(selected[:3]) #pierwsze 3 elementy    

  
if __name__ == '__main__':
    print(entry_start)

    movies = [
        Film('Jurassic Park', '1993', 'thriller'),
        Film('Terminator','1988','thriller'),
        Film('Superman', '1988', 'action'),
        Film('Batman','1989','action'),
        Film('Rainman', '1974', 'drama'),
        Serial('8','1', 'Przyjaciele','1994','serial'),
        Serial('8','2','Przyjaciele','1994','serial')
        ]    

    for movie in movies:
        print(movie)
        
    generate_views()
    print('\n\nTUTAJ funkcja get_movies')
    get_movies()
    print('\n\nTUTAJ funkcja get_series')
    get_series()
    print('\n\nTUTAJ funkcja generate_views')
    print(generate_views()) 
    print('\n\nTUTAJ funkcja generate_views_10')
    generate_views_10()
    print('\n\nTUTAJ funkcja top_titles')
    top_titles()
    print('\n\nTUTAJ funkcja search_movie')
    print(search_movie())