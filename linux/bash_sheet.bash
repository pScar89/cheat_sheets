# Bash Scripting Cheat Sheet

# Basic Script Structure
#!/bin/bash        # Shebang line to specify bash interpreter
echo "Hello World" # Basic command to print text to the console

# Variables
VAR="value"        # Defining a variable
echo $VAR          # Accessing a variable

# Special Variables
$0                 # The name of the script
$1, $2, ...        # Script arguments
$#                 # Number of arguments
$?                 # Exit status of the last command executed
$$                 # Process ID of the script
$USER              # The username of the user running the script
$HOSTNAME          # The hostname of the machine
$SECONDS           # Number of seconds the script has been running
$RANDOM            # Random number

# Conditionals
if [ condition ]; then
    # commands
elif [ condition ]; then
    # commands
else
    # commands
fi

# Comparison Operators
-eq                # Equal
-ne                # Not equal
-gt                # Greater than
-lt                # Less than
-ge                # Greater than or equal to
-le                # Less than or equal to

# Loops
# For loop
for VAR in list; do
    # commands
done

# While loop
while [ condition ]; do
    # commands
done

# Until loop
until [ condition ]; do
    # commands
done

# Functions
function_name () {
    # commands
}

# File Test Operators
-e file            # True if file exists
-d file            # True if file is a directory
-f file            # True if file is a regular file
-r file            # True if file is readable
-w file            # True if file is writable
-x file            # True if file is executable

# Redirection
command > file     # Redirect standard output to a file
command < file     # Redirect standard input from a file
command >> file    # Append standard output to a file
command 2> file    # Redirect standard error to a file
command1 | command2 # Pipe the output of command1 to the input of command2

# Special Characters
;                   # Command separator
&&                  # Logical AND
||                  # Logical OR
*                   # Wildcard for zero or more characters
?                   # Wildcard for exactly one character

# Arithmetic
let sum=$num1+$num2  # Arithmetic operation
$((expression))      # Arithmetic expansion

# Quoting
"string"             # Double quotes (allows variable and command expansion)
'string'             # Single quotes (prevents expansion)

# Here Documents
cat <<EOF
This is a
multiline text string
EOF

# Command Substitution
output=$(command)

# Exit Status
exit 0              # Exit script successfully
exit 1              # Exit script with error

# Note: This cheat sheet is a basic overview and does not cover all features of bash scripting.
