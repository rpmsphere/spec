%undefine _debugsource_packages

Name: etsh
Summary: V6 Thompson Shell Ports
Version: 5.4.0
Release: 1
Group: System Environment/Shells
License: various opensource
URL: https://etsh.nl/
Source0: https://etsh.nl/src/%{name}_%{version}/%{name}-%{version}.tar.gz

%description
Osh is an enhanced, backward-compatible port of the Sixth Edition Thompson
shell. Sh6 is an unenhanced port of the shell, and glob6(1) is a port of its
global command. Together, sh6 and glob6 provide a user interface which is
backward compatible with that provided by the Sixth Edition Thompson shell
and global command, but without the obvious enhancements found in osh.

%prep
%setup -q

%build
./configure
make

%install
make install PREFIX=/usr DESTDIR=%{buildroot}
mv %{buildroot}%{_libexecdir}/%{name}-%{version} %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_datadir}
mv %{buildroot}/usr/man %{buildroot}%{_mandir}

%files
%doc README NOTES LICENSE AUTHORS CHANGES DEDICATIONS
%{_bindir}/*
%{_libexecdir}/%{name}
%{_mandir}/man1/*

%changelog
* Sun May 8 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 5.4.0
- Rebuilt for Fedora
