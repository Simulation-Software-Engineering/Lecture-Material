# Boost.Test and CTest for Testing C++ Codes

## Hello World

```cpp
#define BOOST_TEST_MODULE Hello World Test
#include <boost/test/included/unit_test.hpp>

BOOST_AUTO_TEST_CASE(SomeTest)
{
  int i = 1;
  BOOST_TEST(i == 2);
}
```

- explain code
  - uses UTF in header-only mode (can also be used as library, more later)
  - UTF defines `main` function for us (could also be done manually)
  - give name to `BOOST_TEST_MODULE`
  - single test case, which is added automatically with `AUTO` (could also be done manually)
- build: `g++ -o test helloWorldTest.cpp`
- run: `./test`
- inspect: `./test --help` and `./test --list_content` (`*` means that a testcase is active)
