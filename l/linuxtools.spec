Summary: Linux Tools
Name: linuxtools
Version: 0.0
Release: 1
License: Free Software
Group: Applications
URL: https://fex.belwue.de/sw/share/linuxtools-0.0/
Source0: linuxtools-%{version}.tar.gz
BuildArch: noarch

%description
linuxtools is a software distribution for UNIX systems developed 1993 at RUS
(Rechenzentrum Universitaet Stuttgart, now TIK)

%prep
%setup -q

%build
#No build

%install
install -d %{buildroot}/usr
cp -a bin sbin %{buildroot}/usr

%files
%doc doc/html/*
%{_bindir}/*
%{_sbindir}/*

%changelog
* Fri Feb 24 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0
- Initial package for Fedora
