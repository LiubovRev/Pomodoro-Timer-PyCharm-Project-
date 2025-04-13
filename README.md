Pomodoro Timer App
Overview

This is a simple Pomodoro Timer application built using Python's tkinter library. The Pomodoro technique is a time management method that uses intervals of work and short breaks to maximize productivity. This app helps users track their work and break sessions with an interactive timer.
Features

    Work Timer: Work intervals are set with a fixed duration (e.g., 5 seconds for demonstration).

    Break Timer: Short and long breaks are available, switching between work and breaks automatically.

    Visual Feedback: During work sessions, a tomato image is displayed, and the screen shows elapsed time in a MM:SS format.

    Progress Marking: After each work session, a check mark (✓) appears to indicate completed work sessions.

Constants and Timer Configuration

    Work Time: WORK_MIN = 0.5 (minutes)

    Short Break: SHORT_BREAK_MIN = 0.1 (minutes)

    Long Break: LONG_BREAK_MIN = 0.25 (minutes)

Note: The duration of each session has been reduced for demonstration purposes. In a production environment, the timer values can be adjusted to your preference.
Functions
1. reset_timer()

Resets the timer back to "00:00", stops any ongoing countdowns, and clears the progress marks.
2. start_timer()

Starts the Pomodoro timer. It checks if the user is on a work session, short break, or long break, and triggers the countdown accordingly.
3. count_down(count)

This function is responsible for updating the timer every second. Once the countdown finishes, the timer either continues to the next session or marks the completion of a work session with a check mark.
UI Elements

    Labels: Show current session type ("Work", "Short Break", "Long Break") and the countdown timer.

    Buttons:

        "Start": Starts the timer.

        "Reset": Resets the timer to its initial state.

    Canvas: Displays a tomato image, with a countdown timer centered in the image.

Setup and Run Instructions

    Install Python and Tkinter if not already installed.

    Download the project files and place the tomato image (tomato.png) in the same directory as the script.

    Run the script using Python:

python pomodoro_timer.py

