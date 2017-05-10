# Champ Lesson 8
In this section of the bootcamp, we will be working with raw data from HERA. As part of it, we need to learn how to retrieve raw data. The interface for doing this is called the Librarian, which is currently hosted at Penn.

## Logging in to the Librarian
Information for logging into the librarian is not public. Please follow the instructions at the following link to connect: http://herawiki.berkeley.edu/doku.php/librarian

## Retrieving a specific file
We'll be working with some specific files of HERA data, which we can find with the search bar. We want to download the specific observations corresponding to JD `2457700`. You will notice that all filenames contain a decimal JD in their names. `xx` is the polarization state of the data. `HH` reflects that this is from the "HERA hex" part of the array. The file extension `.uvc` shows that this is a raw `.uv` file that has had some preliminary `c`orrections applied to it.

To download the files from the librarian, go to "search" and enter in the text field:
```
{"name-like": "zen.2457700.4%.xx.HH.uvc"}
```
This will return all files that have a JD starting with `2457700.4`, as well as the desired polarization and array components. The `%` operator is a wildcard character in SQL (the database software managing the librarian's storage) that behaves the same way as the `*` operator for the shell. Click on each file to download it.

