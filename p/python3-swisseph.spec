%global srcname pyswisseph

Name:           python3-swisseph
Version:        2.08.00
Release:        1
Summary:        Swiss Ephemeris astrology data
License:        GPLv2+
URL:            https://pypi.python.org/pypi/pyswisseph
Source0:        https://pypi.python.org/packages/source/p/pyswisseph/%{srcname}-%{version}-1.tar.gz
BuildRequires:  python3-devel

%description
Python extension to AstroDienst Swiss Ephemeris library.

%prep
%autosetup -n %{srcname}-%{version}-1

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt README.rst
%{python3_sitearch}/*

%changelog
* Mon Sep 07 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.08.00
- Rebuilt for Fedora
* Thu Feb 11 2016 Jens Petersen <petersen@redhat.com>
- Initial package
