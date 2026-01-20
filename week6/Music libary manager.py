# create empty data structure
songs = []
genre_count = {}

print("Welcome to Music Library Manager!")

# loop to collect 5 songs
for i in range(5):
    print(f"Enter Song {i+1}:")
    name = input("Song name: ")
    genre = input("Genre: ")
    
    # store as tuple and add to list
    songs.append((name, genre))
    
    # update genre count using .get()
    current_count = genre_count.get(genre, 0)
    genre_count[genre] = current_count + 1

# display results
print("\n=== YOUR MUSIC LIBRARY ===")
index = 1
for song in songs:
    print(f"{index}. {song[0]} ({song[1]})")
    index += 1

print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} songs")

# find most popular genre
most_popular = max(genre_count, key=genre_count.get)
print(f"Most popular genre: {most_popular}")