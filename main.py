from tkinter import *

text = ("Once upon a time, in a realm where the skies shimmer with myriad hues and the seas whisper secrets of the universe, "
        "there embarked a young explorer named Eliana. Her heart brimmed with unquenchable curiosity and a thirst for discovery "
        "that no map could satisfy. Eliana's vessel, The Starbound, was no ordinary ship. Crafted from the heartwood of the ancient "
        "Whistling Pines and blessed by the winds of fortune, it glided over the waters like a dream through the night.")

test_time = 30
countdown_id = None
def on_key_press(event):
    global timer_started
    if not timer_started:
        timer_started = True
        countdown(test_time)

def countdown(time_left):
    global countdown_id
    if time_left > -1:
        timer_label.config(text=f"Time left: {time_left}s")
        countdown_id = window.after(1000, countdown, time_left-1)
    else:
        on_timeout()

def on_timeout():
    entry.configure(state='disabled')
    user_input = entry.get("1.0", "end-1c").strip()
    input_length = len(user_input)
    provided_text_segment = text[:input_length]

    correct_chars = sum(
        1 for i, char in enumerate(user_input) if i < len(provided_text_segment) and char == provided_text_segment[i])

    accuracy = (correct_chars / input_length) * 100 if input_length > 0 else 0

    words_typed = len(user_input.split())
    wpm_count = (words_typed * 60) / test_time

    wpm.config(text=f"Words Typed: {words_typed}, WPM: {wpm_count}, Accuracy: {accuracy:.2f}%")

def restart():
    global timer_started
    timer_started = False
    entry.configure(state='normal')
    entry.delete("1.0", END)
    timer_label.config(text="Time left: 30s")
    wpm.config(text="Words Typed: 0, WPM: 0, Accuracy: 0%")
    window.after_cancel(countdown_id)


window = Tk()
window.title("Typing Speed Test")
window.config(pady=10, padx=10)

timer_started = False
timer_label = Label(window, text="Time left: 30s", font=("Ariel", 18))
timer_label.pack()

restart = Button(text="Restart", command=restart)
restart.pack()

test_text = Label(window, text=text, wraplength=650, font=("Ariel", 18))
test_text.pack(pady=10)

entry = Text(window, width=60, height=15, font=("Ariel", 18))
entry.pack()
entry.bind("<KeyPress>", on_key_press)

wpm = Label(window, text="Words Typed: 0, WPM: 0", font=("Ariel", 18))
wpm.pack(side=LEFT)

window.mainloop()
