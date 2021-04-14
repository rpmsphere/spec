%undefine _debugsource_packages
Name:           namebench
Version:        1.3.1
Release:        17.1
License:        GPL v2 or later
Source:         http://namebench.googlecode.com/files/%{name}-%{version}-source.tgz
Group:          Development/Libraries/Python
Summary:        Hunt down the fastest DNS servers
URL:            http://code.google.com/p/namebench/
BuildRequires:  python2-devel
BuildArch:      noarch

%description
Nnamebench hunts down the fastest DNS servers available for your
computer to use. namebench runs a fair and thorough benchmark using
your web browser history, tcpdump output, or standardized datasets in
order to provide an individualized recommendation. namebench is
completely free and does not modify your system in any way.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}/usr/%{name} %{buildroot}%{_datadir}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}.py

%clean
rm -rf %buildroot

%files
%{_bindir}/*
%{python2_sitelib}/*
%{_datadir}/%{name}

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.1
- Rebuilt for Fedora
* Fri Jan 29 2010 doiggl@velocitynet.com.au
- packaged namebench version 1.3.1 using the buildservice spec file wizard
