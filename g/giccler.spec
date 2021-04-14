Name: giccler
Summary: Manipulate color profiles containing VCGT data in realtime
Version: 0.2.4
Release: 5.1
Group: Converted/utils
License: see /usr/share/doc/giccler/copyright
URL: http://mein-neues-blog.de/category/giccler/
Source0: http://repository.mein-neues-blog.de:9000/archive/%{name}-%{version}_all.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils

%description
A tool to make some minor corrections to the VCGT ramps provided in those
profiles – preferably in realtime.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}
cp -a * %{buildroot}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}.py

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/doc/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/%{name}

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuilt for Fedora
