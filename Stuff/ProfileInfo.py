fileName = "Profile"

template = """[settings]
os=$operatingSystem
arch=x86_64
compiler=clang
compiler.version=19
compiler.cppstd=20
compiler.libcxx=libstdc++11
build_type=$buildType

[buildenv]
# CC=clang.exe
# CXX=clang++.exe

[conf]
tools.cmake.cmaketoolchain:generator=Ninja
"""