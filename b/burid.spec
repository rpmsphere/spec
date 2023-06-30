%undefine _debugsource_packages

Name:    burid
Version: 0.0.8
Release: 5.1
Summary: E-Book Reader
License: GPLv2
Group:   Applications/Office
URL:     https://carpo.sourceforge.net/
Source: %{name}-%{version}.tar.gz
Source2: %{name}.desktop
BuildRequires: libpng-devel
BuildRequires: pkgconfig(QtNetwork)
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: pkgconfig(QtDeclarative)
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++ automake
Requires: unzip

%description
E-Book Reader.

%prep
%setup -q
sed -i 's|poppler-qt4|poppler-qt5|' burid.pro
sed -i 's|poppler/qt4/poppler-qt4.h|poppler/qt5/poppler-qt5.h|' src/pdf-pager.h

%build
./configure --prefix=/usr
make 

%install
rm -rf $RPM_BUILD_ROOT
install -p -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 bin/%{name} $RPM_BUILD_ROOT%{_bindir}
install -p -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 755 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE2}

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
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.8
- Rebuilt for Fedora
* Wed Jul  6 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.8-2
- remove Behaviour to fix rendering artifacts
* Thu Jun  2 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.7-1
- fix recent book memory to use full path name
- cosmetic changes to UI
* Mon May 30 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.6-1
- remember recent books
* Sun May 29 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.5-1
- delete bookmarks
* Sat May 28 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.4-1
- fix pdf crash
- elementary normal pdf version to select file
- get DPI from system for pdf
- show relative position in epub book
- take file names from command line (for xdg-open support)
* Fri May 27 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.3-1
- epub bookmarks working, save and jump back
* Thu May 26 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.2-1
- some epub stuff sort of works
* Mon May 23 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.1-1
- start work
