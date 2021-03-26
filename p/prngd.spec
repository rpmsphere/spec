Name: prngd
Version: 0.9.29
Release: 9.1
License: Public Domain
Group: Productivity/Security
URL: http://prngd.sourceforge.net/
Source: http://downloads.sourceforge.net/prngd/prngd-%{version}.tar.gz
Patch: prngd-0.9.29_build_config.patch
Summary: Pseudo Random Number Generator Daemon

%description
This is the PRNGD "Pseudo Random Number Generator Daemon". It offers an EGD
compatible interface to obtain random data and is intented to be used as an
entropy source to feed other software, especially software based on OpenSSL. 

Like EGD it calls system programs to collect entropy. 

Unlike EGD it does not generate a pool of random bits that can be called from
other software. Rather more it feeds the bits gathered into the OpenSSL PRNG
from which the "random bits" are obtained when requested. This way, PRNGD is
never drained and can never block (unlike EGD), so it is also suitable to seed
inetd-started programs. It also features a seed-save file, so that it is
immediately usable after system start.

Authors:
--------
    Lutz Jänicke <Lutz.Jaenicke@aet.TU-Cottbus.DE>

%prep
%setup -q
%patch

%build
%{__make} OPTFLAGS="%{optflags} -g"
gcc -o prngd-ctl %{optflags} tools/prngd-ctl.c

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -D -m 0755 prngd     $RPM_BUILD_ROOT%{_sbindir}/prngd
%{__install} -D -m 0755 prngd-ctl $RPM_BUILD_ROOT%{_sbindir}/prngd-ctl
%{__install} -D -m 0644 prngd.man $RPM_BUILD_ROOT%{_mandir}/man1/prngd.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_sbindir}/prngd
%{_sbindir}/prngd-ctl
%{_mandir}/man1/prngd.1*
%doc 00* ChangeLog

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.29
- Rebuild for Fedora
* Sun Mar  4 2007 mrueckert@suse.de
- updated urls
