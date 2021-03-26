%global debug_package %{nil}

Name:    e6irc
Version: 0.6.7
Release: 8.4
Summary: IRC from Egalite
License: GPLv2
Group:   Applications/Network
URL:     http://e6irc.sourceforge.net/
Source: %{name}_%{version}.tar.gz
BuildRequires: libpng-devel
BuildRequires: pkgconfig(QtNetwork) >= 4.7
BuildRequires: pkgconfig(QtDeclarative) >= 4.7
BuildRequires: qt-mobility-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++

%description
IRC Chat with colleagues, friends and enemies.

%prep
%setup -q

%build
cp %{name}-linux.pro %{name}-linux.pro.save
rm -f *.pro
mv %{name}-linux.pro.save %{name}.pro
qmake-qt4
make

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%doc COPYRIGHT
%doc LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.7
- Rebuild for Fedora
* Mon Sep  5 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.6.4 
- fix bug in window size change detection
* Thu Sep  1 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.6.3 
- support multi-channel join: JOIN #chan1 #chan2 #chan3
* Tue Aug 30 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.6.2 
- deal with pop-up virtual keybboard a bit
  - suppress initial caps where not appropriate
  - functions to delete servers, channels, nicks
  - better editing of new user/server/channel; packing issues;
* Sun Aug 28 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.6.1 
- count objects
  - suppress initial caps where not appropriate
  - functions to delete servers, channels, nicks
  - better editing of new user/server/channel; packing issues;
  - add channels; servers and nicks to database
  - use geuzen text browser; some costmetics;
  - mark things as being gpl2, hopefully in all neccessary places
* Wed Aug 24 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.6.0 
- convert egalite code to stand-alone IRC client
- make more suitable for phone-size displays
