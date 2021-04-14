%undefine _debugsource_packages

Name:           ipgrab
Version:        0.9.10
Release:        2.1
Summary:        A verbose packet sniffer for hosts
License:        GPLv2+
URL:            http://ipgrab.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  libpcap-devel

%description
This program reads and parses packets from the link layer through the
transport layer, dumping explicit header information along the way.
It is a lot like tcpdump from LBL except that I've made an effort to
dump every relevant header field possible.  The overall structure of
the code is loosely based on tcpdump and I've lifted a few modules
from the tcpdump distribution when necessary, rather than re-inventing
the wheel.  In particular, the address conversion hashing routines are
pretty much lifted verbatim, as well as the TCP options section.

%prep
%setup -q

%build
export CFLAGS="-fPIC -std=gnu89"
./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_infodir}/%{name}.info.gz
%{_bindir}/%{name}

%changelog
* Mon Jan 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.10
- Rebuilt for Fedora
* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.8-1
- Initial package for Fedora
