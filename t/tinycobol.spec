%undefine _debugsource_packages

Name:		tinycobol
Version:	0.66
Release:	17.1
Summary:	TinyCobol compiler and runtime
Group:		Development/Languages/Other
License:	GPL and LGPL
URL:		http://tiny-cobol.sourceforge.net/
Source:	http://sourceforge.net/projects/tiny-cobol/files/tiny-cobol/0.66/%{name}-%{version}.tar.bz2
BuildRequires:	libtool
BuildRequires:  libdb-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  readline-devel
BuildRequires:  vbisam-devel
Requires:	gcc
Requires:	ncurses
Requires:	vbisam

%description
TinyCOBOL is a COBOL compiler based on the COBOL 85 standards. You can
build your COBOL programs on various platforms, including Unix/Linux,
FreeBSD and Microsoft Windows.

%prep
%setup -q
sed -i 's|db46|libdb|' configure

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
sed -i 's|^INCLUDES=|INCLUDES= -fPIC |' `find . -name Makefile`
make

%install
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}/man1 tcob_docdir=%{_docdir}/htcobol-%{version} lib_dir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/htcobol
%{_bindir}/htcobrun
%{_libdir}/libhtcobol.*
%{_datadir}/htcobol
%{_datadir}/doc/htcobol-%{version}
%{_datadir}/man/man1/*.1.*

%changelog
* Sun Dec 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.66
- Rebuilt for Fedora
* Thu Aug 31 2010 - Sebastian Ritter - 1.1-0.2010-08-29
- OpenSuSE 11.3 with debian compatible package format and standard groups
