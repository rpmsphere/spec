Summary: KiSS data from OtakuWorld
Name: kiss-data-otakuworld
Version: 2016
Release: 2.1
License: freeware
Group: Amusements/Games
URL: http://otakuworld.com/index.html?/kiss/0kiss.html
Source: %{name}.zip
Requires: lha
BuildArch: noarch

%description
This package contains the data files from Otaku World
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
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2016
- Rebuild for Fedora
