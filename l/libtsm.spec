Summary: Terminal-emulator State Machine
Name: libtsm
Version: 4.0.2
Release: 1
License: GPL
URL: https://github.com/Aetf/libtsm
Group: Applications
Source0: https://github.com/Aetf/libtsm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: cmake

%description
TSM is a state machine for DEC VT100-VT520 compatible terminal emulators.
It tries to support all common standards while keeping compatibility to
existing emulators like xterm, gnome-terminal, konsole, ...

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%files
%doc COPYING LICENSE_htable NEWS README README.md
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/%{name}
%{_includedir}/*.h

%changelog
* Thu Apr 10 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.2
- Rebuilt for Fedora
