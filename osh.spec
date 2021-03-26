%global debug_package %{nil}

Name: osh
Summary: Two ports of V6 Thompson Shell
Version: 20130331
Release: 6.1
Group: System Environment/Shells
License: various opensource
URL: http://v6shell.org/
Source0: http://v6shell.org/src/%{name}-%{version}.tar.gz

%description
Osh is an enhanced, backward-compatible port of the Sixth Edition Thompson
shell. Sh6 is an unenhanced port of the shell, and glob6(1) is a port of its
global command. Together, sh6 and glob6 provide a user interface which is
backward compatible with that provided by the Sixth Edition Thompson shell
and global command, but without the obvious enhancements found in osh.

%prep
%setup -q

%build
make

%install
make install PREFIX=/usr DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/goto %{buildroot}%{_bindir}/goto6
mv %{buildroot}%{_mandir}/man1/goto.1 %{buildroot}%{_mandir}/man1/goto6.1
mv %{buildroot}%{_bindir}/if %{buildroot}%{_bindir}/if6
mv %{buildroot}%{_mandir}/man1/if.1 %{buildroot}%{_mandir}/man1/if6.1

%files
%doc README NOTES LICENSE AUTHORS CHANGES CHANGES6 DEDICATIONS
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 20130331
- Rebuild for Fedora
