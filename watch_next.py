# The module 'spaCy' is imported.
import spacy 
nlp = spacy.load('en_core_web_md')

# The function takes in a list of movies and returns a movie most similar to the 
# input description. 
def select_movie(movie_desc, movielist):
    movie_desc_compare = nlp(movie_desc)
    similarity = ""
    for movie in movielist: 
        similarity_movie = nlp(movie).similarity(movie_desc_compare)
        if similarity_movie > nlp(similarity).similarity(movie_desc_compare):
            similarity = movie
    return similarity.split(':')[0].strip()

# The movie title and description are assigned to variables here.
movie_title = "Planet Hulk"
movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# The file is read and appended to a list of movies. 
with open ('movies.txt', 'r') as file:
    movies = [] 
    for line in file: 
        movies.append(line)

# Output statement declaring which movie to watch next. 
print(f"You have just finished watching Planet Hulk. You should watch {select_movie(movie_description, movies)} next.")

