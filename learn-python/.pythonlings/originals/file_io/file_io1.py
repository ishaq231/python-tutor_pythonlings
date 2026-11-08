# Exercise: File IO 1
# I AM NOT DONE
#
# Programs can save information to FILES so it's still there after the program
# stops. Opening a file takes a "mode":
#     "w"   write (creates the file, or wipes it if it already exists)
#     "r"   read (the default)
#     "a"   append (adds to the end)
#
#     f = open(path, "w")      <- open it
#     f.write("some text")     <- put text in
#     f.close()                <- close it when you're done (important!)
#
# Here `data_path` is the location of a brand new temporary file.
# Replace the ??? so that the file contains exactly "hello, file!".

import tempfile

data_path = tempfile.mktemp()

# Write "hello, file!" to data_path.
f = open(data_path, "w")
f.write(???)
f.close()
