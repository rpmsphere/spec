Name:           etherwake
Version:        1.09
Release:        4.1
License:        GPL
Group:          Productivity/Networking/Boot/Utilities
Source:         etherwake_1.09.orig.tar.gz
Summary:        A little tool to send magic Wake-on-LAN packets

%description
A little tool to send magic Wake-on-LAN packets
You can wake up WOL compliant Computers which have been powered down to
sleep mode or start WOL compliant Computers with a BIOS feature.

WOL is an abbreviation for Wake-on-LAN. It is a standard that allows you
to turn on a computer from another location over a network connection.
etherwake also supports WOL passwords.

Authors:
--------
    Donald Becker <becker@scyld.com>

%prep
%setup -n etherwake-1.09.orig

%build
gcc %{optflags} -Wno-format-security -o etherwake ether-wake.c

%install
%{__install} -D -m 0755 etherwake   $RPM_BUILD_ROOT%{_sbindir}/etherwake
%{__install} -D -m 0644 etherwake.8 $RPM_BUILD_ROOT%{_mandir}/man8/etherwake.8

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_sbindir}/etherwake
%{_mandir}/man8/etherwake.8*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.09
- Rebuilt for Fedora
* Wed Apr  4 2007 mrueckert@suse.de
- initial package of 1.09
