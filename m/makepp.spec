Name:         makepp
Summary:      Make Plus Plus
URL:          http://makepp.sourceforge.net/
Vendor:       G. Holt, A. Johnson, D. Peiffer
Group:        Building
License:      GPL/Artistic
Version:      2.0
#Version:      2.0.99.2
Release:      7.1
Source0:      http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-%{version}.tgz
BuildRequires:  perl
BuildRequires:  perl-podlators
BuildArch:    noarch

%description
Makepp is a drop-in replacement for GNU make which has a number
of features that allow for more reliable builds and simpler build
files. It supports almost all of the syntax that GNU make supports,
and can be used with makefiles produced by utilities such as
automake. It is called makepp (or make++) because it was designed
for building C++ programs. Also its relationship to make is supposed
to be analogous to C++'s relationship to C: it is almost 100%
backward compatible but adds a number of new features.

%prep
%setup -q
sed -i 's|package Mpp::File;|package Mpp::FileOpt;|' Mpp/FileOpt.pm
sed -i '1i package Mpp::Utils;' Mpp/Utils.pm
sed -i 's|/usr/local|/usr|' install.pl
sed -i '29i use lib q[.];' install.pl

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
perl install.pl /usr/bin /usr/share/makepp /usr/share/man /usr/share/makepp/html none $RPM_BUILD_ROOT/usr

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue May 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Sat Feb 07 2009 OpenPKG Foundation e.V.
- Initial package
