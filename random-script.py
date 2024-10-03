from random import randint

NUMBER_OF_USERS = 100_000

categories = {
    "Grammar": ["Pronoun Error", "Tense Error", "Adverb Error"],
    "Vocabulary": ["Word Usage Error", "Mispronunciation"],
    "Pronunciation": ["xyz", "abc"],
    "Fluency": ["Speech not coherent", "Hesitation"]
}

with open("init.sql", 'w') as f:
    f.write("CREATE DATABASE stimuler;\n\n")
    f.write("\\c stimuler\n\n")
    f.write("""CREATE TABLE IF NOT EXISTS user_errors (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        category VARCHAR(255) NOT NULL,
        sub_category VARCHAR(255) NOT NULL,
        frequency INT DEFAULT 1,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT category_types CHECK (category IN ('Grammar', 'Vocabulary', 'Pronunciation', 'Fluency')),
        CONSTRAINT unique_error UNIQUE (user_id, category, sub_category)
    );\n\n""")
    f.write("INSERT INTO user_errors(id, user_id, category, sub_category, frequency, last_updated) VALUES\n")
    
    cnt = 0
    for i in range(NUMBER_OF_USERS):
        for key, type in categories.items():
            for val in type:
                row = f"({cnt}, {i}, '{key}', '{val}', {randint(1,50)}, NOW()),\n"
                f.write(row)
                cnt += 1
    
    row = f"({cnt}, -1, 'Grammar', 'val', {randint(1,50)}, NOW());\n"
    f.write(row)
    f.write("CREATE INDEX idx_name ON user_errors(user_id);\n")
    
    print(cnt, " rows written")