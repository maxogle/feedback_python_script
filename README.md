# feedback_python_script

Feedback is an audio analysis software built in python, for use in editing files, or providing a quick way to identify key points of an audiofile.  Feedback takes an audiofile finds the frequency value of each sample at a 44,100Hz rate, averages them, and then anylizes the file again against that average. Any value found to be at an extreme in comparison to that average is classified as an event and a clip of the event is then written. Thus cataloging it for the user to observe without having to listen to the whole file.  Events can be either high or low extremes, high(or loud) extremes are generally things like applause or loud laughter(best used to anaylize a speech or performance), low(or quiet) extremes are generally silence or dead air(best used for editing things like podcasts). 

This software is still buggy and a bit over-tuned at the moment. That being said i think it is a strong proof of concept, 
if you'd like to see the functionality for yourself simply run

"python3 audio6.py" in the directory then follow the instructions of the CLI 

if you then check the directory you'll see the program writing more files based on the data set it interprets 
