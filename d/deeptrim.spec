%undefine _debugsource_packages

Name:    deeptrim
Version: 0.0.9
Release: 19.1
Summary: Text editor
License: GPLv2
Group:   Applications/Productivity
URL:     https://%{name}.sourceforge.net/
Source0: %{name}_%{version}.tar.gz
Source2: %{name}.desktop
BuildRequires: libpng-devel
BuildRequires: pkgconfig(QtGui) >= 4.6
BuildRequires: pkgconfig(QtWebKit) >= 4.6
BuildRequires: qscintilla-devel
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils

%description
A text editor using QScintilla.

%prep
%setup -q
sed -i 's|hiddenBox (false),|hiddenBox (0),|' src/permute.cpp

%build
./configure
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
%doc README COPYRIGHT LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.9
- Rebuilt for Fedora
* Wed May  4 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.9-1
- filter out middle-button mouse clicks, so they do not paste in editor
* Tue Mar 29 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.8-1
- update packaging
* Mon Dec  6 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.7-1
- even more improved shortcuts
* Sun Dec  5 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.5-1
- correct line number to display 1-based
- handle ambiguous shortcut keys better
* Thu Dec  2 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.5-1
- add files from command line to already running instance
- cosmetic stuff
* Wed Nov  3 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.4-1
- jump to line
- misc cosmetic details
* Sun Oct 31 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.3-1
- file load/save/refresh
- search/replace
- various window management issues
- docking window issues
- font configuration for file types
- lexers for file types
* Thu Oct 28 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.1-1
- Initial RPM build
