%define _name MikuMikuDance

Summary: Multi 3D Miku Model
Name: mmd-data
Version: 5.24
Release: 3.1
License: freeware
Group: User Interface/Desktops
Source0: https://www.geocities.jp/higuchuu4/pict/%{_name}E_v524.zip
URL: https://www.geocities.jp/higuchuu4/index_e.htm
BuildArch: noarch

%description
Miku Hatune is a Japanese female vocalist of VOCALOID2 and has been on sale
from Crypton Future Media, Inc.

%prep
%setup -q -n %{_name}E_v524
rm MikuMikuDance.exe Data/MMDxShow.dll Data/Thumbs.db Data/win2000.bat

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/%{_name}

%changelog
* Mon May 23 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 5.24
- Rebuilt for Fedora
