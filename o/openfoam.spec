%global debug_package %{nil}
Name:		openfoam
Version:	2.2.2
Release:	16.1
Group:		Sciences/Physics
License:	GPL
Summary:	The open source CFD toolbox
URL:		http://www.opencfd.co.uk/openfoam/
Source0:	http://downloads.sourceforge.net/foam/OpenFOAM-%{version}.tgz
Source1:	http://downloads.sourceforge.net/foam/ThirdParty-%{version}.tgz
BuildRequires:	cmake
BuildRequires:	libGL-devel
BuildRequires:	gmp-devel
BuildRequires:	gnuplot
BuildRequires:	hdf5-devel
BuildRequires: 	libtiff-devel
BuildRequires:	libXt-devel
BuildRequires:	mpfr-devel
BuildRequires:	openmpi-devel
BuildRequires:	paraview-openmpi-devel
BuildRequires:	netcdf
BuildRequires:	python2-devel
BuildRequires:	qt4-devel
BuildRequires:	qt4-assistant
BuildRequires:	libmetis-edf-devel
BuildRequires:	readline-devel
BuildRequires:	scotch-devel
BuildRequires:	tk-devel
BuildRequires:	zlib-devel
BuildRequires:	environment-modules
#Requires:	task-c-devel
BuildRequires:  atlas
%ifarch x86_64
BuildRequires:  infinipath-psm
%endif

%description
OpenFOAM is a free, open source CFD software package produced by a
commercial company, OpenCFD Ltd. It has a large user base across most
areas of engineering and science, from both commercial and academic
organisations. OpenFOAM has an extensive range of features to solve
anything from complex fluid flows involving chemical reactions,
turbulence and heat transfer, to solid dynamics and electromagnetics.

%prep
tar zxf %{SOURCE0}
tar zxf %{SOURCE1}
find . -name fileMonitor.C

%build
export FOAM_INST_DIR=%{_builddir}
. OpenFOAM-%{version}/etc/bashrc

# Build paraview first as it is not built by default.
#pushd ThirdParty-%{version}
#sh ./makeParaView
#popd

pushd OpenFOAM-%{version}
sh ./Allwmake
popd

%install
# Match binaries distributed by upstream (reducing from 800+ to 300+ Mb install)
find OpenFOAM-%{version}/applications \( -name \*.o -o -name \*.dep \) | xargs rm -f
find OpenFOAM-%{version}/src \( -name \*.o -o -name \*.dep \) | xargs rm -f
%ifarch x86_64
LIBDIR=linux64GccDPOpt
%else
LIBDIR=linuxGccDPOpt
%endif
for make in `find OpenFOAM-%{version} -name Make`; do
    rm -fr $make/$LIBDIR
done
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -fpar OpenFOAM-%{version} %{buildroot}%{_datadir}/%{name}

#perl -pi -e "s|(libdir=').*(/ThirdParty.*)|$1%{_datadir}/%{name}$2|;"	\
#    `find ThirdParty-%{version}/platforms -name \*.la`
rm -f `find ThirdParty-%{version}/platforms -name \*.la`

mkdir -p %{buildroot}%{_datadir}/%{name}/ThirdParty-%{version}
cp -fpar ThirdParty-%{version}/platforms %{buildroot}%{_datadir}/%{name}/ThirdParty-%{version}

# avoid dependency on /usr/xpg4/bin/sh
rm -f %{buildroot}%{_datadir}/%{name}/OpenFOAM-%{version}/bin/tools/replaceAllShellSun

# correct permissions
find %{buildroot}%{_datadir}/%{name}/OpenFOAM-%{version} -perm 0640 | xargs chmod 0644
find %{buildroot}%{_datadir}/%{name}/OpenFOAM-%{version} -perm 0750 | xargs chmod 0755

mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh

export FOAM_INST_DIR=%{_datadir}/%{name}
export PS1="OpenFOAM-%{version}:\u@\h:\W: "
. %{_datadir}/%{name}/OpenFOAM-%{version}/etc/bashrc
if [ ! -d \$FOAM_RUN ]; then
    mkdir -p \$FOAM_RUN
    cp -r \$FOAM_TUTORIALS \$FOAM_RUN 
fi
cd \$FOAM_RUN
exec /bin/bash
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Jan 22 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.2
- Rebuild for Fedora
* Sat Jan 28 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1.0-2mdv2012.0
+ Revision: 769490
- Add conditional to build paraview.
- Correct permissions of installed files.
- Install third party dynamic scotch libraries.
- Modify script to setup user environment and copy tutorials.
* Thu Jan 19 2012 Sergey Zhemoitel <serg@mandriva.org> 2.1.0-1
+ Revision: 762802
- add new version 2.1.0
- new version 2.0.1
* Fri May 20 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.7.1-1
+ Revision: 676453
- Import OpenFOAM 1.7.1
