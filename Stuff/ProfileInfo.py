fileName = "Profile"

template = """[settings]
os=$operatingSystem
arch=x86_64
compiler=clang
compiler.version=19
compiler.cppstd=20
build_type=$buildType

[buildenv]
CC=clang.exe
CXX=clang++.exe
toolset=clang-win

[conf]
tools.cmake.cmaketoolchain:generator=Ninja
"""