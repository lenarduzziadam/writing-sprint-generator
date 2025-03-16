#TODO: figure out imports for a project like this

class Writer:
    GENRES = ["sci-fi", "fantasy", "romance", "political", "historical fiction", "adventure", "action", "time-travel"]
    POVS = ["1st person", "2nd person", "3rd person", "mixed pov"]
    
    #time limit and word count should have the option to be specified by the writer, perhaps a dedicated genre, and pov choice feature could be 
    # beneficial as well
    #TODO: consider if you need all these parameters or simply word_count and time_limit, self is too useful to not use. 
    def __init__(self, genre, word_count, pov, time_limit)
        self.word_count = word_count
        self.time_limit = time_limit
        