%undefine _debugsource_packages

Summary: A language with roots in Forth
Name: retro12
Version: 2024.1
Release: 1
License: Freeware
Group: Development/Language
URL: https://www.forthworks.com/retro
Source0: https://www.forthworks.com/retro/r/RETRO12-%{version}.tar.gz

%description
Retro is a concatenative, stack based language with roots in Forth. It is
designed to be small, easily learned, and easily modified to meet specific
needs, it has been developed and refined through continual use by a small
community over the last decade.

%prep
%setup -q -n RETRO12-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
%make_install PREFIX=/usr MANDIR=%{_mandir}/man1 EXAMPLESDIR=%{_datadir}/RETRO12

%files
%{_docdir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/RETRO12

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2024.1
- Rebuilt for Fedora
