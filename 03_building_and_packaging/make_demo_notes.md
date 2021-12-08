# Notes for Make demo

Example code is in [`building-and-packaging/material/examples/make`](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/building-and-packaging/material/examples/make).

## "Hello World" starting point

Show `main.cpp` and build by hand `g++ -o helloworld main.cpp`

```cpp
#include <iostream>

int main()
{
  std::cout << "Hello World!" << std::endl;
  return 0;
}
```

## Single rule example

- Remove `helloworld`.
- Show `Makefile`.
- Explain that `helloworld` depends on `main.cpp` and rule to update.
- Three cases:
    - no `helloworld`: run update
    - `helloworld` older than `main.cpp`: run update
    - `helloworld` newer than `main.cpp`: do nothing

- Run make twice.
- `ls -la` to show timestamp
- Requires actual tabs, spaces not allowed. Show error message.

> Makefile:2: *** missing separator (did you mean TAB instead of 8 spaces?).  Stop.

## Multiple rules example and phony targets

- Show `sse.hpp` and `sse.cpp` in subfolder `sse`.
- Use it.

`main.cpp`:

```diff
#include <iostream>
+ #include "sse.hpp"

int main()
{
  std::cout << "Hello World!" << std::endl;
+ sse();
  return 0;
}
```

`Makefile`:

```makefile
sse.o : sse/sse.hpp sse/sse.cpp
	$(CXX) -c sse/sse.cpp

helloworld : main.cpp sse.o
	$(CXX) -o helloworld sse.o main.cpp
```

- Run `make`, only builds `sse.o`.
- By default, first target is built.
- `make helloworld` to build specific target
- phony target (a helper target, doesn't correspond to a file)

```diff
+ all : helloworld sse.o
```

- Why does Make not just build directly build all targets? We could want to do different things with different targets.
- `all` typically comes first.
- Add `clean` target, has no dependency.

```diff
+ clean :
+ 	rm -f helloworld sse.o
```

- Run `make clean`
- `mkdir clean` and `make clean` confuses Make

```
+ .PHONY : all clean
```

- `all` and `clean` are standard targets. All makefiles should have them.
- Last remark: `make -j` builds in parallel.
