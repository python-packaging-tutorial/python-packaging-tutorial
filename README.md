# python-packaging-tutorial
Tutorial on python packaging at SciPy 2018

## Rendered notes here:

https://python-packaging-tutorial.github.io/python-packaging-tutorial/


## Installation instructions


### Windows

* Install Miniconda3: https://conda.io/docs/user-guide/install/windows.html
* Install conda-build using conda: https://conda.io/docs/user-guide/tasks/build-packages/install-conda-build.html
* install Visual Studio 2017: https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15&utm_source=vscom&utm_medium=clickbutton&utm_campaign=tailored_featurepgcppsp&rid=34346
* Install Docker for Windows: https://www.docker.com/docker-windows
* create a conda environment for playing with scikit-build: ``conda create -n skbuild -c conda-forge cmake scikit-build cython``


### MacOS

* Install Miniconda3: https://conda.io/docs/user-guide/install/macos.html
* Install conda-build using conda: https://conda.io/docs/user-guide/tasks/build-packages/install-conda-build.html
* Install Xcode: ​https://itunes.apple.com/us/app/xcode/id497799835?mt=12​ .
* Follow instructions in the conda-build documentation to install an older MacOS SDK: https://conda.io/docs/user-guide/tasks/build-packages/compiler-tools.html#macos-sdk
* Install Docker for Mac: https://www.docker.com/docker-mac
* create a conda environment for playing with scikit-build: ``conda create -n skbuild -c conda-forge cmake scikit-build cython``


### Linux

* Install Miniconda3: https://conda.io/docs/user-guide/install/linux.html
* Install conda-build using conda: https://conda.io/docs/user-guide/tasks/build-packages/install-conda-build.html
* Install Docker client for your OS:
  * Ubuntu: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04
  * Fedora/RHEL: https://developer.fedoraproject.org/tools/docker/docker-installation.html
* create a conda environment for playing with scikit-build: ``conda create -n skbuild -c conda-forge cmake scikit-build cython``


### Docker Image caching

* run ``docker pull dockcross/manylinux-x64``


## Testing installation

* Clone this repository
* cd into the ``test_recipes`` folder
* run ``conda build bitarray``.  Success is indicated by output like:

```
===== bitarray-0.8.1-py36h1de35cc_1 OK =====
import: 'bitarray'

Resource usage statistics from testing bitarray:
   Process count: 1
   CPU time: Sys=0:00:00.0, User=0:00:00.0
   Memory: 1.1M
   Disk usage: 16B
   Time elapsed: 0:00:02.0

TEST END: /Users/msarahan/miniconda3/conda-bld/osx-64/bitarray-0.8.1-py36h1de35cc_1.tar.bz2
Renaming work directory,  /Users/msarahan/miniconda3/conda-bld/bitarray_1529267981928/work  to  /Users/msarahan/miniconda3/conda-bld/bitarray_1529267981928/work_moved_bitarray-0.8.1-py36h1de35cc_1_osx-64_main_build_loop
# Automatic uploading is disabled
# If you want to upload package(s) to anaconda.org later, type:

anaconda upload /Users/msarahan/miniconda3/conda-bld/osx-64/bitarray-0.8.1-py36h1de35cc_1.tar.bz2

# To have conda build upload to anaconda.org automatically, use
# $ conda config --set anaconda_upload yes

anaconda_upload is not set.  Not uploading wheels: []
####################################################################################
Resoource usage summary:

Total time: 0:00:36.9
CPU usage: sys=0:00:00.2, user=0:00:00.2
Maximum memory usage observed: 50.6M
Total disk usage observed (not including envs): 1016B


####################################################################################
```

* cd into the ``test_recipes/hello-cython`` folder
* activate the ``skbuild`` environment: ``conda activate skbuild``.  For older conda (<4.4) installations, follow legacy instructions at https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment
* run ``python setup.py install``.  Success is indicated by output ending in lines like:

```
creating 'dist/hello_cython-1.2.3-py3.5-macosx-10.9-x86_64.egg' and adding '_skbuild/setuptools/bdist.macosx-10.9-x86_64/egg' to it
removing '_skbuild/setuptools/bdist.macosx-10.9-x86_64/egg' (and everything under it)
Processing hello_cython-1.2.3-py3.5-macosx-10.9-x86_64.egg
Copying hello_cython-1.2.3-py3.5-macosx-10.9-x86_64.egg to /Users/msarahan/miniconda3/envs/skbuild/lib/python3.5/site-packages
Adding hello-cython 1.2.3 to easy-install.pth file

Installed /Users/msarahan/miniconda3/envs/skbuild/lib/python3.5/site-packages/hello_cython-1.2.3-py3.5-macosx-10.9-x86_64.egg
Processing dependencies for hello-cython==1.2.3
Finished processing dependencies for hello-cython==1.2.3
```
* You're all set!

## Troubleshooting

* Please file issues on this github issue tracker: https://github.com/python-packaging-tutorial/python-packaging-tutorial/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc


## Package hosting service accounts
Pprior to attending the tutorial, participants should set up an account on
* PyPI (​https://pypi.org/account/register/) and TestPyPI (https://test.pypi.org/account/register/)
* anaconda.org (​https://anaconda.org/​)
