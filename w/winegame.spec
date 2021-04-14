Name:           winegame
Version:        0.2.0
Release:        5.1
Summary:        A simple front-end to Wine
License:        GPL-3.0+
Group:          System/Emulators/PC
URL:            http://code.google.com/p/winegame/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  winestuff-devel
Requires:       wine-core

%description
WineGame is a simple front-end to Wine, provides an easy
interface to install some game from DVD.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc CHANGELOG LICENSE TODO VERSION
%{_bindir}/winegame
%{_datadir}/winegame
%{_datadir}/pixmaps/winegame.png
%{_datadir}/applications/winegame.desktop

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Fri Mar 23 2012 jengelh@medozas.de
- Strip redundant sections/tags
- SPDX license field
* Tue Aug 31 2010 yar@sibnet.ru
- update to 0.2.0
* Sun Aug 22 2010 yar@sibnet.ru
- update to 0.1.92
* Mon Jul 19 2010 yar@sibnet.ru
- update to 0.1.91
* Mon Jun 28 2010 prusnak@opensuse.org
- spec cleanup
* Wed Jun 16 2010 yar@sibnet.ru
- initial packaging
