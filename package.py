name = 'opensubdiv'

version = '3.4.3-houdini-18.5.351-ta.1.0.0'

authors = [
    'benjamin.skinner',
    'pixar',
    'sidefx',
]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

private_build_requires = [
    'python-2',
    'houdini-18.5.351',
]

requires = [
    'glew-1.1.0-houdini',
]

build_command = "python {root}/rez_build.py"

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.OPENSUBDIV_VERSION.set(split_versions[0])
    env.OPENSUBDIV_PACKAGE_VERSION.set(split_versions[1])

    env.OPENSUBDIV_ROOT_DIR.set("{root}")
    env.OPENSUBDIV_LIB_DIR.set( "{root}/lib" )
    env.OPENSUBDIV_INCLUDE_DIR.set( "{root}/include" )