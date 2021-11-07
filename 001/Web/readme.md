# about this folder
Mainly for exploring of web.py and python, i have been doing .net for about 15 years on (.net webforms, .net mvc, and now .net core) and before that (classic asp). In my work of web development, i have came across python script for jobs, while the syntax looked familiar but some thing are just not, so i decided to pick up python with a popular course on udemy. There was a python script at work that uses web.py, and i needed to modify it, but i had no idea how it worked and it was simply amazing, a few lines of code and a single python script was a web server! So this is my exploration forcusing with Python, web.py and youtubedl python library.


# about the project
1. form.py
* on load it shows a form for you to paste in the youtube url
* using youtubedl, it will get the stream info and direct user to a page (using tempates) where u can see the videi
* you can also see the different streams available, 
* each stream 'format id' is clickable and u can then switch to that stream and it plays it

2. index.py
* learning page on passing list to templates

# todo
* split format table to (audio, video & both)
    * audio: (formatid, size, codec, extension)
    * video: (formatid, size[width, height], codec, extension)
    * both: (formatid, size[width, height], codec (audio, video), extension)
* make the stream to be beside the video so when we switch we can see the change, 
    * maybe make it a ddl
* add the video width and height option and use JS to resize the video the smaller size.
* add ability 2 pull videos from the author of current video and or video search (will require youtube api)


