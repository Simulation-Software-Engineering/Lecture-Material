#define BOOST_TEST_MODULE Hello World Test
#include <boost/test/included/unit_test.hpp>

BOOST_AUTO_TEST_CASE(SomeTest)
{
  int i = 1;
  BOOST_TEST(i == 2);
}
