# Creating a Repository

Once Git is configured,
we can start using it.

We will continue with the story of Wolfman and Dracula who are developing a
delicious guacamole recipe.

First, let's create a directory for our work and then move into that directory:

~~~
$ mkdir guacamole
$ cd guacamole
~~~


Then we tell Git to make `guacamole` a repository—a place where
Git can store versions of our files:

~~~
$ git init
~~~


If we use `ls` to show the directory's contents,
it appears that nothing has changed:

~~~
$ ls
~~~


But if we add the `-a` flag to show everything,
we can see that Git has created a hidden directory within `guacamole` called `.git`:

~~~
$ ls -a
~~~


~~~
.	..	.git
~~~


Git uses this special sub-directory to store all the information about the project,
including all files and sub-directories located within the project's directory.
If we ever delete the `.git` sub-directory,
we will lose the project's history.

We can check that everything is set up correctly
by asking Git to tell us the status of our project:

~~~
$ git status
~~~


If you are using a different version of git than I am, then then the exact
wording of the output might be slightly different.

~~~
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
~~~

Do not create git repositories inside other ones!