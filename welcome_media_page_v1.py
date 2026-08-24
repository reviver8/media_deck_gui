from guizero import App, Text, Box, PushButton, Picture
import os
#from PIL import Image
def do_nothing():
    return 0

app = App(title="My app", width=960, height=540,layout="grid")
app.bg = "#7E7E7E"

top_pad = Box(app, grid=[0,0], height=20, width="fill")
left_pad = Box(app, grid=[0,0], height="fill", width=20)

#text = Text(app, text="Some text here", grid=[0,0])
clock_box = Box(app, layout="auto", grid=[1,1], height=216, width=app.width * 0.35)
clock_text = Text(clock_box, text="Clock", height=100, width=200)
clock_box.bg = "#FF9F1C"

top_middle_pad = Box(app, grid=[2,1], height="fill", width=30)

recent_media_display_box = Box(app, layout="auto", grid=[3,1,5,1], height=216, width=app.width * 0.55)
recent_media_display_text = Text(recent_media_display_box, text="Recent Media", height=100, width=200)
recent_media_display_box.bg = "#F15BB5"

top_right_pad = Box(app, grid=[4,1], height="fill", width=20)
middle_pad = Box(app, grid=[0,2], height=20, width="fill")

gif_box = Box(app, layout="auto", grid=[1,3], height=app.height * 0.5, width=app.width * 0.35)
gif_image = Picture(gif_box, image="assets\hi-res-shrek.gif", height=int(gif_box.height), width=int(gif_box.width))

# movie_img_path = os.path.abspath("assets\movie icon image.png")
# img = Image.open(movie_img_path)

bottom_middle_left_pad = Box(app, grid=[2,3], height="fill", width=10)
movie_button_box = Box(app, layout="auto", grid=[3,3], height=gif_image.height, width=app.width * 0.25)
movie_button = PushButton(movie_button_box, text="add movie", command=do_nothing, height=100, width=100)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# image_path = os.path.join(BASE_DIR, "assets", "movie icon image.png")
# print(image_path)

#movie_button_image = Picture(movie_button_box, image=os.path.abspath("assets\hi-res-shrek.gif"), height=10, width=10)
movie_button_box.bg = "#9B5DE5"

bottom_middle_right_pad = Box(app, grid=[4,3], height="fill", width=2)
tv_button_box = Box(app, layout="auto", grid=[5,3], height=gif_image.height, width=app.width * 0.15)
tv_button = PushButton(tv_button_box, command=do_nothing, text="add TV show", height=40, width=20)
tv_button_box.bg = "#00BBF9"

bottom_right_pad = Box(app, grid=[6,3], height="fill", width=2)
book_button_box = Box(app, layout="auto", grid=[7,3], height=gif_image.height, width=app.width * 0.15)
book_button = PushButton(book_button_box, command=do_nothing, text="add book", height=40, width=20)
book_button_box.bg = "#FEE440"

# tv_button = PushButton(app, command=do_nothing, text="add TV show", grid=[5,1,3,1], padx=5, width=5, height=10)
# tv_button.bg = "#00BBF9"
# book_button = PushButton(app, command=do_nothing, text="add book", grid=[9,1,3,1], padx=5,width=5, height=10)
# book_button.bg = "#FEE440"

# print(os.path.abspath("assets\hi-res-shrek.gif"))
# print(os.path.exists("assets\movie icon image.png"))


app.display()
