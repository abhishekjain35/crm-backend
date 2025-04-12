pwd - 
  Prints the working directory.
  Helps knowing where you are currently, the path.

whoami - 
  Prints the current user.
  Helps knowing the current user and with which user the commands will be run

echo $SHELL - 
  Prints the current shell i am working with.
  Helps knowing which shell currently being used.
  Question - what do different shells do? like zsh, bash etc..?

echo $PATH - 
  Displays value of $PATH env variable, a colon separated list of directories
  From start to end, it tries to find the command you ran in the directories
  Question - how to add something to path?

ls -la - 
  Lists all directories and folder available in current directory, including files and folders starting with . and more info like size, owner, modified date etc.
  Helps knowing which all files and folders are available 
  Question - what is this "drwxr-x---+"? what does everything mean here?

cd ..
  Goes to parent directory

mkdir dev && cd dev - 
  Creates a directory named dev and goes into it.

ps aux | grep python - 
  displays a lot of info about currently running process.
  Helps knowing things like cpu%, mem% etc..
  Question - what does STAT and VSZ mean here?

chmod +x somefile - 
  Make a file executable like a bash script.

top - 
  Realtime status of processes, since when they're running, resource utilization etc..
  Question - what are some of the important things displayed by top that are useful?
