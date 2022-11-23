<div id="header" align="center">
	<h1>AirBnB clone</h1>
</div>

---

### Project Description:

This project is the first step to creating a clone of the [AirBnB Website](https://www.airbnb.com/).

To start, we would be creating a console which will enable us interact with the project by using some commands.

---


### Command interpreter:

To start it in interactive mode, simply run

```
$ ./console.py
```


To use it, type the desired command after the '(hbnb)' prompt

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But it also works in non-interactive mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
