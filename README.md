# dojo_lang_detector

The objective of this kata is to label wikipedia articles with their
languages.

To achieve this training and tests data are provided in this repository
with their schemas documented below.

To get a score on the dojo leaderboard, your script will have to be able to
take a filename of a test dataset and generate an answer file.

i.e:

  python label_articles.py test_200.json > team_n_answers.json

Then the grading.py script is going to be used to get the official dojo score.

## Files schema

## lang_train.json

Label training dataset as a jsonl file containing objects with the
following schema:

1. text  
UTF-8 extract from wikipedia articles, cleared of HTML tags.
2. lang  
iso code of the language in the extract.
3. subject  
the wikipedia subject of the language of the extract

## train_*.json

Another label training dataset as a jsonl file containing objects with the
same schema as lang_train.json but in which the text is only 100 or 200
characters from the middle of the article.

## test_100.json

Unlabel label test dataset as a jsonl file containing objects with the
following schema:

1. text  
100 characters long UTF-8 extract from wikipedia articles, cleared of HTML
    tags. 
2. example
Number of the example.

## random_solution_answers.json

Example answer file
following schema:

1. text  
100 characters long UTF-8 extract from wikipedia articles, cleared of HTML
    tags. 
2. example
Number of the example.

The objective of the kata is to create a script that will take the grading data
set and generate an answer files


## languages.json

A json object containing the mapping between the languages iso codes and their
human names.

