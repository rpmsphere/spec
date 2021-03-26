%global debug_package %{nil}
Name:           python-hashlib
Summary:        Python secure hash and message digest module
%define tarname hashlib
BuildRequires:  python-devel openssl-devel
Version:        20060408a
Release:	1
License:        GNU General Public License (GPL)
Group:          add-group-here
URL:            http://code.krypto.org/python/hashlib
Source:         http://code.krypto.org/python/hashlib/%{tarname}-%{version}.tar.gz

%description
Python secure hash and message digest module
MD5, SHA1, SHA224, SHA256, SHA384 and SHA512
(backported from Python 2.5 for use on 2.3 and 2.4)

%prep
%setup -n %{tarname}-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python2 setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog LICENSE LICENSE.openssl README.txt
%{python2_sitearch}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20060408a
- Rebuild for Fedora
* Mon Sep 10 2008 milochen <milo_chen@mail2000.com.tw>
- initial ossii package
* Tue Mar  4 2008 bwalle@suse.de
- initial SUSE package
