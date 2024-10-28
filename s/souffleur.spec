%undefine _debugsource_packages

Name:    souffleur
Version: 0.1.8
Release: 9.4
Summary: Schedule events and remind the user of stuff to be done
License: GPLv2
Group:   Applications/Productivity
URL:     https://souffleur.sourceforge.net/
Source: %{name}_%{version}.tar.gz
BuildRequires: libpng-devel
BuildRequires: pkgconfig(QtGui) >= 4.7.2
BuildRequires: pkgconfig(QtWebKit) >= 4.7.2
BuildRequires: pkgconfig(QtDeclarative)
BuildRequires: pkgconfig(QtOpenGL)
BuildRequires: qt-mobility-devel
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils

%description
An application for planning scheduled events and receiving reminders about
such events.

%prep
%setup -q

%build
sh configure
make 

%install
rm -rf $RPM_BUILD_ROOT
install -p -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 bin/souffleur $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 bin/souffleur-background-picker $RPM_BUILD_ROOT%{_bindir}
install -p -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 755 souffleur.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  \
         linux/souffleur.desktop

%files
%doc README
%doc COPYRIGHT
%doc LICENSE.txt
%{_bindir}/souffleur
%{_bindir}/souffleur-background-picker
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.8
- Rebuilt for Fedora
