#! /bin/bash
# A script to set the current Git branch to main and push it to origin
cd ..
git branch -M main
git push -u origin main
