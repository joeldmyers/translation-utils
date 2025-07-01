# translation-utils

The idea here was to take in a long text in German and produce flashcards of vocabulary from it. 

The goal is to improve my vocabulary in German in a specific domain. 

To do this, I did the following: 

1. Loaded the podcast "Von Assur Nach Babylon" on a Mac
2. Ripped the transcript: 

    a. open the transcript in podcast app on mac, 
    
    b. go to ~/Library/Group Containers/243LU875E5.groups.com.apple.podcasts/Library/Cache/Assets/TTML and grab the file and then 
    
    c. use this rip.html in this folder to convert it to txt file.
  
3. Combined all transcripts into one txt file manually (only 7 files, could write a script)
4. Then take the "Dedupe lemmatized words" to get a list of unique word lemmas. (important since German is declined, so otherwise we would get gut, guter, gutes, when we just want gut)
5. Then take "translate german csv" to translate the words.

You can then load Anki app on a Mac and import these using a CSV. 

This was inspired by realizing that I would like to know this domain vocabulary around Ancient Near East Studies in German better, but it's challenging to learn. This is a quick way to essentially convert a text into translated flashcards.