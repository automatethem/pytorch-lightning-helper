rom setuptools import setup

VERSION = "0.1"

setup(
    name="datasette-expose-some-environment-variables",
    description="Expose environment variables in Datasette at /-/env",
    author="Simon Willison",
    license="Apache License, Version 2.0",
    version=VERSION,
    py_modules=["datasette_expose_some_environment_variables"],
    entry_points={
        "datasette": [
            "expose_some_environment_variables = datasette_expose_some_environment_variables"
        ]
    },
    install_requires=["datasette"],
)
