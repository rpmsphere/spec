%global debug_package %{nil}
%global __os_install_post %{nil}

%define		_prefix		/opt/Geant4
%define		clhep_version	2.2.0.8
%define		g4system	Linux-g++
%define		runcheck	1

Summary:	Geant4 is an acronym of GEometry ANd Tracking
Name:		geant4
Version:	10.02
Release:	9.1
License:	Geant4 Software License
Group:		Development/Libraries/C and C++
URL:		http://geant4.cern.ch/
Source0:	http://geant4.cern.ch/support/source/geant4.%{version}.tar.gz
#Source1:	geant4-env-funcs.sh
BuildRequires:	gcc, gcc-c++
BuildRequires:	mesa-libGL-devel, mesa-libGLU-devel, xorg-x11-proto-devel, motif-devel, xerces-c-devel
BuildRequires:  libXmu-devel, libXpm-devel, libXi-devel
Requires:	libX11, mesa-libGL, mesa-libGLU, motif, xerces-c
BuildRequires:	clhep-devel
Requires:	glibc, libgcc, libstdc++
#Requires:	dawn, vrmlview
Requires:	clhep = %{clhep_version}

%description
Geant4 is a toolkit for the simulation of the passage of particles
through matter. Its areas of application include high energy, nuclear
and accelerator physics, as well as studies in medical and space
science. The two main reference papers for Geant4 are published in
Nuclear Instruments and Methods in Physics Research A 506 (2003)
250-303, and IEEE Transactions on Nuclear Science 53 No. 1 (2006)
270-278.

%package devel
Summary:	Geant4: Static libraries, C++ header files and so on
Group:		Development/Libraries/C and C++
Requires:	%{name} = %{version}
Requires:	clhep-devel = %{clhep_version}
Requires:	xorg-x11-proto-devel, motif-devel, libXi-devel, xerces-c-devel


%description devel
The static libraries and C++ header files are additionally included in this package and some scripts required at the compilation; i.e. stuffs placed under the config directory; are also inclusive. This is mainly focused for users classified the application developer.

%package source
Summary:	Geant4: Sources and examples
Group:		Development/Libraries/C and C++
Requires:	%{name} = %{version}

%description source
All of sources and various examples are included in this package. This is mainly focused for users classified the class library developer.

%prep
%setup -n %{name}.%{version}
#%{__cp} -p %{SOURCE1} ./config/scripts/

# modify system/Linux-g++.gmk file to link to lib64 dir
%ifarch x86_64
#
# No more need following patch from version 9.2
# 
# fixed as follows
#   ARCH   := $(shell uname -m | cut -s -d "_" -f 2)
#   X11LIBS   := -L/usr/X11R6/lib$(ARCH) 
#%{__cp} -p ./config/sys/%{g4system}.gmk ./config/sys/%{g4system}.gmk.orig
#%{__sed} -i -e 's/\(\/usr\/X11R6\/\)\(lib\)/\1\264/g' -e 's/\($(OGLHOME)\/\)\(lib\)/\1\264/g' ./config/sys/%{g4system}.gmk
#
# Still remain this patch: geant4/clhep libs are placed in lib64
%{__cp} -p ./config/architecture.gmk ./config/architecture.gmk.orig
%{__sed} -i -e 's/\($(G4INSTALL)\/lib\)/\164/g' -e 's/\($(CLHEP_BASE_DIR)\/lib\)/\164/g' -e 's/\(.*GDMLLIBS.*\)\(-L.*\/lib\)\(.*\)/\1\264\3/g' ./config/architecture.gmk
%endif


%build
# failed to grep, eventually rpmbuild failure
export G4_dummy=dummy

envs=`env | egrep '^G4|^CLHEP' > /dev/null 2>&1`
if test "x${envs+x}" = "xx"; then
    for env in "$envs"; do
        name=`echo "$env" | cut -d'=' -f1`
        unset $name
    done
    unset name env
fi
unset envs
if test "x${CXX+x}" = "xx"; then
    unset CXX
fi
export G4SYSTEM=%{g4system}
export G4INSTALL=%{_builddir}/%{name}.%{version}
export CLHEP_BASE_DIR=/opt/clhep
export G4LIB_BUILD_GDML=1
export XERCESCROOT=/usr
export G4VIS_BUILD_DAWN_DRIVER=1
export G4VIS_BUILD_VRML_DRIVER=1
export G4VIS_BUILD_RAYTRACERX_DRIVER=1
export G4VIS_BUILD_OPENGLX_DRIVER=1
export G4VIS_BUILD_OPENGLXM_DRIVER=1
cd $G4INSTALL/source
%{__make} %{?_smp_mflags}

