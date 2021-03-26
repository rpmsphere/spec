%define gitdate 20131014
%define gitname ProjectTox-Core

Name:           tox
Version:        0.0.0.%{gitdate}
Release:        3.1
Summary:        Secure decentralized instant messaging application
License:        GPL-3.0
Group:          Productivity/Networking/Instant Messenger
URL:            http://tox.im/
Source0:        %{gitname}-master.zip
BuildRequires:  cmake, gcc-c++, libconfig-devel, libsodium-devel, ncurses-devel      

%description
Project Tox, also known as Tox, is a FOSS instant messaging 
application aimed to replace Skype.
With the rise of governmental monitoring programs, 
Tox aims to be an easy to use application that allows 
people to connect with friends and loved ones without 
the worry of privacy.
See also http://tox.someguy123.com/

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q -n %{gitname}-master

%build
autoreconf -if
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc COPYING README.md
%{_bindir}/*
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.0.20131014
- Rebuild for Fedora
* Sat Aug  3 2013 novell@tower-net.de
- Update to ProjectTox-Core-aa78644aed020198f85c97fe63bea7fc88e4a8dc
* Fri Aug  2 2013 novell@tower-net.de
- Modified CMakeLists_curses_ncurses_link_typo.patch
* Fri Aug  2 2013 novell@tower-net.de
- Updated to tox-7379392d80
* Wed Jul 31 2013 novell@tower-net.de
- CMakeLists_curses_ncurses_link_typo.patch fixes a typo to link with libncurses
* Tue Jul 30 2013 novell@tower-net.de
- New tox https://github.com/irungentoo/ProjectTox-Core/commit/b94d9d6765381e0a80f86a85edf45b1fd652a21a
