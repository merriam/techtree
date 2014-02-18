# This is a DockerFile for use with docker container managers.

# This may use data cached before 2/10/14.
# As cache is used until the first changed line in a DockerFile, changing the date
# will force a cache reload.

FROM ubuntu:saucy
# annoyingly, using saucy as 'ubuntu', aka 12.04, will not correctly
# apt-update because dpkg tries to do a mount.  Seriously?
MAINTAINER Charles Merriam <charles.merriam@gmail.com>

# update sources list to 'universe'
run sed 's/main$/main universe/' -i /etc/apt/sources.list

# update list of sources in repository cache
run apt-get update

# upgrade all packages changed since the beginning of this image.
run apt-get upgrade -y

# Install node.ls (not node), and npm.
# The npm package manager drags in many packages.
run apt-get install -y node.js npm

# install some handy node packages
run npm install express request

# expose port 8080, a private only mapping.
# see http://crosbymichael.com/dockerfile-best-practices.html on why private only.
expose 8080
