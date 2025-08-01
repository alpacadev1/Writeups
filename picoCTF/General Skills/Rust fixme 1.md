# URL
https://play.picoctf.org/practice/challenge/461?originalEvent=74&page=1

# Challenge 
Description
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!

# Work
* tar -xzf fixme1.tar.gz (-x means extract, -z means decompress gzip, -f specifies the filename.)
* cd into src
* nano main.rs -> fix errors (e.g, semicolon, return, and println use double quotes)
* Use the cargo build command in the directory where Cargo.toml is located (it installs the dependencies for the code to compile)
* cargo run to get the flag!
