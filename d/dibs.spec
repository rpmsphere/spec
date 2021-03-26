%global debug_package %{nil}
Name:         dibs
License:      BSD
Group:        Development/Libraries/Python
Version:      0.93
Release:      4.1
Summary:      Distributed Internet Backup System
URL:          http://web.mit.edu/~emin/www.old/source_code/dibs/
Source:       http://web.mit.edu/~emin/www.old/source_code/dibs/DIBS-%{version}.tar.gz
BuildArch:    noarch
BuildRequires:  python2-devel 

%description
Since disk drives are cheap, backup should be cheap too. Of course it does not
help to mirror your data by adding more disks to your own computer because a
virus, fire, flood, power surge, robbery, etc. could still wipe out your local
data center. Instead, you should give your files to peers (and in return store
their files) so that if a catastrophe strikes your area, you can recover data
from surviving peers. The Distributed Internet Backup System (DIBS) is designed
to implement this vision.

%prep
%setup -q -n DIBS-%{version}

%build
export CFLAGS="%{optflags}"
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm -r %{buildroot}/usr/doc
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/cgi-bin/*.cgi

%clean
rm -rf %{buildroot}

%files
%doc CHANGELOG doc LICENSE README RELEASE_NOTES
%{_bindir}/*
%{_datadir}/%{name}/*
%{python2_sitelib}/dibs_lib
%{python2_sitelib}/DIBS-*

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.93
- Rebuild for Fedora
