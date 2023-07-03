%undefine _debugsource_packages

Name:           slowcat
License:        GPL
Group:          Productivity/Text/Convertors
Version:        1.0.1
Release:        7.1
Summary:        Slow Cat
URL:            https://grox.net/software/mine/slowcat/slowcat.c
Source:         %{name}-%{version}.tar.bz2

%description
Cat files slowly.

Authors:
--------
    dave w capella
    brian@landsberger.com
    Brian K. White <brian@aljex.com>

%prep
%setup -q

%build
CFLAGS="%{optflags}" make

%install
PREFIX=%{buildroot}/usr MANDIR=%{buildroot}/%{_mandir} make install

%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Nov 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuilt for Fedora
* Fri Feb 18 2011 - brian@aljex.com
- Version 1.0.1
* Fri Feb 18 2011 - brian@aljex.com
- Version 1.0.0 for SuSE for Aljex Software
