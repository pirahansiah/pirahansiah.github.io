workspace "pytorchCPP"
   configurations { "Debug", "Release" }

project "pytorchCPP"
   kind "ConsoleApp"
   language "C++"
   cppdialect "C++17"

   targetdir "bin/%{cfg.buildcfg}"

   files { "src/**.cpp", "include/**.h" }

   includedirs { "/Users/farshid/farshid/2024/libtorch/include", "include" }
   libdirs { "/Users/farshid/farshid/2024/libtorch/lib" }
   links { "torch", "c10" }

   filter "system:macosx"
      systemversion "latest"
      -- Add the necessary frameworks here (Metal, etc.) if you are using them

   filter "configurations:Debug"
      defines { "DEBUG" }
      symbols "On"

   filter "configurations:Release"
      defines { "NDEBUG" }
      optimize "On"
