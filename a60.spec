Name:		a60
Summary:	Algol 60 Interpreter
Version:	0.23a
Release:	4.1
Source0:	https://github.com/Abderasoft/NASE-A60/archive/0.23a.tar.gz#/NASE-A60-%{version}.tar.gz
URL:		https://github.com/Abderasoft/NASE-A60
Group:		Development/Languages
License:	GPLv2

%description
This is the Algol 60 interpreter NASE A60 made for fun and call-by-name.
NASE A60 is based on the 'Revised Report on the Algorithmic Language Algol 60'.
The I/O section of the interpreter is not complete at all, but basic
things are now working.

%prep
%setup -q -n NASE-A60-%{version}

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir} %{buildroot}%{_mandir}/man1
make install BINDIR=%{buildroot}%{_bindir} LIBDIR=%{buildroot}%{_libdir} MANDIR=%{buildroot}%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%doc TODO ChangeLog COPYING README RRA60*
%{_libdir}/%{name}*
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}

%changelog
* Thu Oct 18 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.23a
- Rebuild for Fedora
