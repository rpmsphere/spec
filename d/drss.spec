%undefine _debugsource_packages

Name:    drss
Version: 0.3.5
Release: 14.1
Summary: RSS/Atom reader
License: GPLv3
Group:   Applications/Productivity
URL:     https://drss.sourceforge.net/
Source: %{name}-%{version}.tar.gz
Source2: %{name}.desktop
BuildRequires:  libpng-devel
BuildRequires:  qt4-devel qt4-webkit-devel
BuildRequires:  gcc-c++ gdb
BuildRequires:  desktop-file-utils

%description
An application to read RSS and Atom feeds.

%prep
%setup -q

%build
sh configure
make 

%install
rm -rf $RPM_BUILD_ROOT
install -p -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -p -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 755 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYRIGHT LICENSE.txt helpman.html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.5
- Rebuilt for Fedora
* Wed Aug 25 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.3.5-1
- change layouts
- remove clock code
- fix mailto bug
* Wed Aug 25 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.3.4-1
- desktop file
- PS3 build
* Wed Mar 27 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.3.1-1
- Initial RPM release
