from tkinter import *
import  math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 25, "bold")
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.25
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", bg=YELLOW)
    tick_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60
    work_sec = 5
    short_break_sec = 2
    long_break_sec = 3

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW)
        count_down(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
        tick_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=FONT_NAME)
timer_label.grid(column=2, row=1)

tick_label = Label( bg=YELLOW, fg=GREEN, font=FONT_NAME)
tick_label.grid(column=2, row=4)

button_start = Button(text="Start", bg=GREEN, command=start_timer)
button_start.grid(column=1, row=3)

button_reset = Button(text="Reset", bg=GREEN, command=reset_timer)
button_reset.grid(column=3, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill="white", font=FONT_NAME)
canvas.grid(column=2, row=2)




window.mainloop()
