%undefine _debugsource_packages

Summary:	An easy editor
Name:		ee
Version:	1.5.2
Release:	4.1
License:	Artistic
Group:		Editors
URL:		http://mahon.cwx.net/
Source0:	http://mahon.cwx.net/sources/%{name}-%{version}.src.tgz

%description
An easy to use text editor. Intended to be usable with little or no instruction.
Provides a terminal (curses based) interface. Features pop-up menus.
A subset of aee.

%prep
%setup -q -n easyedit-%{version}
sed -i '1i #define SIGUNUSED 31' ee.c
sed -i 's|-s|-Wl,--allow-multiple-definition|' *.make

%build
make OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m644 %{name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.ee ee.i18n.guide Changes
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Mar 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.2
- Rebuilt for Fedora
