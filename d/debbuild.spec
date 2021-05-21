Summary: Build .deb packages from RPM .spec files
Name: debbuild
Version: 0.9.9
Release: 3.1
Source: http://www.deepnet.cx/debbuild/debbuild-%{version}.tar.gz
Group: Development/Tools
License: GPLv2
Requires: perl, make, gcc, pax, fakeroot, debhelper
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
debbuild attempts to build Debian-friendly semi-native packages from
RPM spec files, RPM-friendly tarballs, and RPM source packages
(.src.rpm files).  It accepts most of the options rpmbuild does, and
should be able to interpret most spec files usefully.  Perl modules
should be handled via CPAN+dh-make-perl instead as it's simpler
than even tweaking a .spec template.

Note that patch is not strictly required unless you have .spec files
with %patch directives, and RPM is not required unless you wish to
rebuild .src.rpm source packages as .deb binary packages.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/*
%{_mandir}/man8/*

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9
- Rebuilt for Fedora
* Thu Feb 28 2008  Kris Deugau <kdeugau@deepnet.cx> -1
- Initial package
