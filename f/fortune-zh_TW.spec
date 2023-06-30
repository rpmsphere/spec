Summary: Fortune from traditional chinese
Name: fortune-zh_TW
Version: 1.3
Release: 1
URL: https://www.freshports.org/chinese/fortunetw
License: BSD
Group: Amusements/Games
Source0: fortune-zh_TW.tar.gz
BuildArch: noarch
BuildRequires: fortune-mod
Requires: fortune-mod

%description
fortune-zh_TW contains very classic fortune files, modified
from zh-fortunetw-1.3.tar.gz by statue@freebsd.sinica.edu.tw

%prep
%setup -q -n %{name}

%build
for i in * ; do strfile $i ; done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/games/fortune
cp * $RPM_BUILD_ROOT%{_datadir}/games/fortune

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/games/fortune/*

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
