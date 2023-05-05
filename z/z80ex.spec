%undefine _debugsource_packages

Name:           z80ex
Version:        1.1.21
Release:        1
Summary:        A Z80 CPU emulator library
License:        GPLv2
URL:            https://sourceforge.net/projects/z80ex/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
A Z80 CPU emulator library:
- precise opcode emulation (documented & undocumented)
- exact timings for each opcode (including I/O operations)
- full support for all interrupt modes
- any number of virtual CPUs may be created
- portable: written in pure ANSI C
- builds as a library with simple callback-based API
- disassembler included

%package devel
Summary: Development files for z80ex
Requires: z80ex = %{version}-%{release}

%description devel
Development files for z80ex, a Z80 CPU emulator library.

%prep
%setup -q

%build
mkdir build
pushd build
%cmake ..
%cmake_build
popd

%install
rm -rf %{build_root}
pushd build
%cmake_install
popd
# Erase static libs
rm -f %{buildroot}%{_libdir}/*.a

# It's no longer required to run ldconfig when installing shared libs on Fedora                     
%files
%license COPYING
%doc Changelog README TODO
# Fedora packaging guidelines advise against globbing for libraries due to
# potential SONAME bumps going unnoticed
%{_libdir}/lib%{name}.so.1.1.21
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}_dasm.so.1.1.21
%{_libdir}/lib%{name}_dasm.so.1

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_dasm.so

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.21
- Rebuilt for Fedora
* Sat Dec 26 2020 RPMBuilder <rpmbuilder@example.com> - 1.1.21-1
- Initial RPM
