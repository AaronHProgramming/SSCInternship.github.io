# Aaron's 2015 Summer Internship
---
### How to check markdown against how it looks is easy: [dillinger.io](dillinger.io)

### To unstage all files from using git add (-A as well):
```sh
$ git reset
```

## Things I learned
1. Python
2. Linux (OS)
   - Using Bash
   - Understanding OS structure i.e. Kernel, distributions
3. Reading from files and manipulating data
4. Using a Database (MySQL)
   - Learned SQL
5. Linear Algebra
   * Least Squares
   * Matrix multiplication, addition, inversion, determinants
   * Signal Processing
6. Scheme syntax (Common Lisp, Clojure)
7. C
   - Pointers
8. HTML
9. CSS
   - [Available Colors](http://www.color-hex.com/color-names.html)
   - [Nice fonts](http://sixrevisions.com/resources/professional-clean-fonts-designs/)

## TODO:
1. Finish reading [this book](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_start).
2. [Learn HTML and CSS basics](http://learn.shayhowe.com/html-css/building-your-first-web-page/).
3. Learn [magic methods](http://rafekettler.com/magicmethods.html) in python.
4. Finish this [C tutorial](http://www.cprogramming.com/tutorial/c/lesson1.html)
5. Use [this](http://interactivepython.org/runestone/static/pythonds/index.html) site to learn python data structures and more.
6. Get [this book](http://www.amazon.com/Introduction-Algorithms-Edition-Thomas-Cormen/dp/0262033844).
7. Utilize [this course](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/), similar to Math 240, especially it's last chapter.
8. Read [this](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/) and understand Python.
9. Keep up with [Project Euler](https://projecteuler.net/sign_in).
  * Fix if __name__ == '__main__': to automatically submit the results to the project euler webpage.



## Awesome resource links!
  * [The Python Tutorial](https://docs.python.org/2/tutorial/index.html) is a huge dictionary of python functions and explanations.
  * To install LAMP on Linux Mint, use [this](http://community.linuxmint.com/tutorial/view/486).
  * In case I fall for a Python "gotcha", use [this](http://docs.python-guide.org/en/latest/writing/gotchas/).
  * Need tips on optimization? Use [this](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
  * Use Gilbert Strang and Khan Academy for linear algebra. Strang has a book called Introduction to Linear Algebra.
  * Important for [conventions and file sorting](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)

This picture from my mapping project show ship points rendered one at a time from a large source. (This picture doesn't show all of the source)
![pic here](/mapping/mapping_points.png)

This picture shows a clustered version of the previous mapping project because the rendering of each single image takes too long to display.
![hi scott](/mapping/mapping_cluster.png)


# Week one:	
Day one: I was taught Python from simple syntax to different methods that are useful such as len(), enumerate()

Day two: I learned about Linux and began reading about Generators, practiced python

Day three: I completed my prime number finder as a program and turned it into a generator and then adapted it to use the send() method, created a git account

Day four: I learned linear algebra. (ex. F(c(a + b)) = c(F(a) + F(b)).  I also learned python exception handling. As an exercise I coded how to calculate a dot product Xcomponent1 times Xcomponent2 + Ycomponent1 times Ycomponent2 = dot product.

Day five: I learned about decorators, functions that return functions. Worked on [random walks](Graphs/randomWalksAndExtra.ipynb).

# Week two:
Day six: I gained experience with linux, learned about how arrays work, created StackOverflow account, completed 2D random_walk program.

Day seven: Took introductory javascript tutorial, progressed on reading in csv and formatting as geojson, having big troubles with plotting

Day eight: Succeeded in plotting observations, cleaned up pycharm, 

Day nine: Consolidated files into folders and deleted useless files.

# Week three:
Day ten: Installed LAMP, learned about databases

Day eleven: Loaded AISdata into database

Day twelve: Went to Network Security event, made python code get specific selects from the MyPHPAdmin

Day thirteen: Made map get points from database instead of file. Learned about functions as paramaters.

Day fourteen: Transferred files from laptop to desktop. Redownloaded many things.

# Week four:
Day fifteen: Finished downloading everything. Fixed up dbconnect.py.

Day sixteen: I taught simple python syntax to the other interns, and helped Jake learn programming logic.

Days seventeen through twenty-two: Redid the first 3 weeks by helping interns.

# Week five:
Days twenty-three through twenty-six: Worked on a clump builder, and helped teach Max and Jake more

# Week six:
Day twenty-seven: Worked on clump builder, retaught linalg

Day twenty-eight: Worked on clump builder, retaught linalg

Day twenty-nine: Signal Processing

Day thirty: Spent hours updating and clarifying my README.md.

# Week seven:
Day thirty-one: Read Structure and Interpretation of Computer Programs

Day thirty-two: Completed signal processing and linear algebra program

# Week eight:
Read SICP
Worked on basic scheme and basic C programs.
Worked on program to write to and execute other programs in Python.

# Week nine:
Read SICP.
Worked on program to write to and execute other programs in Python.

# Week ten:
I worked on learning HTML and CSS.
Worked on figuring out permutations and combinations with replacement and without replacement.
Last day: Made a dual-boot on my laptop by adding Linux Mint, tried to install rEFInd (don't know if it did anything), used chkdsk and gparted to partition the memory.

# Specific commands in linux to remember:
sudo, cd, rm, mv, cp, ps, ls, |
```sh
$ ipython notebook
```
 to open general ipython notebook
 
```sh
$ ipython notebook file.ipynb
```
to open specific .ipynb
```sh
$ /opt/pycharm-community-4.5.1/bin/pycharm.sh
```
to open pycharm
```sh
$ xdg-open { file | URL }
```
Opens a file, or window in your browser
```sh
$ scheme --load path/filename
```
Executes a scheme program and enters the environment
```sh
$ sudo apt-get install xcalib
$ xcalib -i -a
```
Inverts the primary screen(-invert -alter)

You can alias commands to speed up typing

xdg-open --> cwin - "create window"

---

