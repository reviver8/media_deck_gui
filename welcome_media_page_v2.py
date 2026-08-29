from guizero import App, Text, Box, PushButton, Picture
from datetime import datetime as dt

def do_nothing():
    return 0

app = App(title="My app", width=960, height=540,layout="grid")
app.bg = "#3F3F3F"

top_pad = Box(app, grid=[0,0], height=20, width="fill")
left_pad = Box(app, grid=[0,0], height="fill", width=15)

# Clock section
clock_box = Box(app, layout="auto", grid=[1,1], height=216, width=app.width * 0.35)
clock_box_pad = Box(clock_box, layout="auto", height=clock_box.height *.25, width="fill")
clock_text = Text(clock_box, text="Clock", size=32, bold=True, )
clock_date_text = Text(clock_box, text="Date", size=24)
clock_box.bg = "#FF9F1C"

#  Clock functionality
def update_clock():
    current_time = dt.now().strftime("%H:%M:%S")
    clock_text.value = current_time
    clock_date_text.value = dt.now().strftime(" %a, %d %b, %Y")
    app.after(1000, update_clock)

top_middle_pad = Box(app, grid=[2,1], height="fill", width=30)

# Recent Media Display section
recent_media_display_box = Box(app, layout="auto", grid=[3,1,5,1], height=216, width=app.width * 0.58)
recent_media_display_box.bg = "#F15BB5"
recent_media_display_box_pad = Box(recent_media_display_box, layout="auto", height=recent_media_display_box.height * 0.10, width="fill")
recent_media_display_text = Text(recent_media_display_box, text="Recent Media", bold=True, size=32)

recent_media_display_text_box = Box(recent_media_display_box, layout="grid", height=recent_media_display_box.height * 0.90, width="fill")
recent_media_top_pad = Box(recent_media_display_text_box, grid=[0,0], height=recent_media_display_text_box.height * 0.22, width="fill")
recent_media_left_pad = Box(recent_media_display_text_box, grid=[0,1], height="fill", width=40)

recent_media_movie_text = Text(recent_media_display_text_box, grid=[1,1,1,2], text="Movie: None", size=18)
recent_media_middle_left_pad = Box(recent_media_display_text_box, grid=[2,1], height="fill", width=20)
recent_media_tv_text = Text(recent_media_display_text_box, grid=[3,1,1,2], text="TV Show: None", size=18)
recent_media_middle_right_pad = Box(recent_media_display_text_box, grid=[4,1], height="fill", width=20)
recent_media_book_text = Text(recent_media_display_text_box, grid=[5,1,1,2], text="Book: None", size=18)
recent_media_right_pad = Box(recent_media_display_text_box, grid=[6,1], height="fill", width=40)


top_right_pad = Box(app, grid=[9,1], height="fill", width=25)
middle_pad = Box(app, grid=[0,2], height=20, width="fill")

# Gif section
gif_box = Box(app, layout="auto", grid=[1,3], height=app.height * 0.5, width=app.width * 0.35)
gif_image = Picture(gif_box, image="assets/shrek_smirk.gif", height=int(gif_box.height), width=int(gif_box.width))

# Movie button section
bottom_middle_left_pad = Box(app, grid=[2,3], height="fill", width=10)
movie_button_box = Box(app, layout="auto", grid=[3,3], height=gif_image.height, width=app.width * 0.25)
movie_button = PushButton(movie_button_box, image="assets\movie_icon.png", command=do_nothing, height=gif_image.height, width=int(app.width * 0.25))
movie_button_box.bg = "#9B5DE5"


# TV button section
bottom_middle_middle_pad = Box(app, layout="auto", grid=[4,3], height="fill", width=10)
tv_button_box = Box(app, layout="auto", grid=[5,3], height=gif_image.height, width=app.width * 0.15)
tv_button = PushButton(tv_button_box, image="assets/tv_icon.png", command=do_nothing, height=int(gif_image.height), width= int(app.width * 0.15))
tv_button_box.bg = "#00BBF9"

# Book button section
bottom_middle_right_pad = Box(app, layout="auto", grid=[6,3], height="fill", width=10)
book_button_box = Box(app, layout="auto", grid=[7,3], height=int(gif_image.height), width=app.width * 0.15)
book_button = PushButton(book_button_box, image=r"assets\book_icon.png", command=do_nothing, height=gif_image.height, width= int(app.width * 0.15))
book_button_box.bg = "#FEE440"

update_clock()
app.display()

