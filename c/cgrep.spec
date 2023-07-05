%undefine _debugsource_packages

Summary:	cgrep
Name:		cgrep
Version:	8.15
Release:	5
License:	Lucent Public License
Group:		Productivity/Text/Utilities
Source0:	%{name}-%{version}.tar.gz
URL:		https://www.bell-labs.com/project/wwexptools/cgrep/

%description
cgrep provides all the features of grep, egrep, and fgrep, with greatly
enhanced performance (see the section on PERFORMANCE in the man page) along
with many additional features, two of which are the ability to output
the context (surrounding lines) of the matching lines and approximate
matching.

%prep
%setup -q

%build
CFLAGS=-O2 ./configure \
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --datadir=%{_datadir} \
  --libdir=%{_libdir} \
  --sysconfdir=%{_sysconfdir} \
  --enable-docdir=%{_defaultdocdir}
make 

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_docdir}/*
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 8.15
- Rebuilt for Fedora
* Fri Jun 24 2005 Lucent Central Exptools Administrator <exptools@lucent.com>
- Initial package
