#!/bin/bash

# simple script to build and push to gh-pages
# designed to be run from master

# this version used a separate copy of the repo in a parallel dir
# to keep the gh-pages branch nicely separate from the main branch.
# this makes it easier to have the index.html in the root dir
#  -- to be nicely served by gh-pages


GHPAGESDIR=../../python-packaging-tutorial.gh-pages

# make sure gh-pages dir is there -- exit if not
if [ ! -d $GHPAGESDIR ]; then
    echo "To build the gitHub pages, you must first create a parallel repo: $GHPAGESDIR"
    exit
fi

if [ ! -d $GHPAGESDIR/.git ]; then
    echo "To build the gitHub pages, you must first create a parallel repo: $GHPAGESDIR"
    echo "It must be a git repo -- do a new git clone"
    exit
fi

# make sure that the main branch is pushed, so that pages are in sync with master
git push

# make sure the gh pages repo is there and in the right branch
pushd $GHPAGESDIR
git checkout gh-pages
popd

# make the docs
make html
# copy to other repo (on the gh-pages branch)
cp -fR build/html/* $GHPAGESDIR

pushd $GHPAGESDIR
git add .  # in case there are new files added
git commit -a -m "updating rendered materials"
git branch -u origin/gh-pages  # make sure we're tracking origin
git pull -s ours --no-edit  # gotta pull before push.. yet maintain local updates
git push
popd

echo "Now verify the render on github.io at the following link:"
echo "https://python-packaging-tutorial.github.io/python-packaging-tutorial"

