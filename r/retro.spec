%undefine _debugsource_packages

Summary: A language with roots in Forth
Name: retro
Version: 12.2021.2
Release: 1
License: Freeware
Group: Development/Language
URL: http://www.forthworks.com/retro
Source0: http://www.forthworks.com/retro/r/RETRO12-2021.2.tar.gz

%description
Retro is a concatenative, stack based language with roots in Forth. It is
designed to be small, easily learned, and easily modified to meet specific
needs, it has been developed and refined through continual use by a small
community over the last decade.

%prep
%setup -q -n RETRO12-2021.2

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
%make_install PREFIX=/usr MANDIR=%{buildroot}%{_mandir}/man1 EXAMPLESDIR=%{_datadir}/RETRO12

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%{_docdir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/RETRO12

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 12.2021.2
- Rebuilt for Fedora
