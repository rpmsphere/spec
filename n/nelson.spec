%undefine _debugsource_packages
%global __os_install_post %{nil}

Summary: The Nelson Programming Language
Name: nelson
Version: 0.6.7
Release: 1
License: GPLv2
Group: Development/Language
URL: https://nelson-numerical-software.github.io/nelson-website/
Source0: https://github.com/Nelson-numerical-software/nelson/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: eigen3-devel
BuildRequires: matio-devel
BuildRequires: openmpi-devel
BuildRequires: libsndfile-devel
BuildRequires: libgit2-devel
AutoReq: off
Requires: openmpi
Requires: qt5-qtbase-gui qt5-qtdeclarative alsa-lib boost libcurl libevent libffi flexiblas-netlib libgcc libgit2 libgomp
Requires: hdf5 hwloc-libs libicu jack-audio-connection-kit lapack matio portaudio libsndfile libstdc++ taglib libxml2 zlib

%description
The aim of Nelson is providing a powerful open computing environment for
engineering and scientific applications using modern C/C++ libraries
(Boost, Eigen, FFTW, ...) and others state of art numerical libraries.

It has sophisticated data structures (including cell, struct, linear
systems...), an interpreter and a high level programming language.

Nelson has been developed to be an open/modular system where an user can define
these own data types and operations on these data types by using overload.

%prep
%setup -q
sed -i 's|fscanf(filepointer, np)|fscanf(filepointer, "%s", np)|' modules/stream_manager/src/cpp/FscanFunction.cpp

%build
#cmake -G "Unix Makefiles" .
cmake . -DCMAKE_INSTALL_PREFIX=/usr/libexec -DCMAKE_BUILD_TYPE=release -DMPI_C_COMPILER=/usr/lib64/openmpi/bin/mpicc -DMPI_CXX_COMPILER=/usr/lib64/openmpi/bin/mpicxx -DMPI_C_INCLUDE_PATH=/usr/include/openmpi-x86_64/
make

%install
%make_install
mkdir -p %{buildroot}%{_bindir}
cd %{buildroot}%{_libexecdir}/Nelson-%{version}/bin/linux
sed -i 's|$0|$(realpath $0)|' %{name}-*i
for i in %{name}-*i; do
  ln -s %{_libexecdir}/Nelson-%{version}/bin/linux/$i %{buildroot}%{_bindir}/$i
done
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libexecdir}/Nelson-%{version}/bin/linux > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
echo %{_libdir}/openmpi/lib >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_libexecdir}/*
%{_bindir}/%{name}-*
%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%changelog
* Sun Aug 7 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.7
- Rebuilt for Fedora
