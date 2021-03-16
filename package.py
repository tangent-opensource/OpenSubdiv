name = 'opensubdiv'

houdini_version = '18.5.499'

version = '3.4.3-houdini-{}-ta.1.1.0'.format(houdini_version)

authors = [
    'benjamin.skinner',
    'pixar',
    'sidefx',
]


linux_variants = [
    ['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

windows_variants = [ 
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

@early()
def variants():
    import sys
    if 'win' in str(sys.platform):
        return windows_variants
    else:
        return linux_variants

private_build_requires = [
    'python-2',
    'houdini-{}'.format(houdini_version),
]

requires = [
    'glew-1.13.0-houdini',
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