export G4LIB_BUILD_SHARED=1
export G4LIB=$G4INSTALL/lib
export G4TMP=$G4INSTALL/tmp
cd $G4INSTALL/source
%{__make} %{?_smp_mflags}
%{__make} global
%{__make} includes

#
# dynamically locates setting shells
#
mkdir -p $G4INSTALL/config/scripts
%{__cat} <<EOF > $G4INSTALL/config/scripts/%{name}-env-funcs.sh
# Functions for manipulating the environment variables
#
# __path_prepend - prepend a value to a path-like environmnet variable
#                                     - puts a ':' to the end end the beginning of the variable
#                                     - removes the value from the string and removes duplicate '::'
#                                     - prepend the value to the beginning of the variable
#                                     - removes duplicate '::' and removes ':' from the beginning and the end variable
#                                     - MANPATH has to be treated specially since, :: has a meaning -> don't get removed
#                                     - Simple : could have a meaning so if it was there in the end or the begining we should not remove it.
#                                     - export the variable, or echos the csh syntax
#
# __path_append - the same as prepend but it appends the value to the end of the variable
# __env_delete  - delete a value from an environment variable. if the value becomes null string then it unsets the environment variable
# __env_set     - sets an environment variable
# __env_setind  - sets an environment variable if it is not already defined


function __path_prepend() {
    myvar="\$1"
    myvalue="\$2"
    myfieldsep=":"
    mytmp="\${!myvar}"

    if [ "x\$mytmp" = "x\$myvalue" ] || [ "x\$mytmp" = "x\$myfieldsep\$myvalue" ] || [ "x\$mytmp" = "x\$myvalue\$myfieldsep" ] ; then
        mytmp="\${mytmp//\$myvalue/}"
    else
        mytmp="\${mytmp//\$myfieldsep\$myvalue\$myfieldsep/\$myfieldsep}" 	#remove if in the middle
        mytmp="\${mytmp#\$myvalue\$myfieldsep}"					#remove if in the begining
        mytmp="\${mytmp%\$myfieldsep\$myvalue}"					#remove if at the end
    fi

    if [ "x\$mytmp" = "x" ]; then
	mytmp="\$myvalue"
    else
	mytmp="\$myvalue\$myfieldsep\$mytmp"
    fi

    mytmp="\${mytmp//\$myfieldsep\$myfieldsep\$myfieldsep/\$myfieldsep\$myfieldsep}"

    if [ "x\$myvar" = "xMANPATH" ] ; then
        mytmp="\${mytmp}::"
    fi
    if [ "x\$ISCSHELL" = "xyes" ]; then
        echo "setenv \$myvar \\"\$mytmp\\"" 
    fi
    eval export \${myvar}=\\""\$mytmp"\\"
}

function __path_append() {
    myvar="\$1"
    myvalue="\$2"
    myfieldsep=":"
    mytmp="\${!myvar}"
    
    if [ "x\$mytmp" = "x\$myvalue" ] || [ "x\$mytmp" = "x\$myfieldsep\$myvalue" ] || [ "x\$mytmp" = "x\$myvalue\$myfieldsep" ] ; then
        mytmp="\${mytmp//\$myvalue/}"
    else
        mytmp="\${mytmp//\$myfieldsep\$myvalue\$myfieldsep/\$myfieldsep}" 	#remove if in the middle
        mytmp="\${mytmp#\$myvalue\$myfieldsep}"					#remove if in the begining
        mytmp="\${mytmp%\$myfieldsep\$myvalue}"					#remove if at the end
    fi

    if [ "x\$mytmp" = "x" ]; then 
        mytmp="\$myvalue"
    else
   	mytmp="\$mytmp\$myfieldsep\$myvalue"
    fi

    mytmp="\${mytmp//\$myfieldsep\$myfieldsep\$myfieldsep/\$myfieldsep\$myfieldsep}"

    if [ "x\$myvar" = "xMANPATH" ] ; then
        mytmp="\${mytmp}::"
    fi
    if [ "x\$ISCSHELL" = "xyes" ]; then
        echo "setenv \$myvar \\"\$mytmp\\"" 
    fi
    eval export \${myvar}=\\""\$mytmp"\\"
} 

