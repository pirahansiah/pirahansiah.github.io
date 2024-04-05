// //  /*
// // // brew install jpeg libpng libtiff openexr
// // // brew install opencv 
// // // //g++ -o fp1 fp1.cpp `pkg-config --cflags --libs opencv4`
// // // export PKG_CONFIG_PATH="/usr/local/Cellar/opencv/4.9.0_3/lib/pkgconfig:$PKG_CONFIG_PATH"
// // // pkg-config --cflags opencv4

// // brew info qt
// // export QTDIR=/usr/local/Cellar/qt/5.15.12
// // export PATH=$QTDIR/bin:$PATH


// //                 "-I",
// //                 "/usr/local/Cellar/qt@5/5.15.12_1/include", 
// //                 "-L",
// //                 "/usr/local/Cellar/qt@5/5.15.12_1/lib",



// // #include <opencv2/opencv.hpp>
// // #include <iostream>

// // int main(void)
// // {
// //     cv::Mat img=cv::imread("a.jpg");
// //     cv::imshow("image",img);
// //     cv::waitKey(10000);

// //     std::cout << "Hello, World" << std::endl;
// // }


// // Farshid Pirahansiah
// // */
// // #include <iostream>

// // #include <format>
// // //g++ -std=c++2b -I/usr/local/include -L/usr/local/lib  farshid.cpp -o f
// // //#include "opencv2/opencv.hpp"
// // //using namespace cv;
// // using namespace std;
// // int main(int argc, const char * argv[]) {
// //     std::cout <<__cplusplus<< " C20 Hello, World!\n";
// //     std::format::print("Hello, {}!\n", "world");
// //     // cout << "OpenCV version : " << CV_VERSION << endl;
// //     // cout << "Major version : " << CV_MAJOR_VERSION << endl;
// //     // cout << "Minor version : " << CV_MINOR_VERSION << endl;
// //     // cout << "Subminor version : " << CV_SUBMINOR_VERSION << endl;
// //     return 0;
// // }
// #include <format>
// #include <iostream>
// #include <string_view>
// #include <numbers>

// using std::numbers::pi;
// using std::cout;
// //using std::format;
// // using std::__format;
// // using std::format_to;
// // using std::format_args;

// template<typename T>
// struct Frac {
//     T n;
//     T d;
// };

// // // format-style print()
// // constexpr void print(const std::string_view str_fmt, auto&&... args) {
// //     fputs(std::vformat(str_fmt, std::make_format_args(args...)).c_str(), stdout);
// // }

// // // format specialization
// // template <typename T>
// // struct std::formatter<Frac<T>> : std::formatter<int> {
// //     template <typename Context>
// //     auto format(const Frac<T>& f, Context& ctx) const {
// //         return format_to(ctx.out(), "{}/{}", f.n, f.d);
// //     }
// // };

// int main() {
//     std::cout <<__cplusplus<< "   b C23 Hello, World!\n";
//     const int inta {47};
//     const char * human {"earthlings"};
//     const std::string_view alien {"vulcans"};
//     const double df_pi {pi};

//     // cout << format("Hello {}\n", human);

//     // print("Hello {} we are {}\n", human, alien);
//     // print("Hello {1} we are {0}\n", human, alien);

//     // print("π is {}\n", df_pi);
//     // print("π is {:.5}\n", df_pi);
//     // print("inta is {1:}, π is {0:.5}\n", df_pi, inta);

//     // print("inta is [{:*<10}]\n", inta);
//     // print("inta is [{:0>10}]\n", inta);
//     // print("inta is [{:^10}]\n", inta);
//     // print("inta is [{:_^10}]\n", inta);

//     // print("{:>8}: [{:04X}]\n", "Hex", inta);
//     // print("{:>8}: [{:4o}]\n", "Octal", inta);
//     // print("{:>8}: [{:4d}]\n", "Decimal", inta);

//     // Frac<long> n {3, 5};
//     // print("Frac: {}\n", n);
// }
