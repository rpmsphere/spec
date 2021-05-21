Name:		wireless-regdb
Summary:	802.11 regulatory domain database
Version:	2011.04.28
Release:	2.1
URL:		http://wireless.kernel.org/en/developers/Regulatory#The_regulatory_database
Source0:	wireless-regdb-%{version}.tar.bz2
License:	BSD3c(or similar)
Group:		Hardware/Wifi
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch

%description
The 802.11 regulatory domain database is used by CRDA and provides
allowed frequency ranges for 802.11 wireless drivers.

Authors:
--------
    Luis R. Rodriguez <mcgrof@gmail.com>
    Johannes Berg <johannes@sipsolutions.net>
    Michael Green <Michael.Green@Atheros.com>

%prep
%setup -n wireless-regdb-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files 
%defattr(-,root,root)
%dir %{_prefix}/lib/crda
%dir %{_prefix}/lib/crda/pubkeys
%{_prefix}/lib/crda/regulatory.bin
%{_prefix}/lib/crda/pubkeys/*pem
%{_prefix}/share/man/man5/regulatory.bin.5.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2011.04.28
- Rebuilt for Fedora
* Thu May 19 2011 - joerg.lorenzen@ki.tng.de
- update to version 2011.04.28
* Thu Dec 02 2010 - joerg.lorenzen@ki.tng.de
- Initial package, version 2010.11.24