function __env_delete() {
    myvar="\$1"
    myvalue="\$2"
    myfieldsep=":"
    mytmp="\${!myvar}"
		                
    if [ "x\$mytmp" = "x\$myvalue" ] || [ "x\$mytmp" = "x\$myfieldsep\$myvalue" ] || [ "x\$mytmp" = "x\$myvalue\$myfieldsep" ] ; then
        mytmp="\${mytmp//\$myvalue/}"
    else
  	mytmp="\${mytmp//\$myfieldsep\$myvalue\$myfieldsep/\$myfieldsep}"            
        mytmp="\${mytmp#\$myvalue\$myfieldsep}"                                 
        mytmp="\${mytmp%\$myfieldsep\$myvalue}"                                 
    fi

    mytmp="\${mytmp//\$myfieldsep\$myfieldsep\$myfieldsep/\$myfieldsep\$myfieldsep}"

    if [ "x\$ISCSHELL" = "xyes" ]; then
        echo "setenv \$myvar \\"\$mytmp\\"" 
    fi
    eval export \${myvar}=\\""\$mytmp"\\"
}

function __env_set() {
    myvar="\$1"
    myvalue="\$2"
    myfieldsep=":"

    if [ "x\$ISCSHELL" = "xyes" ]; then
        echo "setenv \$myvar \\"\$myvalue\\"" 
    fi
    eval export \${myvar}="\\"\${myvalue}\\""
}

function __env_setind() {
    myvar="\$1"
    myvalue="\$2"
    if [ "x\$ISCSHELL" = "xyes" ]; then
	echo 'if ( \${?'\$myvar'} == 0 ) setenv '\$myvar \\'"\$myvalue"\\'
    fi
    eval export \$myvar=\\\${\$myvar:-\\\$myvalue}
}
EOF

%{__cat} <<EOF > $G4INSTALL/config/scripts/%{name}-env.sh
if test "x\${G4_ENV_SET+x}" = "x"; then
. %{_prefix}/config/scripts/%{name}-env-funcs.sh
__env_set	"G4SYSTEM"		"%{g4system}"
__env_set	"G4INSTALL"		"%{_prefix}"
__env_set	"CLHEP_BASE_DIR"	"`clhep-config --prefix`"
__env_set	"G4LIB_BUILD_GDML"	"1" # Bug in architecture.gmk line 262!
__env_set	"G4LIB_USE_GDML"	"1"
__env_set	"XERCESCROOT"		"/usr"
__env_set	"G4VIS_USE_DAWN"	"1"
__env_set	"G4VIS_USE_VRML"	"1"
__env_set	"G4VIS_USE_RAYTRACERX"	"1"
__env_set	"G4VIS_USE_OPENGLX"	"1"
__env_set	"G4VIS_USE_OPENGLXM"	"1"
__env_set	"G4UI_USE_TCSH"		"1"
__env_set	"G4UI_USE_GAG"		"1"
#
# to make and link shared libs, uncomment below and activate it or insert a line 'G4LIB_BUILD_SHARED := 1' in your makefile
#__env_set	"G4LIB_BUILD_SHARED"	"1"
#
# following 2 lines should be defined by a user 
#__env_set	"G4DAWNFILE_PS_VIEWER"	"gv"
#__env_set	"G4VRMLFILE_VIEWER"	"vrmlview"
__env_set	"G4_ENV_SET"		"1"
unset __path_prepend __path_append __env_delete __env_set __env_setind
fi
EOF

