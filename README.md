## White Noise
Plays white noise in the background with a few simple commands. 

## Commands
### Play random white noise

This command will allow the user to have mycroft randomly choose a white noise in it's library. The white noise can be played for a specified duration or a default duration if it isn't provided.  

Utterances available for playing a random white noise:  

"Play some white noise"  
"Play some white noise for {duration}"  
"Play white noise"  
"Play white noise for {duration}"  

{duration} could be said in seconds, minutes, or hours. If no duration is specified in the command, the default time will be 10 minutes.  


### Play white noise by title

This command will allow the user to choose and play any available white noise audio clips that mycroft has availble in it's library.  

Utterances available for playing white noise by title:  

"Play me {title}"   
"Play {title}"  

{title} has to be a title that mycroft already has in it's library. If no title is specified in the command, or if a title is not in the library, mycroft will politely respond with a "no title" message or a "no command" message.  

### List out white noises available

This command will list all the available white noise audio mp3 clips that mycroft has available in it's library.  

Utterances available for listing white noise titles available:  

"List white noises"   
"What white noises do you have"   
"What white noise do you have"   
"What do you have for white noise"   
