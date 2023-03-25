#include "gtest/gtest.h"

TEST(HelloTest, GetGreet) {
  EXPECT_EQ("Hello bazel", "Hello bazel");
}
