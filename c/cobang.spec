%global realname CoBang

Name:           cobang
Version:        0.9.8
Release:        1
Summary:        A missing native QR Code scanner application for Linux desktop
License:        GPLv3+
URL:            https://github.com/hongquan/CoBang
Source0:        https://github.com/hongquan/CoBang/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  meson
BuildRequires:  python3-rpm-macros
BuildRequires:  %{py3_dist setuptools}
Requires:  python3-gstreamer1
Requires:  python3-gobject
Requires:  gtk3
Requires:  %{py3_dist logbook }
Requires:  %{py3_dist single-version }

%description
CoBang can scan from webcam or static image, local or remote.
In the future, it will support generating QR code and running on Linux phones.

%prep
%setup -q -n %{realname}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py3_build_egg

%install
%py3_install

%files
%license LICENSE.txt
%doc README.rst
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/*.py
%{python3_sitelib}/%{name}/__pycache__/*.pyc
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.8
- Rebuilt for Fedora
* Mon Sep 14 2020 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 0.5.6-1
- Initial package.
