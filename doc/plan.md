Technology Tree Project Plan
===


Goal
----
   Learn a bit of TDD, a bit of node.js, a few packages, keep a log.

Steps
----
*   Set-up
    *   Repository up and running
    *   Outline of Plans and Logs
    *   Docker running
    *   Docker running w/node.js
    * Docker running w/node.js hello world
    * Docker running test w/node.js hello world
* Development
* Usage
  * Make some fun technology trees
      * Personal development
      * Corporate capabilities
      * Real current technology
      * TED Topics
  * Pull out some useful tools
  *  Blog and present it

Docker Notes
----
*   VirtualBox is installed at system level.
*   Install docker at local level.  Should have directory like docker.0.8
      and link to it.
*   Docker needs
      cd ~/p/dev/docker && vagrant up && vagrant ssh
     Virtual boxes live in "~/VirtualBox VMs", yes with a space


Create Recipe
----
1.   Start with Ubuntu
2.   Do the
    sudo apt-get update
      to update my repository list
3.  Save the changed version as Ubuntu-update
4.  Do the
   sudo apt-get -y upgrade
5.  Save the changed version as ubuntu-update
6.  Add in the sdl lines
      Save as ubuntu-sdl

Issues
---

*  Need to make a share directory using the docker's vagrant file so that editing in OS/X shows up in the VM filespace easily.
*  Need to maintain simple 'go' command to make tests happen and so on.

Open Emacs Issues
--
- Need better way to wrap text, the text mode.
- Still missing pgup/pgdown as terminal remaps
- Easy way to increase face when working without glasses, map to ctrl+/ctrl-
- Need .emacs under source control


Plan for Development
---------------------


About Technology Tree TDD
=============

Write a program that takes the technology tree, and a current set of technologies.

*  It should be able to tell me what are the next technologies available.
* It should be able to tell me what set of technologies need to researched
  for a goal and an overview of the 'cost'
* It should be able to reward a technology and add it to my current set

requirements
-----

   It should have a menu with these options:
      1.  Show next available technologies
      2.  Show plan for target technology
      3.  Award a technology.


alt steps
---------

   Need to read about new Docker
   -   download new docker
   -   figure out plan of docker heirarchy:
       *     core ubuntu
       *    patched ubuntu
       *     w/build tools like gcc and emacs
       *     w/project tools like node.js
       *     w/development ready
   - figure out how to run full test from command line
         - run tests
         - run web server and connect to it
         - suck off logs

   Need a vagrant file to spin up a docker
   Need to understand docker files
   Need to create a structure:
      src, lib, bin
   Need to figure out Travis CI
      need to set up a git repo
   Need to select some testing tools
   Serving via Node.js

   Open a terminal in emacs....
))
