%global debug_package %{nil}
Name:           python-yowsup
Version:        2.3.124
Release:        4.1
Summary:        Open Whatsapp service under platforms
License:        GPLv3
Group:          Development/Libraries/Python
URL:            https://github.com/tgalal/yowsup
Source0:        yowsup-%{version}.tar.gz
BuildRequires: python2-devel
BuildRequires: python2-setuptools
Requires:	python-dateutil
Requires:	python-pillow
BuildArch: noarch

%description
Yowsup is a python library that allows you to login and use the Whatsapp
service and provides you with all capabilities of an official Whatsapp
client, allowing you to create a full-fledged custom Whatsapp client.

%prep
%setup -q -n yowsup-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=/usr

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%doc LICENSE README.md
%{_bindir}/yowsup-cli
%{python2_sitelib}/*

%changelog
* Tue Jul 14 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.124
- Rebuild for Fedora
