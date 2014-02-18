2/17/2014
-

It's been a few days.  Just kids, a nice date, a day at Angel Island.  I did spend an hour or two mucking around with sample data from frustration of being a week into the project without getting infrastructure to work.

Time to come back to the project.   Suddenly it seems I left it broken.  The 'docker' mechanisms arebroken with boot2docker not mounting files and CoreOS failing to work.   'make' is broken.   tests are broken.  The 'git' is out of date.  The only solution is to work at getting a process back.  Make a test run, with git up to date.  I started with the tests and am adding there.

2/12/2014
-

Played with Jasmine files as a test framework.   Seems to work, though Safari lies about 'disable caches`.   Remember to constantly empty the cache and then reload (option-cmd E; cmd-R).

Tried mounting the Jasmine files into the node image.  Filed two pull requests in Docker:  the mount commands only use the boot2docker vm.



2/11/2014
-

Finally got past bugs (on a better network) and managed to get node.js running in a container.  Good milestone.


Trying to add a 'delete images' target, but running into more bugs with docker.  First, some odd zombie container, then another image_delete error on the last container.

The node.js package is node.   The node package is an amateur packet radio package that creates a /usr/sbin/node.


Still playing with just running apt-get update and apt-get install.   Amazingly badly written pieces everywhere.   The default output is a spew, but the cryptic messages like "invoke-rc.d: policy-rc.d denied execution of stop" is in stdout instead of stderr.   Man page documentation of -q is unreadable, and apt-get install -q still has "Reading database..." display hacks in it.  Avoiding go down a rabbit hole filing bugs.


2/10/2014
-

Added spotify's dockerfile mode (https://github.com/spotify/dockerfile-mode) for better syntax highlighting goodness.   Really need to put .emacs under source control.

Playing around with docker.  Feels like slogging through random errors.   A missing environment errors manifests itself as 'docker version' dying.  Something is corrupted down in the virtual boxes.  No documentation on the docker cache.

Stopped playing with the check_update.py feature:  it can be a full new program.

Added first tests with 'ubuntu' base repository.   Added comments to the 'ubuntu' image.  Added to bug report on "Couldn't snd EOF".  Didn't file bugs on docs being wrong about mounts.   Didn't file bugs on missing docs on exit status.   Only so many bugs reported per day.

Bugging out on an "Unexpected EOF" which might be a vagrant error and might be a docker error.   Added to current bug report.   Found out that:

* Standard Virtual Box images live in "~/VirtualBox VMs", but the boot2docker virtualbox image lives in ~/.boot2docker.
* bin/boot2docker ssh has the password as tcuser
* The boot2docker vmdk seems to be small, only 1.9GB.   The settings suggest it may grow to as much as 40 gb.
* boot2docker gives "locked" errors meaning that it is still running when trying to delete it.


2/9/2014
-

Switched to iTerm2, now my pgUp/pgDown seems to work.

Docker main getting started is borked on os/x installation instructions.   The "edit this page" link on http://docs.docker.io/en/latest/installation/vagrant/ goes to https://github.com/dotcloud/docker/blob/master/docs/sources/installation/vagrant.rst which is wrong.  That page fails to mention all the specific running OS/X on docker installation instructions at http://docs.docker.io/en/latest/installation/mac/.  Submitted a bug.

Hmm.. Emacs binds C-/ to undo.  Good to know.

Noticed virtualbox was out of date and hacked together a tool to check if things are up to date.   That tool, in check_version.py, might mature in time.   Meanwhile, I have a makefile now.

2/8/2014
-

Not much time today to play.   Set up a github repository, clone it to local, start adding plans and files.

These files should be markdown, it's just cleaner that way.  Copying off a few random views of how it should work.

Learned a smidgeon more about markdown outlines.  Emacs shift-tab is odd.  Also a line like "\#.#" in .gitignore ignores some emacs files
