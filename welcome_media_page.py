from guizero import App, Text, Box, PushButton, Picture
def do_nothing():
    return 0

app = App(title="My app", height=300, width=300, layout="grid")
app.bg = "#7E7E7E"

#text = Text(app, text="Some text here", grid=[0,0])
box = Box(app, layout="grid", grid=[1,0])
clock_box = Box(box, layout="grid", grid=[0,0,3,2], width=200, height=100)
clock_box.bg = "#FF9F1C"

clock_text = Text(clock_box, text="Clock", grid=[0,0]) 

recent_media_display_text = Text(box, text="Recent Media", grid=[1,0,2,1])
recent_media_display_text.bg = "#F15BB5"
button3 = PushButton(box, command=do_nothing, text="3", grid=[5,0])

gif_image = Picture(box, image="assets\hi-res-shrek.gif", grid=[0,1]) #PushButton(box, command=do_nothing, text="4", grid=[0,1])
movie_button = PushButton(box, command=do_nothing, text="add movie", grid=[1,1,2,1], width=10, height=10)
movie_button.bg = "#9B5DE5"
tv_button = PushButton(box, command=do_nothing, text="add TV show", grid=[5,1,3,1], padx=5, width=5, height=10)
tv_button.bg = "#00BBF9"
book_button = PushButton(box, command=do_nothing, text="add book", grid=[9,1,3,1], padx=5,width=5, height=10)
book_button.bg = "#FEE440"
app.display()
