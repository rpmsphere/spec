Name:           fakeap
Version:        0.3.2
Release:        2.1
Summary:        Fake Access Points generator

Group:          Applications/Internet
License:        GPLv2
URL:            https://www.blackalchemy.to/project/fakeap/
#Reported upstream about the url issue but till now no answer
#Source0:        https://www.blackalchemy.to:8060/project/fakeap/download.php?name=%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Buildarch:      noarch

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
FakeAP generates thousands of counterfeit 802.11b access points. Hide in 
plain sight amongst Fake AP's cacophony of beacon frames. As part of a 
honeypot or as an instrument of your site security plan, Fake AP confuses
Wardrivers, NetStumblers, Script Kiddies, and other undesirables.

%prep
%setup -q

%build
#nothing to build

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 0755 fakeap.pl $RPM_BUILD_ROOT%{_bindir}/%{name}.pl
#add shebang to make rpmlint quite
sed -i -e '1d;2i#!/usr/bin/perl' $RPM_BUILD_ROOT%{_bindir}/%{name}.pl

%files
%doc COPYING CREDITS INSTALL README lists/
%{_bindir}/%{name}.pl

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora

* Sat Nov 01 2008 Fabian Affolter <fabian@bernewireless.net> - 0.3.2-1
- Initial package for Fedora
