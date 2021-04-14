Name:         bbe
Summary:      Binary Block Editor
URL:          http://sourceforge.net/projects/bbe-/
Group:        ShellUtils
License:      GPL
Version:      0.2.2
Release:      20080102.1
Source0:      http://switch.dl.sourceforge.net/bbe-/bbe-%{version}.tar.gz

%description
bbe is an sed(1) like editor for binary files. bbe performs basic
byte operations on blocks of input stream.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/%{name}
%exclude %{_datadir}/doc/bbe/bbe.html
%{_datadir}/info/bbe.info.*
%exclude %{_datadir}/info/dir
%{_mandir}/man1/bbe.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
