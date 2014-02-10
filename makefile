

# Note 'all' must be the first target.
# Note the '@' at the beginning of @echo means don't display command
all:   tests
	@echo "All tests pass"

test0:
	@echo "Test 0 passes!"

test_versions:
	python3 bin/check_version.py

# This was here just to have a failed make.
# test1:)
#	echo "Should fail" && /usr/bin/false

tests:  test0 test_versions
