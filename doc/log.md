2/10/2014
-

Playing around with docker.  Feels like slogging through random errors.   A missing environment errors manifests itself as 'docker version' dying.  Something is corrupted down in the virtual boxes.  No documentation on the docker cache.

Stopped playing with the check_update.py feature:  it can be a full new program.

Added first tests with 'ubuntu' base repository.   Added comments to the 'ubuntu' image.  Added to bug report on "Couldn't snd EOF".  Didn't file bugs on docs being wrong about mounts.   Didn't file bugs on missing docs on exit status.   Only so many bugs reported per day.


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
