name = 'opensubdiv'

version = '3.4.3-ta.1.0.0'

authors = [
    'benjamin.skinner',
    'pixar',
]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

requires = [
    'glew-2.0.0',
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

build_system = "cmake"

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.OPENSUBDIV_VERSION.set(split_versions[0])
    env.OPENSUBDIV_PACKAGE_VERSION.set(split_versions[1])

    env.OPENSUBDIV_ROOT_DIR.set("{root}")
    env.OPENSUBDIV_LIB_DIR.set( "{root}/lib" )
    env.OPENSUBDIV_INCLUDE_DIR.set( "{root}/include" )