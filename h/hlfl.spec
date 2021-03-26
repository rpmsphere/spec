Name:         hlfl
Summary:      High-Level Firewall Language
URL:          http://www.hlfl.org/
Group:        Language
License:      GPL
Version:      0.60.1
Release:      3.1
Source0:      http://www.hlfl.org/hlfl/hlfl-%{version}.tar.gz

%description
HLFL stands for "High Level Firewall Language". It translates
your high level language firewalling rules into usable rules for
IPChains, NetFilter, IPFilter, IPFW, Cisco IOS, and many others.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir}
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
rm -f $RPM_BUILD_ROOT%{_prefix}/share/hlfl/CodingStyle
rm -f $RPM_BUILD_ROOT%{_prefix}/share/hlfl/RoadMap
rm -f $RPM_BUILD_ROOT%{_prefix}/share/hlfl/TODO

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.60.1
- Rebuild for Fedora
