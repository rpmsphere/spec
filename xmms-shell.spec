Summary:	XMMS-Shell is a simple utility for controlling XMMS externally
Name:		xmms-shell
Version:	0.99.3
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/xmms-shell/%{name}-%{version}.tar.gz
URL:		http://www.loganh.com/xmms-shell/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRequires:	xmms-devel
Requires:	xmms

%description
XMMS-Shell is a simple utility for controlling XMMS externally.
Although XMMS itself provides some similar functionality, XMMS lacks a
few important command line options to allow one to perform certain
tasks, such as volume control, easily manipulating a playlist, and
more. XMMS-Shell is intended to make up for these deficiencies.

%prep
%setup -q
sed -r -i '7i #include <cstdlib>\n#include <cstring>' include/command.h

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/xmms-shell
%{_mandir}/man1/xmms-shell.1*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.99.3
- Rebuild for Fedora
* Wed Nov 26 2008 Feather Mountain <john@ossii.com.tw>
- Build for M6(OSSII)
