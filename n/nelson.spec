%undefine _debugsource_packages

Summary: The Nelson Programming Language
Name: nelson
Version: 0.5.9
Release: 1
License: GPLv2
Group: Development/Language
URL: https://nelson-numerical-software.github.io/nelson/
Source0: https://github.com/Nelson-numerical-software/nelson/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: eigen3-devel
BuildRequires: matio-devel
BuildRequires: openmpi-devel

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

%build
#cmake -G "Unix Makefiles" .
cmake . -DCMAKE_INSTALL_PREFIX=/opt -DCMAKE_BUILD_TYPE=release -DMPI_C_COMPILER=/usr/lib64/openmpi/bin/mpicc -DMPI_CXX_COMPILER=/usr/lib64/openmpi/bin/mpicxx -DMPI_C_INCLUDE_PATH=/usr/include/openmpi-x86_64/
make

%install
install -d %{buildroot}%{_bindir}
%make_install
mkdir -p %{buildroot}/opt
mv %{buildroot}/root/Nelson-%{version} %{buildroot}/opt/Nelson
cd %{buildroot}/opt/Nelson/bin/linux64
for i in %{name}-*; do
  ln -s /opt/Nelson/bin/linux64/$i %{buildroot}%{_bindir}/$i
done

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE COPYING* *.md
/opt/Nelson
%{_bindir}/%{name}-*

%changelog
* Sun Sep 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.9
- Rebuilt for Fedora
