%undefine _debugsource_packages

Name:		qwallchange
Summary:	A simple wallpaper changing program
Version:	0.1.3
Release:	5.1
URL:		http://suslic-2012.narod.ru/QWallChange.html
Source0:	qwallchange_0.1.3_src.tar.gz
Source1:	qwallchange.desktop
License:	BSD
Group:		Desktop/User Interface
BuildRequires:	qt-devel

%description
QWallChange is a simple wallpaper changing program for Gnome written on Qt for Linux.

Author: Koptsow Dmitriy <suslic-2012@rambler.ru>

%prep
%setup -q -n qwallchange-0.1.3.orig

%build
qmake-qt4
make

%install
install -D -m 755 bin/qwallchange $RPM_BUILD_ROOT%{_bindir}/qwallchange
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/qwallchange.desktop
install -D -m 644 images/main.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/qwallchange.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/qwallchange
%{_datadir}/applications/qwallchange.desktop
%{_datadir}/pixmaps/qwallchange.png
%doc ReadMe

%changelog
* Tue Jun 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.3
- Rebuilt for Fedora
