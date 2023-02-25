from __future__ import annotations

import nox


@nox.session(reuse_venv=True)
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass "serve" to serve.
    """

    session.install("-r", "sphinx_presentation/requirements.txt")
    session.chdir("sphinx_presentation/source")

    if "pdf" in session.posargs:
        session.run("sphinx-build", "-M", "latexpdf", ".", "_build")
        return

    session.run("sphinx-build", "-M", "html", ".", "_build")

    if "serve" in session.posargs:
        session.log("Launching docs at http://localhost:8000/ - use Ctrl-C to quit")
        session.run("python", "-m", "http.server", "8000", "-d", "_build/html")
    elif session.posargs:
        session.error("Unsupported argument to docs")