%{__cat} <<EOF > $G4INSTALL/config/scripts/%{name}-env.csh
set mycshtmpfile=\`mktemp /tmp/%{name}-env.XXXXXX\`
bash -c "export ISCSHELL=yes; source %{_sysconfdir}/profile.d/%{name}-env.sh" >> \$mycshtmpfile
source \$mycshtmpfile
rm -f \$mycshtmpfile
EOF


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_prefix}
%{__cp} -pr %{_builddir}/%{name}.%{version}/lib %{buildroot}%{_prefix}/
%{__cp} -pr %{_builddir}/%{name}.%{version}/ReleaseNotes %{buildroot}%{_prefix}/
%{__cp} -p %{_builddir}/%{name}.%{version}/LICENSE %{buildroot}%{_prefix}/

%{__mkdir_p} %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_prefix}/lib/%{g4system}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# devel
%{__cp} -pr %{_builddir}/%{name}.%{version}/config %{buildroot}%{_prefix}/
%{__cp} -pr %{_builddir}/%{name}.%{version}/cmake %{buildroot}%{_prefix}/
%{__cp} -pr %{_builddir}/%{name}.%{version}/include %{buildroot}%{_prefix}/
# to avoid printing error message 'permission denied' due to making directory /opt/geant4/tmp and /opt/geant4/bin
# while building user's app
%{__mkdir_p} %{buildroot}%{_prefix}/bin
%{__mkdir_p} %{buildroot}%{_prefix}/tmp

# source
%{__cp} -pr %{_builddir}/%{name}.%{version}/source %{buildroot}%{_prefix}/
%{__cp} -pr %{_builddir}/%{name}.%{version}/examples %{buildroot}%{_prefix}/

%clean
%{__rm} -rf %{buildroot}

%post

%postun
if test $1 = 0; then
fi

%post devel
%{__ln_s} %{_prefix}/config/scripts/%{name}-env.sh %{_sysconfdir}/profile.d/%{name}-env.sh
%{__ln_s} %{_prefix}/config/scripts/%{name}-env.csh %{_sysconfdir}/profile.d/%{name}-env.csh

%postun devel
if test $1 = 0; then
    %{__rm} -f %{_sysconfdir}/profile.d/%{name}-env.sh
    %{__rm} -f %{_sysconfdir}/profile.d/%{name}-env.csh
fi

%files
%dir %{_prefix}
%{_prefix}/ReleaseNotes
%{_prefix}/lib
%{_prefix}/LICENSE
%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%files devel
%{_prefix}/include
%{_prefix}/config
%{_prefix}/cmake
%{_prefix}/bin
%{_prefix}/tmp

%files source
%{_prefix}/source
%{_prefix}/examples

%changelog
* Thu Jan 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 10.02
- Rebuild for Fedora
* Sun Dec  6 2009 Go Iwai <go.iwai@kek.jp> - 9.2.p02
- Update to 9.2.p02
* Sun May 17 2009 Go Iwai <go.iwai@kek.jp> - 9.2.p01
- The update package version 9.2 to 9.2.p01
- Build with clhep version 2.0.4.2
* Wed Jan 14 2009 Go Iwai <go.iwai@kek.jp> - 9.2
- The update package version 9.1.p03 to 9.2
- Build with clhep version 2.0.4.2
- New: G4GDML module is now included in the package
- To do this above, xerces-c-devel in DAG repository is required while building the package and xerces is also required on the execution of Geant4 application
- G4LIB_BUILD_GDML variable should be set even in user application, this is a bug in architecture.gmk line 262
- Fixed (devel): g4sysdir is properly deleted on removing this package
- Patch for x86_64 arch in Linux-g++.gmk is removed from this version
* Thu Sep 25 2008 Go Iwai <go.iwai@kek.jp> - 9.1.p03
- G4DAWNFILE_PS_VIEWER has been removed, should be preferably defined by a user.
- G4VRMLFILE_VIEWER has been removed, should be preferably defined by a user.
- To develop user's apps easier, xorg-x11-devel (libGL/libGLU) and openmotif-devel (libXm) are additionally required for Vis OpenGL.
* Wed Sep 24 2008 Go Iwai <go.iwai@kek.jp> - 9.1.p03
- The update package 9.1.p02 to 9.1.p03
- geant4-env-funcs.sh has been removed from source of package, it's dynamically created into scripts dir instead. Actually, therfore, no change.
- Naming convention of G4 source archive seems to be chnaged since this version, i.e. geant4-x.y.gtar.gz to geant4-x.y.tar.gz, its' rather good change.
- Removed it 'Requires: dawn, vrmlview' based on suggestion from the meeting at LAPP, Annecy, France. However, G4VRMLFILE_VIEWER still is set of vrmlview, potentially cause of problem.
- Requires: clhep-devel is additionally required by geant4-devel. Always G4 developer needs it.
* Tue Jul 29 2008 Go Iwai <go.iwai@kek.jp> - 9.1.p02
- The update package from 9.1.p01 to 9.1.p02 released on Day of Niku
* Thu May 29 2008 Go Iwai <go.iwai@kek.jp> - 9.1.p01
- The 1st packaging of Geant4 released on Day of Niku
