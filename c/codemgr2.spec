Name: codemgr2
Summary: Centralized Source Code and Revision Control System
Version: 1.4.1
Release: 5.1
Group: System Administration
License: GPL
URL: https://code.google.com/archive/p/codemanager2/
Source0: %{name}-%{version}.tgz
BuildArch: noarch

%description
CM2 has been designed to provide a complete source code control system for
a set of developers sharing the same working directory tree (a practice
still common believe it or not).

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}/usr
mv share %{buildroot}/usr
mkdir %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}

%files
%{_mandir}/man1/*
%{_datadir}/%{name}

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.1
- Rebuilt for Fedora
