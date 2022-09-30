%undefine _debugsource_packages

Name: clcc
Version: 0.3.0
Release: 44.1
Source0: http://sourceforge.net/projects/clcc/files/v%{version}/%{name}-%{version}-25-src.zip
License: Boost Software License 1.0
Group: Development/Tools
URL: http://clcc.sourceforge.net/
Summary: The OpenCL kernel Compiler
BuildRequires: gcc-c++, cmake, boost-devel, subversion, doxygen
BuildRequires: ocl-icd-devel, mesa-libOpenCL-devel, llvm-devel

%description
CLCC is a compiler for OpenCL kernel source files. It is intended to be a tool
for application developers who need to incorporate OpenCL source code into
their programs and who want to verify their OpenCL code actually gets compiled
by the driver before their program tries to compile it on-demand.

%prep
%setup -q -c
sed -i '22,27d' CMakeLists.txt
sed -i '14d' src/CMakeLists.txt
sed -i 's|__LINUX__|__linux__|' src/options.cpp

%build
export LDFLAGS="-lboost_system -lboost_program_options"
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make clcc clcc_doc

%install
rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc
mv $RPM_BUILD_ROOT/usr/doc/html $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/doc/%{name}-%{version}

%changelog
* Sun Dec 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
