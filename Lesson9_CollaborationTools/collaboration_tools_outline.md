# Memos
* http://reionization.org/science/memos/
* Memos are a way to formalize and communicate interesting findings to the whole collaboration.
* Sometimes memos are developed into full publications, but even if they aren’t, they are very useful to refer back to.
* In HERA, there’s a low threshold for memos -- they don’t have to be large or publication level

# Wiki
* Much of the project is documented here.  It’s community edited!
* http://hera.pbworks.com/

# Slack
* eoranalysis.slack.com
* HERA is a highly distributed collaboration. We talk to each other every day, often many times a day.
* Slack lets you paste in plots and code. Use it.
* If you are having trouble with some bit of code or subsystem odds are the person that invented it is just a slack away. Don’t be afraid!
* There are a *lot* of channels for specific topics. Sometimes it’s not totally clear which channel to use, but make your best guess to have the best chance of getting to the right people.
* Use channels instead of private messages to get more eyes on your problem (but private messages are often useful too)
* Remember! DMs do not exist to the world. Anything useful said there might as well not exist.

# Git and GitHub
## Developing Code in Personal Repos
* Making a new repo
  * Add your mentor as a collaborator (to share your awesome work!)
  * Make it public! Science belongs to everyone
  * Add a license! Open source ones are best (BSD 2/3-clause, MIT, GPL)
  * Add a README (documentation is key!)
  * Add a  .gitignore
* Ideal workflow
  * Can push directly to master branch (though other branches are possible)
  * Commit early and often! 1x per day at least
  * Write copious documentation! Communicate with others and your future self
  * Make a new notebook for each new problem you’re trying to solve. Notebooks are not “finished” until you can restart the kernel and run without errors
  * Once code in notebooks is useful enough to be reused, it should be brought out into modules
* Potential Pitfalls
  * Don’t commit big files, or lots of small files. Repos are (generally) for code, not for data!
    * Plots can go in notebooks, which are very useful for exploring data
  * Don’t collaborate with people on jupyter notebooks. They are useful for personal code exploration, but do not play nicely with git.
    * Python modules are much nicer to use with git, so it encourages you to modularize useful notebook code when you want to share!
  * If you want to make large changes, making a branch can be useful (rather than pushing directly to master)
## Contributing to Collaboration Software
* Collaboration software is for everyone in the collaboration -- including you!
* If you come up with useful functionality, we want to incorporate it into the collaboration software.
* We have mechanisms to allow you to easily modify collaboration software to make it do what you need without messing other people up (forks & branches)
* Make a new branch before you start modifying the code (ask for help from your mentor or on Slack). This will make it much easier to flow your work back into the master code.
* See the [HERA Software Dev Handbook (google doc)](https://docs.google.com/document/d/1hWTem1LwMgASZ4oWzSnVIvj-2-z2McwU6czD3dI5284/edit?usp=sharing) for more.
* Pull requests are how we work together to make code changes. [Here is an example](https://github.com/HERA-Team/pyuvdata/pull/355).
* Potential Pitfalls
  * Don’t make edits on the master branch of any HERA collaboration repo.
    * You won’t be able to push them up to github and it will take work to move them over to another place.
  * Branches should be for single ideas. If you’re making several different, unrelated changes, do them in separate branches.
