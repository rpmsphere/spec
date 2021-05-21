Name:          dnspython
Version:       1.9.2
Release:       3.1
Summary:       A DNS toolkit for Python
Group:         System/Libraries
URL:           www.dnspython.org/
Source:        http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
License:       BSD
BuildRequires: python-devel
Requires:      python
BuildArch:     noarch

%description
dnspython supports almost all record types. It can be used for queries,
zone transfers, and dynamic updates. It supports TSIG authenticated messages
and EDNS0. dnspython provides both high and low level access to DNS.
The high level classes perform queries for data of a given name, type,
and class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records. 

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
   -O1 --skip-build \
   --root=$RPM_BUILD_ROOT \
   --install-headers=%{_includedir}/python \
   --install-lib=%{python_sitelib}

%files 
%{python_sitelib}/dns
%{python_sitelib}/dnspython-*-info

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.2
- Rebuilt for Fedora
* Mon Dec 27 2010 Ercole 'ercolinux' Carpanetto <ercole69@gmail.com> 1.9.2-1mamba
- package created by autospec
