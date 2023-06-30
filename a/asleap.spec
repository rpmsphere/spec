Name:           asleap
Version:        2.2
Release:        3.1
Summary:        Recovering tool for weak LEAP and PPTP passwords
Group:          Applications/Internet
License:        GPLv2
URL:            https://www.willhackforsushi.com/?page_id=41
Source0:        https://www.willhackforsushi.com/code/%{name}/%{version}/%{name}-%{version}.tgz
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel 
Patch0:		asleap-glibc.patch

%description
asleap is a tool to recover weak LEAP and PPTP passwords. asleap is the
product of the research of weaknesses in Cisco's proprietary LEAP protocol.

asleap can work directly from any wireless interface in RFMON mode and can
perform channel hopping.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 0755 asleap $RPM_BUILD_ROOT%{_sbindir}/asleap
install -Dp -m 0755 genkeys $RPM_BUILD_ROOT%{_sbindir}/genkeys
#remove exec permissions from files in scripts directory
find scripts/*.pl -type f -name \* -exec chmod 644 {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README THANKS scripts/
%{_sbindir}/%{name}
%{_sbindir}/genkeys

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
* Sun Nov 02 2008 Fabian Affolter <fabian@bernewireless.net> - 2.2-1
- Initial package for Fedora
