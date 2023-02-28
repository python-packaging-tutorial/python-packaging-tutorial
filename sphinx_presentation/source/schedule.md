# Schedule

0:00: Overview of packaging
: - SDists  vs. wheels
  - Pure Python vs. compiled packages
  - Wheel vs conda packages
  - PyPI / anaconda.org
  - Links packaging documentation such as PyPA, Packaging Native

0:15: Exercise
: - Identify platforms supported for the xxx packages on PyPI and anaconda.org

0:20: Virtual environments
: - Setting up a virtual environment
  - Setting up a conda environment
  - Using a task runner (nox)

0:30: Exercise writing a noxfile
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

1:35: Worked example/exercise: building a package and uploading to pypi
: - Continuing from the the previous exercise, build a wheel for the package
  - Register the package on the pypi testing server
  - Upload the built distributions using twine
  - Delete one of the uploaded files on pypi and try re-uploading (will fail)
  - Introduce the idea of .post releases (it will happen to everyone who uploads)

1:45: Coffee break

2:05: Binaries and dependencies: how scikit-build can make life easier
: - Scikit-build overview & motivation
  - Adding a minimal CMakeLists.txt
  - Building the extension
  - Adding options and controlling the build

2:30: Exercise: add CMake project that generates python extension.
: - Tie it into previous python project.
  - Setup build caching

2:50: Break & catch up

3:00: Automated building with cloud-based CI services
: - GitHub action
  - Pre-commit.yml
      - Ruff
  - https://cibuildwheel.readthedocs.io/en/stable/

3:15: Exercise:
: - Update previous example adding cibuildwheel support
  - Linting using pre-commit + Ruff
  - Automated PyPI release


3:30: Handling dependencies
: - "In-project" compilation
  - External

3:45: Exercise
: - Add a dependency to the project
    - pybind11 (in-project)
    - lz4 (external)
