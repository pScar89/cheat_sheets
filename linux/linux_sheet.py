# Linux Command Cheat Sheet

# System Information
uname -a                # Display Linux system information
hostname                # Show or set the system's host name
top                     # Display Linux processes
ps aux                  # Display active processes
whoami                  # Display the current user
id                      # Display user identity
df -h                   # Report file system disk space usage
du -sh                  # Estimate file space usage
free -m                 # Display free and used memory

# File and Directory Management
ls                      # List directory contents
ls -l                   # List with long format
ls -a                   # List including hidden files
pwd                     # Print working directory
cd directory_name       # Change directory
mkdir directory_name    # Create a new directory
rmdir directory_name    # Delete a directory
touch file_name         # Create a new empty file
cp source_file dest_file # Copy files
mv old_name new_name    # Move/rename files or directories
rm file_name            # Remove files
rm -r directory_name    # Remove directories recursively

# File Viewing and Manipulation
cat file_name           # Display file content
more file_name          # View file content page by page
less file_name          # Improved version of more
head file_name          # Display the first lines of a file
tail file_name          # Display the last lines of a file
grep 'pattern' files    # Search for a pattern in files
wc file_name            # Print newline, word, and byte counts for files
sed 's/old/new/' files  # Stream editor for filtering and transforming text
awk 'pattern {action}' files # Pattern scanning and processing language

# Network Operations
ping host               # Send ICMP ECHO_REQUEST to network hosts
ifconfig                # Configure a network interface
netstat -tulpn          # Display network connections
ssh user@host           # Connect to host as user
scp source_file user@host:directory # Secure copy file to remote host

# System Administration
sudo command            # Execute a command as superuser
apt-get install package # Install packages (Debian-based systems)
yum install package     # Install packages (Red Hat-based systems)
systemctl status service # Check status of a service
journalctl -xe          # Query and display messages from the journal
useradd user_name       # Add a new user
userdel user_name       # Delete a user
passwd user_name        # Change user password

# Archiving and Compression
tar cvf archive_name.tar files # Create a tar archive
tar xvf archive_name.tar       # Extract a tar archive
gzip file_name                # Compress a file
gunzip file_name.gz           # Decompress a file

# File Permissions
chmod permissions file_name  # Change file permissions
chown user:group file_name   # Change file owner and group

# Disk Usage
df                           # Display disk usage
fdisk -l                     # Display disk partitions
mount /dev/partition /mount/point # Mount a file system

# Note: This cheat sheet provides a basic overview and does not cover all commands or options available in Linux.
