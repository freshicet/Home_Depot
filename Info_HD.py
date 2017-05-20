#!/usr/bin/python
# -*- coding: utf-8 -*-
# A script to read the Info the File_INFO file

file = open('File_INFO.txt', 'r')
First_name = file.readline()
Last_name = file.readline()
Email = file.readline()
zip_code = file.readline()
