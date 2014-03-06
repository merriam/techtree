#!/usr/bin/env python3
"""
 A little program to check if there are later versions of packages I rely upon.
 This may grow into a full fledged service, but not today.
"""

import subprocess
import re
import sys

class Program:
    """A known program that can be checked to see the installed version
    number matches the published version.

    A note on security: checking requires running shell programs.  If
    a recipe runs something bad, like 'rm foo', then that will run.

    """

    def __init__(self, name, installed_command, installed_regex,
                 published_command, published_regex):
        self.name = name
        self.installed_command = installed_command
        # command can have shell charcters, e.g., "cat * | grep -i version"
        # must return 0 (Unix all ok code)
        self.installed_regex = installed_regex
        # run this regex on the output, match version as capture group 1
        self.published_command = published_command
        self.published_regex = published_regex

    def _e_get_version_number(self, for_error_message, command, regex):
        # pylint: disable=no-self-use
        """ returns (err, version_number).  Just internal repeated code. """
        # TODO:  This just doesn't cleanly grab stderr.
        try:
            out = subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError:
            return "Could not cleanly execute command to check {} version.".format(
                for_error_message), None
        if type(regex) == str:
            out = str(out, "utf-8")  # if regex was not bytes, treat output as unicode
        try:
            version = re.search(regex, out).group(1)
        except AttributeError:
            return "Could not match version number in {} command output.", None
        except IndexError:
            return "{} regex matched but did not have a group (parenthesis)", None
        return None, version

    def err_check(self):
        """return None if this program is up to date with known programs,
        else returns a string with the error.
        """
        err, installed_version = self._e_get_version_number(
            "installed", self.installed_command, self.installed_regex)
        if err:
            return err
        err, published_version = self._e_get_version_number(
            "published", self.published_command, self.published_regex)
        if err:
            return err
        if published_version != installed_version:
            return "Versions do not match.  Installed {}, but published {}".format(
                installed_version, published_version)
        return None


class KnownPrograms:
    """.known_programs{name} is a Program that could be checked. Only
    need to create a single instance."""
    def __init__(self):
        self.known_programs = {}

    def add(self, name, installed_command, installed_regex,
            published_command, published_regex):
        """ Add this to list of known programs """
        program = Program(name, installed_command, installed_regex,
                          published_command, published_regex)
        self.known_programs[name] = program

    @classmethod
    def usual_suspects(cls):
        """ return a set of the usual known programs """
        known = cls()
        known.add('VirtualBox',
            'VirtualBox --help',
            r'Oracle VM VirtualBox Manager (\d.\d.\d)',
            'curl --silent https://www.virtualbox.org/wiki/Downloads',
            r'OS X.*/virtualbox/(\d\.\d\.\d)/')
        known.add('Docker',
            'docker --version',
            r'Docker version (\d.\d.\d)',
            'curl --silent https://raw.github.com/dotcloud/docker/release/VERSION',
            r'(\d.\d.\d)')
        return known

def _add_pass(known):
    known.add("_pass", "echo True", "(True)", "echo True", "(True)")

def test_simple_pass():
    known = KnownPrograms()
    _add_pass(known)
    assert "_pass" in known.known_programs
    assert "_mystery" not in known.known_programs
    assert known.known_programs["_pass"].err_check() is None

def _add_failures(known):
    # hate to repeat code
    known.add("_version_mismatch", "echo True", "(True)", "echo False", "(False)")
    known.add("_installed_will_not_run", "//bad_command", "True", "echo False",
              "(False)")
    known.add("_no_group_in_installed_regex", "echo True", "True", "echo True",
              "(True)")
    known.add("_no_group_in_publshed_regex", "echo True", "(True)", "echo True",
              "True")
    known.add("_installed_will_not_match", "echo True", "(bad_regex)", "echo True",
              "(True)")
    known.add("_published_will_not_run", "echo True", "(True)", "//bad_command",
              "(True)")
    known.add("_published_will_not_match", "echo True", "(True)", "echo True",
              "(bad_regex)")


def test_failures():
    known = KnownPrograms()
    _add_failures(known)
    for program in known.known_programs.values():
        assert program.err_check() is not None

class ProgramSuite:
    """A set of installed programs to check.

    Each program is identified by a name, which should correspond to a
    list of known programs that can be checked.

    There are really only a few possible errors: don't know how to
    check, failed to run installed programs, failed to run published
    programs, version numbers don't match.  Faling to run might be in
    the exec or matching the version number.  These can be strings for now.

    """
    def __init__(self, program_list=None):
        if program_list == None:
            self.programs = []
        else:
            self.programs = program_list.split()

    def check(self, known):
        """ return True if everything up to date, else false.
        Print status to terminal.
        """

        print("Checking versions...")
        all_OK = True
        for name in self.programs:
            if name not in known.known_programs:
                print("{}: FAIL Could not match program in list of "
                      "known programs".format(name))
                all_OK = False
            else:
                err = known.known_programs[name].err_check()
                if err:
                    print("{}: FAIL {}".format(name, err))
                    all_OK = False
                else:
                    print("{}: PASS".format(name))
        if all_OK:
            print("Versions are all up to date.")
        else:
            print("Failure while checking versions.")
        return all_OK

def test_suite_passes():
    known = KnownPrograms()
    _add_pass(known)
    _add_failures(known)
    assert ProgramSuite("_pass _pass _pass").check(known)
    assert ProgramSuite("").check(known)
    assert not ProgramSuite("_pass _version_mismatch _pass").check(known)
    assert not ProgramSuite("_pass _unknown _pass").check(known)


def test_usual_suspects():
    known = KnownPrograms.usual_suspects()
    assert "Docker" in known.known_programs.keys()

if __name__ == "__main__":
    usual = KnownPrograms.usual_suspects()
    is_ok = ProgramSuite("Docker VirtualBox").check(usual)
    if is_ok:   # Unix has 0 as success, 1 for fail.
        sys.exit(0)
    else:
        sys.exit(1)
