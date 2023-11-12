#!/bin/bash
array=($(ls -d */))
for i in "${array[@]}"
do
   :
   name=${i::-1}
   cp ./template.py ./$name/$name.py
   cp ./template_main.java ./$name/$name.java
   cp ./template_solution.java ./$name/Solution.java
   cp ./template.cpp ./$name/$name.cpp
   cp ./template.c ./$name/$name.c
done
