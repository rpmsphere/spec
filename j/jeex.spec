%undefine _debugsource_packages

Name: jeex
Summary: Visual editor to view and edit files in hexadecimal
Version: 12.0.4
Release: 8.1
Group: Applications/Editors
License: GPL
URL: http://www.hds619.net/Jeex.php
Source0: http://www.hds619.net/data/jeex/jeex-pkg/%{name}-%{version}.tar.bz2
BuildRequires: file-devel
BuildRequires: gtk2-devel

%description
Jeex is a simple hexadecimal editor which allows user to create, open
and edit files in hexadecimal, binary, octal and ASCII. The features include
insert, delete, copy-and-paste, search and many others.
It also shows several information about the opened file, like file mode bits,
ownership, last access and modification timestamps.

%prep
%setup -q
sed -i 's|-pipe|-pipe -Wl,--allow-multiple-definition|' Makefile

%build
make %{?_smp_mflags}

%install
make install destdir=%{buildroot}
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps

%files
%doc ChangeLog README COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_sysconfdir}/%{name}

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 12.0.4
- Rebuilt for Fedora
