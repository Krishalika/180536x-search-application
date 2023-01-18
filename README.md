# Sinhala Songs Metaphor Search Engine
    A search application for metaphors of Sinhala songs.
    Completed as the Mini project of CS4642 - Data Mining & Information Retrieval.

# Start project
    1. Clone the project 
    2. Go to search-application/sinhala-song-metaphor-search-engine folder.
    3. Execute 'npm install' and install node modules. 
    4. Start application using 'npm start' and the project will open in http://localhost:3000/.
    5. Enter target domain in the search bar and hit 'Enter' button.

# Data
    Go to folder search-application/text-corpus.
    The corpus includes 116 metaphors of unique 101 Sinhala songs. 

# Metadata
    1. Title 
    2. Composer 
    3. Lyricist
    4. Singer
    5. Album
    6. Year
    7. Genre
    8. Lyrics
    9. Metaphor
    10. Source
    11. Target 
    12. Interpretation

# Usecases
    Basic search
    1. Search metaphors by target domain - search results contain metadata of songs with number of hits
    2. Can include proceeding and stop words with 'target' and still get the results.

    Advanced search
    Search results can be filtered by singer, composer and lyrisist.

# Indexing techniques
    Used Elasticsearch analysers for indexing.
