Name:           vsntp
Version:        2.0.0
Release:        2.1
Summary:        SNTP Client for Virtual PC
License:        GPL
URL:            https://sourceforge.net/projects/vsntp/
Source0:        https://sourceforge.net/projects/vsntp/files/vsntp/2.0.0/vsntp-2.0.0.tar.gz 

%description
An SNTP client for Virtual PC. It is for machines that do not have a sane time
and a working hardware RTC. It synchronize the system time frequently with a
nearby NTP server. It uses settimeofday(). It is based on RFC 1769 and RFC 1305.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS* ChangeLog* COPYING* INSTALL* NEWS* README* THANKS*
%{_sbindir}/vsntp
%exclude %{_datadir}/info/dir
%{_datadir}/info/vsntp.info.gz
%{_datadir}/man/man8/vsntp.8.gz

%changelog
* Mon Jul 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuilt for Fedora
