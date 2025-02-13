conan install --output-folder=build --build=missing --profile:host=./Profile --profile:build=./Profile --requires=fmt/11.1.1 -g CMakeDeps -g CMakeToolchain

cmake --preset conan-debug
cmake --build --preset conan-debug