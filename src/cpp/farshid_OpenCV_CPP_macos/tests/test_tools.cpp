#include <gtest/gtest.h>
#include <iostream>

TEST(SimpleTest, ShowMessage) {
    std::cout << "Hello from Google Test!" << std::endl;
    EXPECT_EQ(1, 1);  // Dummy test to make sure the framework works
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
