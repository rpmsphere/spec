%global theme_name    Sato

Name:           sato-matchbox-theme
Version:        0.2
Release:        2.1
Summary:        Sato Theme for Matchbox
Group:          User Interface/Desktops
License:        GPLv3
URL:            https://github.com/jku/matchbox-sato
Source0:        https://codeload.github.com/jku/matchbox-sato/tar.gz/0.2#/matchbox-sato-0.2.tar.gz
BuildArch:      noarch      

%description
Sato Theme for Matchbox Window Manager.

%prep
%setup -q -n matchbox-sato-%{version}

%build
autoreconf -ifv
./configure --prefix=/usr --enable-matchbox-1 --enable-matchbox-2
make

%install
%make_install

%files
%doc TODO COPYING ChangeLog
%{_datadir}/themes/%{theme_name}/matchbox*

%changelog
* Fri Aug 17 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
