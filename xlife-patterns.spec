Name: xlife-patterns
Summary: All patterns for XLife
Version: 6.7.6
Release: 1
Group: Amusements/Games
License: GPL
URL: http://litwr2.atspace.eu/xlife.php
Source0: %{name}.tar.xz
BuildArch: noarch

%description
All patterns in one archive (8.3M).

%prep
%setup -q -n patterns 

%build

%install
install -d %{buildroot}%{_datadir}/xlife
cp -a * %{buildroot}%{_datadir}/xlife

%files
%{_datadir}/xlife

%changelog
* Fri Sep 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 6.7.6
- Rebuild for Fedora
