Summary: The local directory layout for a Linux system
Name: filesystem-local
Version: 1
Release: 3.1
License: Public Domain
Group: System Environment/Base
Requires: filesystem

%description
Filesystem-local contains the local directory layout
for a Linux operating system.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/{bin,%{_lib},share}
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo /usr/local/%{_lib} > %{buildroot}%{_sysconfdir}/ld.so.conf.d/local-%{arch}.conf

%files
%dir /usr/local
%dir /usr/local/bin
%dir /usr/local/%{_lib}
%dir /usr/local/share
%{_sysconfdir}/ld.so.conf.d/local-%{arch}.conf

%changelog
* Fri Nov 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
