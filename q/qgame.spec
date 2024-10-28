%global __spec_install_post %{nil}
%undefine _debugsource_packages

Name:           qgame
Version:        0.4.1
Release:        1
Summary:        Quantum Gate And Measurement Emulator
Group:          Amusements/Games
License:        LGPL
URL:            https://hampshire.edu/lspector/qgame.html
Source0:        https://hampshire.edu/lspector/qgame++/%{name}-%{version}.tar.gz
Patch0:         qgame-qgtypes.cpp-patch
Patch1:         qgame-client.cpp-patch

%description
QGAME (Quantum Gate And Measurement Emulator) is a system, that allows a user
to run quantum computing algorithms on an ordinary digital computer.
Because quantum computers have complexity advantages over classical computers,
any classical emulator will necessarily be less efficient than the quantum
computer that it is emulating. QGAME nonetheless allows the user to find out
what outputs the quantum program would produce, and with what probabilities
(since quantum computation is in general not deterministic).

%prep
%setup -q
%patch 0 -p0
%patch 1 -p0

%build
%configure
sed -i 's|-Wall|-Wall -std=gnu++14|' Makefile */Makefile
make 

%install
%__rm -rf %{buildroot}
DESTDIR=$RPM_BUILD_ROOT make install

%files
%{_bindir}/*
%{_includedir}/*
%{_libdir}/lib*
%{_mandir}/man1/qgame.1*

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
* Fri Sep 12 2008 Feather Mountain <john@ossii.com.tw> 0.4.1-1
- Build for OSSII
