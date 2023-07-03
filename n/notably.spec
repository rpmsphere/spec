%undefine _debugsource_packages

Name:    notably
Version: 0.3.4
Release: 31.1
Summary: Note taking application
License: GPLv3
Group:   Applications/Productivity
URL:     https://notably.sourceforge.net/
Source: %{name}-%{version}.tar.gz
Source2: %{name}.desktop
BuildRequires: libpng-devel
BuildRequires: pkgconfig(QtNetwork) >= 4.6
BuildRequires: pkgconfig(QtWebKit) >= 4.6
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++

%description
Notably is a note taking and organizing application. It is designed to 
allow quick entry of notes, and organization of these notes. To organize notes,
they can be groups into books. Notes can be tagged to make them 
easier to find.

%prep
%setup -q

%build
./configure
make 

%install
rm -rf $RPM_BUILD_ROOT
install -p -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 bin/notably $RPM_BUILD_ROOT%{_bindir}
install -p -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 755 notably.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%doc LICENSE.txt
%doc qrcfiles/userman.html
%{_bindir}/notably
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4
- Rebuilt for Fedora
* Sun Aug 1 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.3.4-2 
- packaging update
* Fri Mar 26 2010 Bernd Stramm <bernd.stramm@gmail.com>
- fixed save-first-note bug
- build/install/packaging changes
* Wed Mar 24 2010 Bernd Stramm <bernd.stramm@gmail.com> 
- Initial RPM release
