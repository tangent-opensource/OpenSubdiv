import os, subprocess, sys
import shutil

if __name__ == "__main__":
    src = os.environ["HOUDINI_ROOT"]
    dst = os.environ["REZ_BUILD_INSTALL_PATH"]
    inc_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/include"
    lib_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/lib"

    
    if 'win' in str(sys.platform):

        # Remove existing build
        if os.path.exists(dst):
            print(" - Removing existing build")
            shutil.rmtree(dst, ignore_errors=True)


        shutil.copytree(src + "/toolkit/include/opensubdiv", inc_dst + "/opensubdiv")
        
        os.mkdir(lib_dst)

        shutil.copy(src + '/custom/houdini/dsolib/libosdCPU_md.lib', lib_dst + "/osdCPU.lib")
        shutil.copy(src + '/custom/houdini/dsolib/libosdGPU_md.lib', lib_dst + "/osdGPU.lib")

    else:

        # Remove existing build
        if os.path.exists(dst):
            print(" - Removing existing build")
            shutil.rmtree(dst, ignore_errors=True)


        shutil.copytree(src + "/toolkit/include/opensubdiv", inc_dst + "/opensubdiv")
        
        os.mkdir(lib_dst)

        shutil.copy(src + '/dsolib/libosdCPU.so.3.4.3', lib_dst + "/libosdCPU.so")
        shutil.copy(src + '/dsolib/libosdGPU.so.3.4.3', lib_dst + "/libosdGPU.so")
