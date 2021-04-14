Name:      lgeneral-data
Summary:   Basic data files for the LGeneral strategy game
Version:   1.1
Release:   1
License:   GPL
Group:     Amusements/Games/Strategy/Turn Based
Source:    %{name}-%{version}.tar.gz
URL:       http://lgames.sourceforge.net/index.php?project=LGeneral
Requires:  lgeneral
BuildArch: noarch

%description
K.u.k General Data is a free stand-alone WWI scenario package by Steve McGuba.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/lgeneral
cp -a * %{buildroot}%{_datadir}/lgeneral

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/lgeneral/*

%changelog
* Fri Mar 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Thu Sep 30 2010 Frank Schaefer <schaeferf.obs@googlemail.com>
- Update to version 1.2
* Mon Nov 09 2009 Frank Schaefer <schaeferf.obs@googlemail.com>
- Update to 1.2beta.14
* Mon Mar 16 2009 Frank Schaefer <schaeferf.obs@googlemail.com>
- Initial openSUSE package release (1.2beta.13)
