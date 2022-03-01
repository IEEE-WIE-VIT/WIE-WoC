# GAME DEV IN PYTHON

Creating your own computer games in Python is a great way to learn the language. To build a game, you’ll need to use many core programming skills. The kinds of skills that you’ll see in real-world programming. In game development, you’ll use variables, loops, conditional statements, functions, object-oriented programming, and a whole bunch of programming techniques and algorithms. As a plus, you’ll have the satisfaction to play the game you’ve just created! In the Python ecosystem, you’ll find a rich set of tools, libraries, and frameworks that will help you create your games quickly. While Python makes learning to code more accessible for everyone, the choices for video game writing can be limited, especially if you want to write arcade games with great graphics and catchy sound effects. For many years, Python game programmers were limited to the pygame framework. Now, there’s another choice.

### arcade library
The arcade library is a modern Python framework for crafting games with compelling graphics and sound. Object-oriented and built for Python 3.6 and up, arcade provides the programmer with a modern set of tools for crafting great Python game experiences. The arcade library was written by Paul Vincent Craven, a computer science professor at Simpson College in Iowa, USA. As it’s built on top of the pyglet windowing and multimedia library, arcade features various improvements, modernizations, and enhancements over pygame:

- Boasts modern OpenGL graphics
- Supports Python 3 type hinting
- Has better support for animated sprites
- Incorporates consistent command, function, and parameter names
- Encourages separation of game logic from display code
- Requires less boilerplate code
- Maintains more documentation, including complete Python game examples
- Has a built-in physics engine for platform games

### Pygame
Pygame is a Python wrapper for the SDL library, which stands for Simple DirectMedia Layer. SDL provides cross-platform access to your system’s underlying multimedia hardware components, such as sound, video, mouse, keyboard, and joystick. pygame started life as a replacement for the stalled PySDL project. The cross-platform nature of both SDL and pygame means you can write games and rich multimedia Python programs for every platform that supports them! 

Writing code that runs in the terminal or in your web browser is good fun. Writing code that affects the real world, however, can be satisfying on a whole other level. Writing this sort of code is called embedded development, and Python is making it more accessible than ever!

### What Is Embedded Development?
Embedded development is writing code for any device that isn’t a general-purpose computer. This definition is a little bit ambiguous, so some examples might help:

General-purpose computers include laptops, desktop PCs, smartphones, and so on.
Embedded systems include washing machines, digital machines, robots, and so on.

### BBC micro:bit
The BBC micro:bit is an embedded system designed for educational use. On board a micro:bit, there are lots of components, including buttons, a 5x5 LED screen, a speaker and microphone, an accelerometer, and a Bluetooth module. Unfortunately, the Bluetooth module is unusable with Python, but you can still use the radio directly. It’s programmable in Scratch, JavaScript, and most importantly, Python.

### Raspberry Pi
Most Raspberry Pis are technically single-board computers instead of embedded systems, but they all still allow access to external hardware through their GPIO pins. One exception to the rule is the Raspberry Pi Pico, which is a microcontroller development board. Other Raspberry Pis run Linux, meaning that you can use them as a full computer, and all Pis support Python right out of the box.

### pyboard
The pyboard is an electronics development board that is designed to run MicroPython. It’s a lot more powerful than a micro:bit but comes without any extra goodies like the on-board screen and sensors of the micro:bit.

### MicroPython
MicroPython is the de facto standard embedded Python implementation. It is a Python 3.x implementation designed to run on microcontrollers. It is not 100 percent CPython-compatible, but it is very close. This means that if you have written code to run on versions up to Python 3.4, then there’s a good chance you can get it to run in MicroPython.

### CircuitPython
CircuitPython is a fork of MicroPython that supports a slightly different list of boards and has some changes to make it more friendly to beginners. For the most part, your experience will be very similar when using CircuitPython as it will when using MicroPython. You might choose to use CircuitPython if your board only supported it and not other implementations.
