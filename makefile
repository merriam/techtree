

# Note 'all' must be the first target.
# Note the '@' at the beginning of @echo means don't display command
all:   tests
	@echo "All tests pass"

test_pass:
	@echo "Empty test passes!"

test_versions:
	python3 bin/check_version.py

# This is here just to have a failed make.  It is not in the test list.
test_fail:
	echo "Should fail" && /usr/bin/false

test_container_pass:
	docker run ubuntu /bin/sh -c 'exit 0'

test_container_fail:
	@echo "This should fail!"
	docker run ubuntu /bin/sh -c 'exit 1'

test_node_pass:
	docker run node node -c 'console.log("Node runs!")'

# These are here because I hate how sysadmin takes over the lore af a project
get_docker:
	# boot2docker is a lightweight docker container
	rm bin/boot2docker || true
	curl https://raw.github.com/steeve/boot2docker/master/boot2docker > bin/boot2docker
	chmod +x bin/boot2docker
	# docker is client talking to docker's container
	curl -o docker https://get.docker.io/builds/Darwin/x86_64/docker-latest
	chmod +x docker
	## Set the environment variable for the docker daemon
	export DOCKER_HOST=tcp://
	@echo "Remember to set 'export DOCKER_HOST=tcp://' somewhere"
	sudo mv docker /usr/local/bin/

boot2docker:
	#
	# Init the daemon.
	bin/boot2docker down || true
	bin/boot2docker delete || true
	bin/boot2docker init
	bin/boot2docker up
	@echo "This is now installed:"
	docker version

up:
	bin/boot2docker up

kill_images:  up
	docker rmi node
	docker rmi ubuntu

docker_images:	up
	docker run ubuntu date
	docker build --tag="node" node_docker
	docker images

tests:  test_pass test_versions test_container_pass test_node_pass
