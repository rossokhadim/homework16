import spells.func as func
class MapMagic:
    map_open = "I solemnly swear that I am up to no good."
    map_close = "Mischief managed."
    #path = str()
    # path = 'D:/PyCharm/pythonProject19/data.json'


class MarauderMap(MapMagic):

    __films_titles = {
    "results": [
            {
                "imdb_id": "tt1201607",
                "title": "Harry Potter and the Deathly Hallows: Part 2"
            },
            {
                "imdb_id": "tt0241527",
                "title": "Harry Potter and the Sorcerer's Stone"
            },
            {
                "imdb_id": "tt0926084",
                "title": "Harry Potter and the Deathly Hallows: Part 1"
            },
            {
                "imdb_id": "tt0304141",
                "title": "Harry Potter and the Prisoner of Azkaban"
            },
            {
                "imdb_id": "tt0417741",
                "title": "Harry Potter and the Half-Blood Prince"
            },
            {
                "imdb_id": "tt0295297",
                "title": "Harry Potter and the Chamber of Secrets"
            },
            {
                "imdb_id": "tt0330373",
                "title": "Harry Potter and the Goblet of Fire"
            },
            {
                "imdb_id": "tt0373889",
                "title": "Harry Potter and the Order of the Phoenix"
            }
        ]
    }

    path = str()
    def __init__(self, way):
        self.path = way

    def map_generator(self):
        print(self.map_open)

        func.Harry()

        print(self.map_close)







