Name: vmware-manager
Summary: Utility to manage VMware virtual machines
Version: 0.2.0
Release: 3
Group: contrib/admin
License: Free Software
URL: https://github.com/hash-bang/VMM
Source0: VMM-master.zip
BuildArch: noarch
#Requires: perl
#Requires: libconfig-inifiles-perl,
#Requires: libnumber-format-perl,
#Requires: libterm-readkey-perl,
#Requires: libtext-glob-perl,
#Requires: libdata-dump-perl

%description
This package provides vwm, a command-line tool for managing VMware
virtual machines. This is primarily useful for larger installations
where virtuals need to be migrated, cloned or otherwise modified
from the command line.

vwm requires the non-free VMware Vsphere Perl SDK to be installed.

%prep
%setup -q -n VMM-master

%build

%install
install -Dm755 vmm %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1

%files
%doc README.md docs/*
%{_bindir}/*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
