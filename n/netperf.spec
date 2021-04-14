Summary: Performance testing tool for TCP/UDP
Name: netperf
Version: 2.7.0
Release: 2.1
License: HP non-commercial
Group: Applications/Internet
URL: http://www.netperf.org/netperf/NetperfPage.html
Source: ftp://ftp.netperf.org/netperf/netperf-%{version}.tar.gz

%description
Netperf is a tool to measure TCP/UDP performance.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --program-prefix="%{?_program_prefix}"
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%doc COPYING README Release_Notes
%doc %{_mandir}/man1/netperf.1*
%doc %{_mandir}/man1/netserver.1*
%doc %{_infodir}/netperf.*
%{_bindir}/netperf
%{_bindir}/netserver

%changelog
* Thu Feb 16 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.0
- Rebuilt for Fedora
* Sat Sep 29 2012 Denis Fateyev <denis@fateyev.com> - 2.6.0-1
- Updated to release 2.6.0
* Thu Feb 23 2012 Gerd v. Egidy <gerd@egidy.de> - 2.5.0-1
- Updated to release 2.5.0
- License tag changed to reflect COPYING file as included in source
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 2.4.5-1
- Updated to release 2.4.5.
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 2.4.2-1
- Initial package. (using DAR)
