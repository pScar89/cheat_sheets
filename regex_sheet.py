# Regular Expressions (Regex) Cheat Sheet

# Basic Syntax
.           # Any single character except newline
^           # Start of string
$           # End of string
[abc]       # Any character between the brackets (a, b, or c)
[^abc]      # Any character not in the brackets
[a-z]       # Any lowercase letter
[A-Z]       # Any uppercase letter
[0-9]       # Any digit
[a-zA-Z0-9] # Any alphanumeric character
|           # Either the pattern to its left or its right (OR operator)
(abc)       # Group - matches the expression 'abc' and stores it as a group

# Quantifiers
*           # 0 or more of the preceding element
+           # 1 or more of the preceding element
?           # 0 or 1 of the preceding element (makes it optional)
{n}         # Exactly n copies of the previous character
{n,}        # n or more copies of the previous character
{n,m}       # Between n and m copies of the previous character

# Special Characters
\n          # Newline
\t          # Tab
\r          # Carriage return
\d          # Any digit [0-9]
\D          # Any non-digit
\w          # Any alphanumeric character [a-zA-Z0-9_]
\W          # Any non-alphanumeric character
\s          # Any whitespace character (space, tab, newline)
\S          # Any non-whitespace character
\b          # Word boundary
\B          # Not a word boundary

# Escaping Special Characters
\           # Escape the next character (e.g., \. to match a literal period)

# Flags (Modifiers)
i           # Case-insensitive mode
g           # Global search
m           # Multiline mode

# Common Patterns
^\d+$       # String contains only digits
^[a-zA-Z]+$ # String contains only letters
^[\w]+$     # String contains only alphanumeric characters
^[\w\s]+$   # String contains only alphanumeric characters and spaces
^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$ # Basic email pattern

# Note: This cheat sheet provides a general overview and is not exhaustive. Regex syntax may vary slightly between different programming languages and tools.
