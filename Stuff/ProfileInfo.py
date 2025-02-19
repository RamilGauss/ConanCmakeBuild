fileName = "Profile"

template = """[settings]
os=$operatingSystem
arch=x86_64
compiler=msvc
compiler.version=194
compiler.cppstd=20
compiler.runtime=dynamic
build_type=$buildType

[conf]
tools.cmake.cmaketoolchain:generator=Ninja
"""