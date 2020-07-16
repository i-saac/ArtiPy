# ArtiPy  
A drawing class that makes it easier to draw using python code!  

# How to Use:  
First, initialize the Drawing class by using this line:  
drawing = Drawing((WIDTH, HEIGHT), title='TITLE', canvas_color='TKINTER COLOR NAME')  
Then, create a function that you want to continuously run to draw things on your canvas  
Then, call drawing.draw(FUNCTION_NAME) and your function will be continuously called  

# Drawing Features:  
drawing.draw_circle((CENTER_X, CENTER_Y), RADIUS, color='TKINTER COLOR NAME', fill='TKINTER COLOR NAME', line_width=int>0)  
Draws a circle centered at (CENTER_X, CENTER_Y) with radius RADIUS  

drawing.draw_line((START_X, START_Y), (END_X, END_Y), color='TKINTER COLOR NAME', line_width=int>0)  
Draws a line starting at (START_X, START_Y) and ending at (END_X, END_Y)  

drawing.draw_rect((X, Y), (WIDTH, HEIGHT), color='TKINTER COLOR NAME', fill='TKINTER COLOR NAME', line_width=int>0)  
Draws a rectangle with top left corner at (X, Y) with width WIDTH and height HEIGHT  

drawing.translate((NEW_X, NEW_Y))  
Sets the new drawing origin to be (NEW_X, NEW_Y)  

drawing.rotate(RADIANS)  
Rotates all future drawings clockwise around the origin by RADIANS radians  

drawing.push()  
Saves current origin and rotation orientation for future callbacks by pop(), can be called multiple times to save multiple orientations

drawing.pop()
Loads most recently saved origin and rotation orientation, and deletes that orientation from the list so in the future previous saved orientations will be called
