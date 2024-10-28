Name:          dhcdbd
Version:       3.0
Release:       2.1
Summary:       Provides D-BUS control of the ISC dhclient software
Group:         Network/Libraries
URL:           https://people.redhat.com/jvdias/dhcdbd/
Source:        https://ftp.debian.org/debian/pool/main/d/dhcdbd/dhcdbd_%{version}.orig.tar.gz
#https://people.redhat.com/jvdias/dhcdbd/dhcdbd-%{version}.tar.gz
License:       GPL
BuildRequires: dbus-devel

%description
dhcdbd exists to :
     o  provide D-BUS control of the ISC dhclient software,
     o  store DHCP configuration parameters (options) persistently
     o  providing access to DHCP options over D-BUS
     o  notify applications of changes to DHCP IP interface configuration

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_sysconfdir}/dbus-1/system.d/dhcdbd.conf
/sbin/dhcdbd
%{_datadir}/dbus-1/services/dhcdbd.service
%doc COPYING README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora

* Wed Feb 04 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 3.0-1mamba
- automatic update by autodist

* Sat Oct 25 2008 Tiziana Ferro <tiziana.ferro@email.it> 2.0-2mamba
- rebuild

* Thu Mar 08 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 2.0-1qilnx
- update to version 2.0 by autospec

* Fri Mar 10 2006 Silvan Calarco <silvan.calarco@mambasoft.it> 1.12-1qilnx
- package created by autospec
