# ♟️ Chess
A cool chess game that you can play with friends or alone against a robot.

## ⌨️ Inputs
To move your selection square, use the dedicated directional arrows.

To select a square, press the 'OK' or 'EXE' button. First, select the piece you want to move, and then select the destination square.

To give up, press the 'Shift' button. To request a draw, press the 'Alpha' button. After either of these inputs, a 3-second timer will start, allowing you to cancel if you change your mind.
##

## 📜 Rules
All classic chess rules are included, so check the rules online if you're not familiar with them!
##

## ℹ️ Information
If you select a piece but cannot see the possible moves, it means the move is illegal and cannot be performed.

The way to promote a piece is unique and straightforward to understand. I’m sure you’ll get it, though it might be surprising at first.

When you select a piece, you will see all its possible moves, helping you to better visualize your options.
##

## 🖥️ Requirements
This program is coded in MicroPython specifically for the NumWorks calculator, but it should work on a computer if you modify the module to be compatible with Python. However, you’ll also need to adjust the size of the squares to fit your screen; otherwise, the game may be difficult to play. Unfortunately, it won't work on the NumWorks site, though I'm not sure why.
##

## 💬 Language
It was coded on a NumWorks calculator in MicroPython.
##

## 🛠️ Details
You can adjust the timer duration by modifying the code at line 406. Change the value (currently set to 600 seconds) to allow 10 minutes per player. Don't forget to convert the time to seconds!

You can also set the AI to play as a specific side. To do this, modify line 17. If you’re playing with a friend, remove all AI controls, but if you want to play as black, leave the AI set to play the first turn by entering '1'.

The function to request a draw is currently disabled because the NumWorks calculator doesn't have enough memory to handle it. The code is present but commented out, so if you're using a computer, you can re-enable this function in a real environment (not on the NumWorks site). The same goes for functionalities like detecting a draw by repetition, insufficient material, or the "50-move rule."

Unfortunately, the interface is in French, but there’s not much text, so it should be easy to understand.

This project was started on May 17, 2023, and finished on August 15, 2024 (though I didn't work on it continuously for 15 months, of course).
##

#
