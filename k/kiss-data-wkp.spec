Summary: KiSS data from WKP
Name: kiss-data-wkp
Version: 2011
Release: 6.1
License: freeware
Group: Amusements/Games
URL: https://www.kiss-wkp.com/
Source: %{name}.zip
Requires: lha
BuildArch: noarch

%description
This package contains the data files from World Kiss Project
required to run any of the KiSS paper dolls game.

%prep
%setup -q -n %{name}

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/kiss
%{__cp} * %{buildroot}%{_datadir}/kiss

%clean
%{__rm} -rf %{buildroot}

%files
%{_datadir}/kiss/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2011
- Rebuilt for Fedora
