### COMPUTER TOOLS FOR DATA ANALYSIS

## SEP 10

-Relative paths are better according to Cecile to write in scripts as
the configuration of my files and directories might change.

-No spaces in your names!
no sapeces for variables or for files, directories. It makes it very confusing
when you are trying to call something, remove something or manipulate 
something from the command line

Ways of naming your files withput spaces 
RawSequences: Camel case
raw_sequences: Snabe case

Command
history - displays all the commands that I have ran in history
!(number) - e.g !180 - shows me which command was number 180 in the history and runs it

jenny brians stat 545 British Columbia
See Computer tools for data analysis resources

## SEP 12

Homework for Monday, excercise 1 on Canvas 

-I have to do pipes and filters because I didnt do it :)
-Uniq command is going to eliminate the adjacent repeted data 
-Control + C abort the command
-Control + D also gets me out of the command when it is waiting for my input

Command: 
echo "asdasdasdasd" | wc -c 
wc -c "asdasdasdad" to count the number of characters in that sentence

To get back to the beggining of the command: Control + A
To get to the end of the command: Control + e

1 character is 1 byteS
-If I press tab at the beggining of the command it would not show me or 
complete the name of the file because it needs a command first
instead it will show me commands that might start like that 


Files dont need to have an extension to work. Extensions are for humans. 
.sh is the extension for "Shell script". To run it from the command line you can do :
bash myscript.sh

For the excercise see: http://cecileane.github.io/computingtools/pages/notes0915.html

When I use > to create an output it only saves the real output (not the error messages)

To redirect potential errors to an output: 2> file.txt 

To get both the error and the output &> file.txt

tail -f will look at the tail of a file while it grows, it will continue to show the tail
at real time 

After pausing with Control + Z

- fg  to run the program in the frontground

- bg to run the program in the background

ps shows me the processes that are running 
- PID Process ID - Useful if you want to kill a specific processes
kill -9 71444 (the number indicates how bad you want to kill it q being the smallest)
ps -u ane (shows all the precesses in the computer, not only in the terminal)

ps -u ane | grep "Visual" - it will look for a process name Visual


to run something in the background from the beggining use & at the end of the command
mb mrBayes-run.nex > screenlog & (it is saving the display in the screenlog and it is
running it on the background)

top (Will give the top processes that are running)

## SEP 17

-I can ad —-color in the grep command to get the matcher colored
-using xargs within the commands tells it to show the content instead of just the filename

-Grep commands work different in linux and in mac. But we can have the linux tools by installing brew (see class)

In regular expressions
[aBc] means or: a or B or c
[^aBc] anything but a B or c
\w a word character 

[[:alnum]_] outside brakets mean or, the inside brakets mean a category(numeric) and the _ means alphanumeric or _

the : : means that is a predifined categoy (like alphanumeric, digit)

\d*\.\d+ means I am looking for a digit  (\d) a zero or more (*) followed by a . \. followed by a digit (\d+)

In the example of class 

How to exclude of the first line? grep -v "^>" tb1.fasta | less (pipe it to less so that if it is a big file dont shows eveeerything)
grep -v "^>" tb1.fasta | grep [^ACGTacgt] | less here the ^ means not ACGTacgt 
grep -v "^>" tb1.fasta | grep --color [^ACGTacgt]
grep -v "^>" tb1.fasta | grep -o [^ACGTacgt]
grep -v "^>" tb1.fasta | grep -on [^ACGTacgt]
grep -v "^>" tb1.fasta | grep -oni [^ACGT]
grep -v "^>" tb1.fasta | grep -oni [^acgt]

## SEP 19

For scripts use relative paths!

Grep

from the file partitionfinder_bestscheme.txt (see class today) I want to determine how many lines have GTR+I
grep -c "| GTR+G " partitionfinder_bestscheme.txt
grep "| GTR+G " partitionfinder_bestscheme.txt | less (to see which I am selecting)
grep "| GTR+G " partitionfinder_bestscheme.txt | wc (to get all the counts)


$ means at the end of the line
\$ means the actual dolar saving
'$ ' will also show me a $ 
^ at the beggining means beggining of line, in the middle means just the ^ inside a [] at the beggining means everything but
grep '^$' shows blank lines
grep -E '^\s+$' will show blank line with spaces

for next homework see example of class  (cd classroom-repos/hw1/)

if with grep i dont want the entire line but just want matches -o
grep -o 
but I want the numbers tools
grep -Eo "Elapsed time. \d+" out/timetest9_sanq.out
grep -Eo "Elapsed time. \d+\.\d" out/timetest9_sanq.out

find ~ -name ".DS_Store" -d 2 | wc (depth 2, goes down 2 levels in the home directory)
find ~ -name ".DS_Store" -d 2 | xargs rm (tells it that what I want to remove is the arguments 

rm $(find ~ -name ".DS_Store) also works

Project management & markdown format

.md means markdown text format (e.g readme.md)

## SEP 24

git diff -> tells me the difference in the files that are going to be commited and the new
git diff --staged -> tells me the difference between the new file and a previous stage (the precious commited)
git add -> tells it to add this to the next commitment
git commit -m 'initial commit, meain readme only' --> commits the new files, the -m indicates the message of the commitment
git log --> list all the different pictures, all the different commits 

If I want to have a long message for each commitment, write a shiort line as a summary and then a blank line 
and then a pararaph. There is only one message for each commitment independently of the files. To do this you dont
use the -m in the commit command, you just type git commit and git opens an editor to write your message
and your paragraph if you want to write it 

git show -> will show the actual content of the commit (only the last one)
git show 0466267 -> and specific commitment
to show all the commitments -> gl
git log -> only shows the title of the commit and who did it, but not the content

git log --pretty=onleline -> shows me the commit in a pretty way in one line
git log --pretty=onleline --abrev--commit -> abreviated the commit name

we have 3 stages in git files

commited    staging area     working files 

git commit -a -> does both git add and git commit on the things that are tracked

touch .gitignore -> creates a file that will tell git what to ignore 
 inside the file write the data that want to be ignored -> example data/seqs/*.fastq

then track the .gitignore (git add, git commit)

It is a good idea to have a new line at the end of each file 

git checkout --readme -> restores the last file I saved with the last version of it that was commited

git reset HEAD filename -> to reset the file, but still have to do the checkout

test test test