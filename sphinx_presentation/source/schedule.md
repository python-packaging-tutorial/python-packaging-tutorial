# Schedule

0:00: Overview of packaging
: - SDists  vs. wheels
  - Pure Python vs. compiled packages
  - Wheel vs conda packages
  - PyPI / anaconda.org
  - Links packaging documentation such as PyPA, Packaging Native

0:20: Exercise
: - Identify platforms supported for the xxx packages on PyPI and anaconda.org

0:25: Virtual environments
: - Setting up a virtual environment
  - Setting up a conda environment
  - Using a task runner (nox)

0:45: Exercise writing a noxfile
: - Take existing working package and add a simple noxfile

0:50: Break & catch up

1:00: Pyproject.toml
: - Essential specifications
  - Optional specifications
  - Specifying requirements
  - Introduce the concept of "build-backend"

1:10: Exercise
: - Fill in the missing pieces in a project.toml for a sample package
  - Build a source distribution for the package

1:20: Building and uploading to PyPI: tools and package types
: - Core tools
    - Pipx
    - build
    - twine: the secure way to upload to PyPI
  - For consolidated experience & dependency management
    - Pdm  (https://pdm.fming.dev/latest/)
    - May be Hatch (https://hatch.pypa.io) (more like a replacement for tox and nox)
  - Building a source distribution
  - Building a wheel
  - Discuss use of delocate/Auditwheel/…
  - Difference between linux & manylinux wheels (internalize dependencies, glibc compatibility, …)

1:45: Worked example/exercise: building a package and uploading to pypi
: - Continuing from the the previous exercise, build a wheel for the package
  - Register the package on the pypi testing server
  - Upload the built distributions using twine
  - Delete one of the uploaded files on pypi and try re-uploading (will fail)
  - Introduce the idea of .post releases (it will happen to everyone who uploads)

1:55: Coffee break

2:15: Binaries and dependencies: how scikit-build can make life easier
: - Scikit-build overview & motivation

2:40: Exercise: add CMake project that generates python extension.
: - Tie it into previous python project.

3:00: Break & catch up

3:10: Automated building with cloud-based CI services
: - GitHub action
  - Pre-commit.yml
  - Ruff
  - Static analysis
  - https://cibuildwheel.readthedocs.io/en/stable/

3:30: Exercise: (10 min)
: - Update previous example adding cibuildwheel support
  - Linting using pre-commit + ruff
  - Automated PyPI release


3:40: Handling dependencies
: - "In-project" compilation (pybind11)
  - External: see https://github.com/pypa/cibuildwheel/issues/1251#issuecomment-1236364876 for example

3:50: Exercise
: - Add a dependency to the project
