import spacy

nlp = spacy.load("en_core_web_md")

# Use NER to determine the movie titles
movie_titles = []
with open("movies.txt", "r") as f:
    for line in f:
        doc = nlp(line)
        for ent in doc.ents:
            if ent.label_ == "WORK_OF_ART":
                movie_titles.append(ent.text)

#set variable to compare against movie list
hulk = ( "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk in to a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

#compare movies to see which in the list would be closest to the hulk
max_similarity = -1
most_similar_movie = ""
hulk_doc = nlp(hulk)
for movie_title in movie_titles:
    movie_doc = nlp(movie_title)
    similarity = hulk_doc.similarity(movie_doc)
    if similarity > max_similarity:
        max_similarity = similarity
        most_similar_movie = movie_title

print("We recommend you watch this one next:", most_similar_movie.strip())

