%global srcname openastro.org-data

Name:           openastro-data
Version:        1.9
Release:        4
Summary:        Astrology data
License:        GPLv3+
URL:            http://www.openastro.org
Source0:        http://www.openastro.org/download.php?file=source&type=data#/%{srcname}_%{version}.orig.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Data for the open source astrology program.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license COPYING
%{python3_sitelib}/*
%{_datadir}/openastro.org
%{_datadir}/swisseph

%changelog
* Mon Sep 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9
- Rebuilt for Fedora
* Thu Feb 11 2016 Jens Petersen <petersen@redhat.com>
- Initial package
