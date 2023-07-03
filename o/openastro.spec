%global srcname openastro.org

Name:           openastro
Version:        1.1.57
Release:        5
Summary:        Astrology charts
License:        GPLv3+
URL:            https://www.openastro.org/
Source0:        https://www.openastro.org/download.php?file=source&type=openastro#/%{srcname}_%{version}.orig.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
#Requires:       gnome-python2-rsvg
Requires:       openastro-data
Requires:       python3-pytz
Requires:       python3-swisseph

%description
The open source astrology program openastro.org.

%prep
%autosetup -n %{srcname}-%{version}
sed -i 's|s\.decode|s.encode().decode|' %{name}

%build
%py3_build

%install
%py3_install
%find_lang openastro
install -Dm644 icons/openastro.svg %{buildroot}%{_datadir}/pixmaps/openastro.svg

%files 
%license COPYING
%{_bindir}/openastro
%{_datadir}/applications/openastro.desktop
%{_datadir}/openastro.org
%{python3_sitelib}/*
%{_datadir}/pixmaps/openastro.svg

%changelog
* Mon Sep 07 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.57
- Rebuilt for Fedora
* Thu Feb 11 2016 Jens Petersen <petersen@redhat.com>
- Initial package
