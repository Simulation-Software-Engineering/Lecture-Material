# Notes for Technical Writing Demo

Example code is in [`04_documentation/examples/technical_writing`](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/04_documentation/examples/technical_writing).

- Look at Python code. Same as in packaging exercise, but now refactored into different functions. Run code.
- We are using [numpydoc](https://numpydoc.readthedocs.io/en/latest/) as syntax (there is also Google style).

## Class Documentation

- Add short description:

    ```diff
    + """2D diffusion equation solved with finite differences
    + """
    ```

- Add long description, example usage:

    ```diff
    + See `main()` for example usage
    ```

## Method Documentation

- Constructor:

    ```diff
    + """Constructs an uninitialized 2D diffusion solver
    +
    + After construction, initialize domain with `initialize_domain` and
    + initialize the physical parameters with `initialize_physical_parameters`.
    + """
    ```

- `initialize_domain`:

    ```diff
    + """Initializes domain and mesh of the domain
    +
    + - Sets width and height of the domain.
    + - Also sets mesh width in x and in y direction.
    + - Using these four values, the method computes the number of mesh elements in x and in y direction.
    """
    ```

- `initialize_physical_parameters`:

    ```diff
    + """Initializes physical parameters and computes time step size
    +
    + You need to call `initialize_domain` before this method.
    + """
    ```

- Ideally, we also add a link to source of time step size computation here.

## Parameters Documentation

- Add to `initialize_domain`:

    ```diff
    + Parameters
    + ----------
    + w : float, default: 10.0
    +     width of the domain
    + h : float, default: 10.0
    +     height of the domain
    + dx : float, default: 0.1
    +     mesh width in x direction
    + dy : float, default: 0.1
    +     mesh width in y direction
    ```
