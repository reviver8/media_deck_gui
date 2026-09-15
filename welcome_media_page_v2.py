from guizero import App, Text, Box, PushButton, Picture
from datetime import datetime as dt

FONT = "Helvetica"

app = App(title="Media Deck", width=960, height=540, layout="grid")
app.bg = "#3F3F3F"

top_pad = Box(app, grid=[0,0], height=20, width="fill")
top_pad.bg = app.bg
left_pad = Box(app, grid=[0,0], height="fill", width=15)
left_pad.bg = app.bg

# Clock section
clock_box = Box(app, layout="auto", grid=[1,1], height=216, width=app.width * 0.35)
clock_box.bg = "#FF9F1C"
clock_box_pad = Box(clock_box, layout="auto", height=clock_box.height *.25, width="fill")
clock_box_pad.bg = clock_box.bg
clock_text = Text(clock_box, text="Clock", size=32, bold=True, font=FONT)
clock_date_text = Text(clock_box, text="Date", size=24, font=FONT)

#  Clock functionality
def update_clock():
    current_time = dt.now().strftime("%H:%M:%S")
    clock_text.value = current_time
    clock_date_text.value = dt.now().strftime(" %a, %d %b, %Y")
    app.after(1000, update_clock)

top_middle_pad = Box(app, grid=[2,1], height="fill", width=30)
top_middle_pad.bg = app.bg

# Recent Media Display section
recent_media_display_box = Box(app, layout="auto", grid=[3,1,5,1], height=216, width=app.width * 0.58)
recent_media_display_box.bg = "#F15BB5"
recent_media_display_box_pad = Box(recent_media_display_box, layout="auto", height=recent_media_display_box.height * 0.10, width="fill")
recent_media_display_box_pad.bg = recent_media_display_box.bg
recent_media_display_text = Text(recent_media_display_box, text="Recent Media", bold=True, size=32, font=FONT)

recent_media_display_text_box = Box(recent_media_display_box, layout="grid", height=recent_media_display_box.height * 0.90, width="fill")
recent_media_display_text_box.bg = recent_media_display_box.bg
recent_media_top_pad = Box(recent_media_display_text_box, grid=[0,0], height=recent_media_display_text_box.height * 0.22, width="fill")
recent_media_top_pad.bg = recent_media_display_box.bg
recent_media_left_pad = Box(recent_media_display_text_box, grid=[0,1], height="fill", width=40)
recent_media_left_pad.bg = recent_media_display_box.bg

recent_media_movie_text = Text(recent_media_display_text_box, grid=[1,1,1,2], text="Movie: None", size=20, font=FONT)
recent_media_middle_left_pad = Box(recent_media_display_text_box, grid=[2,1], height="fill", width=20)
recent_media_middle_left_pad.bg = recent_media_display_box.bg
recent_media_tv_text = Text(recent_media_display_text_box, grid=[3,1,1,2], text="TV Show: None", size=20, font=FONT)
recent_media_middle_right_pad = Box(recent_media_display_text_box, grid=[4,1], height="fill", width=20)
recent_media_middle_right_pad.bg = recent_media_display_box.bg
recent_media_book_text = Text(recent_media_display_text_box, grid=[5,1,1,2], text="Book: None", size=20, font=FONT)
recent_media_right_pad = Box(recent_media_display_text_box, grid=[6,1], height="fill", width=40)
recent_media_right_pad.bg = recent_media_display_box.bg


top_right_pad = Box(app, grid=[9,1], height="fill", width=25)
top_right_pad.bg = app.bg
middle_pad = Box(app, grid=[0,2], height=20, width="fill")
middle_pad.bg = app.bg

# Gif section
gif_box = Box(app, layout="auto", grid=[1,3], height=app.height * 0.5, width=app.width * 0.35)
gif_box.bg = app.bg
gif_image = Picture(gif_box, image="assets/shrek_smirk.gif", height=int(gif_box.height), width=int(gif_box.width))

# Movie button section
def add_movie():
    title = app.question("Add Movie", "Movie title:")
    if title:
        recent_media_movie_text.value = f"Movie: {title}"

bottom_middle_left_pad = Box(app, grid=[2,3], height="fill", width=10)
bottom_middle_left_pad.bg = app.bg
movie_button_box = Box(app, layout="auto", grid=[3,3], height=gif_image.height, width=app.width * 0.25)
movie_button = PushButton(movie_button_box, image="assets/movie_icon.png", command=add_movie, height=gif_image.height, width=int(app.width * 0.25))
movie_button_box.bg = "#9B5DE5"


# TV button section
def add_tv_show():
    title = app.question("Add TV Show", "TV show title:")
    if title:
        recent_media_tv_text.value = f"TV Show: {title}"

bottom_middle_middle_pad = Box(app, layout="auto", grid=[4,3], height="fill", width=10)
bottom_middle_middle_pad.bg = app.bg
tv_button_box = Box(app, layout="auto", grid=[5,3], height=gif_image.height, width=app.width * 0.15)
tv_button = PushButton(tv_button_box, image="assets/tv_icon.png", command=add_tv_show, height=int(gif_image.height), width= int(app.width * 0.15))
tv_button_box.bg = "#00BBF9"

# Book button section
def add_book():
    title = app.question("Add Book", "Book title:")
    if title:
        recent_media_book_text.value = f"Book: {title}"

bottom_middle_right_pad = Box(app, layout="auto", grid=[6,3], height="fill", width=10)
bottom_middle_right_pad.bg = app.bg
book_button_box = Box(app, layout="auto", grid=[7,3], height=int(gif_image.height), width=app.width * 0.15)
book_button = PushButton(book_button_box, image="assets/book_icon.png", command=add_book, height=gif_image.height, width= int(app.width * 0.15))
book_button_box.bg = "#FEE440"

update_clock()
app.display()
