from PIL import Image, ImageFilter, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog


def watermark_adding(in_images, text, opacity, filepath):
    global out
    n = 1
    # open the image as an object
    for in_image in in_images:
        with Image.open(in_image).convert("RGBA") as base:
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

            # get the font size
            w, h = base.size
            x, y = int(w / 4.5), int(h / 1.08)
            font_size = (w + h) / 40

            # get a font
            font = ImageFont.truetype("calibri.ttf", int(font_size))

            # get a drawing context
            draw = ImageDraw.Draw(txt)

            # add the watermark
            draw.text((x, y), text, fill=(0, 0, 0, opacity), font=font, anchor="ms")

            out = Image.alpha_composite(base, txt)
            if len(in_images) > 1:
                out.save(filepath + "/" + entry_for_filename.get() + str(n) + ".png")
                n += 1
            else:
                out.save(filepath + "/" + entry_for_filename.get() + ".png")


def browse_files():
    global filenames
    filenames = filedialog.askopenfilenames()
    text_list = []
    for filename in filenames:
        filename = "File Opened: " + filename
        text_list.append(filename)
    label_file_explorer.configure(text="\n".join(text_list))


# create the function for asking directory
def ask_directory():
    global path
    path = filedialog.askdirectory()
    label_for_directory.config(text=path)



# create window from TK class
window = tk.Tk()
window.title("Watermarking")
padx = 30
pady = 15


# Python program to create
# a file explorer in Tkinter
label_file_explorer = tk.Label(window, text="File Explorer using Tkinter",
                               width=100,
                               height=4,
                               fg="blue")

button_explore = tk.Button(window, text="Browse Files", command=lambda: browse_files())

entry_for_watermark_text = tk.Entry(window)

button_add_mark = tk.Button(window,
                            text="Add Watermark",
                            command=lambda: watermark_adding(filenames, entry_for_watermark_text.get(),
                                                             int(opacity_scale.get() * 2.25),
                                                             filepath=path)
                            )

opacity_scale = tk.Scale(window,
                         from_=0,
                         to=100,
                         orient="horizontal")

# ask for directory
button_for_directory = tk.Button(window,
                                 text="Change",
                                 command=ask_directory)

label_for_directory = tk.Label(window,
                               text="")

entry_for_filename = tk.Entry(window)

# Grid method

label_file_explorer.grid(column=1, row=1, padx=padx, pady=pady)

button_explore.grid(column=1, row=2, padx=padx, pady=pady)

entry_for_watermark_text.grid(column=1, row=3, padx=padx, pady=pady)

opacity_scale.grid(column=1, row=4, padx=padx, pady=pady)

label_for_directory.grid(column=1, row=5, padx=padx, pady=pady)

button_for_directory.grid(column=1, row=6, padx=padx, pady=pady)

entry_for_filename.grid(column=1, row=8, padx=padx, pady=pady)

button_add_mark.grid(column=1, row=9, padx=padx, pady=pady)

# Run the tkinter
window.mainloop()

