#!/bin/bash

# Creating an array of all the folders specifically, so that the template
# files are copied into the folders only.
array=($(ls -d */))

# For each of the folders, copy in the template file, renamed
# to the problem/name of the folder.
for i in "${array[@]}"
do
   :
   name=${i::-1}
   
   if    ls -A1q $name | grep -q .
   then  ! echo $name is not empty, skipping
   else  
     echo Copying over templates into $name
     # Create Python file
     cp ./template.py ./$name/$name.py
     # Create Java files
     cp ./template_main.java ./$name/$name.java
     cp ./template_solution.java ./$name/Solution.java
     # Create C++ file
     #cp ./template.cpp ./$name/$name.cpp
     # Create C file
     #cp ./template.c ./$name/$name.c
     # Create Go file
     #cp ./template.go ./$name/$name.go
     # Create Rust file
     #cp ./template.rs ./$name/$name.rs
     # Create Typescript
     #cp ./template.ts ./$name/$name.ts
   fi
done
