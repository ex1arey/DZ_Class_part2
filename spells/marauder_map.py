from title import films_awards
import DZ13_Files
import json
class MapMagic:
    def __init__(self):
        self.__map_open = "I solemnly swear that I am up to no good."
        self.__map_close = "Mischief managed."

    def reveal_map(self):
        return self.__map_open

    def hide_map(self):
        return self.__map_close

class MarauderMap(MapMagic):
    __films_titles = {
        "tt1201607": "Harry Potter and the Deathly Hallows: Part 2",
        "tt0241527": "Harry Potter and the Sorcerer's Stone",
        "tt0926084": "Harry Potter and the Deathly Hallows: Part 1",
        "tt0304141": "Harry Potter and the Prisoner of Azkaban",
        "tt0417741": "Harry Potter and the Half-Blood Prince",
        "tt0295297": "Harry Potter and the Chamber of Secrets",
        "tt0330373": "Harry Potter and the Goblet of Fire",
        "tt0373889": "Harry Potter and the Order of the Phoenix"
    }

    def get_title_by_imdb_id(self, imdb_id):
        return MarauderMap.__films_titles.get(imdb_id)


with open('films_awards.json', 'w') as f:
    json.dump(films_awards, f)

class FilmsAwards:
    def __init__(self, path):
        self.path = path
        with open(path, 'r') as f:
            self.films_awards = json.load(f)

class MarauderMap:
    def __init__(self, path):
        self.path = path
        self.map_open = MapMagic().map_open
        self.map_close = MapMagic().map_close

    def map_generator(self):
        print(self.map_open)
        films_awards_obj = FilmsAwards(self.path)
        for award in films_awards_obj.films_awards[0]['results']:
            award_name = award['award_name']
            award_year = award['year']
            movie_title = award['movie']['title']
            print(f"{award_name} ({award_year}): {movie_title}")
        print(self.map_close)

my_map = MarauderMap("DZ13_Files")
my_map.map_generator()