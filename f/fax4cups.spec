Summary: A fax backend for CUPS
Name: fax4cups
Version: 1.29
Release: 4.1
License: GPL
Group: Applications/Communications
URL: https://freshmeat.net/fax4CUPS
Source: https://vigna.dsi.unimi.it/fax4CUPS/fax4CUPS-%{version}.tar.gz
BuildArch: noarch

%description
fax4CUPS consists of some PPD (PostScript Printer Definition) files and a shell
scripts that acts as a back end for CUPS (the Common Unix Printing System).
Essentially, you print with lpr and the fax is sent. fax4CUPS supports
efax, mgetty-fax, capisuite and HylaFAX. To use the HylaFAX backend, you
also need grep and sudo.

%prep
%setup -q -n fax4CUPS-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/lib/cups/backend
mkdir -p $RPM_BUILD_ROOT/usr/share/cups/model/FAX
mkdir -p $RPM_BUILD_ROOT/var/log/fax
install -m 644 ./fax4CUPS.1 $RPM_BUILD_ROOT/usr/share/man/man1
install -m 755 ./efax $RPM_BUILD_ROOT/usr/lib/cups/backend
install -m 644 ./efax.ppd $RPM_BUILD_ROOT/usr/share/cups/model/FAX
install -m 755 ./mgetty-fax $RPM_BUILD_ROOT/usr/lib/cups/backend
install -m 644 ./mgetty-fax.ppd $RPM_BUILD_ROOT/usr/share/cups/model/FAX
install -m 755 ./capisuite-fax $RPM_BUILD_ROOT/usr/lib/cups/backend
install -m 644 ./capisuite-fax.ppd $RPM_BUILD_ROOT/usr/share/cups/model/FAX
install -m 755 ./hylafax $RPM_BUILD_ROOT/usr/lib/cups/backend
install -m 644 ./hylafax.ppd $RPM_BUILD_ROOT/usr/share/cups/model/FAX

%post
systemctl restart cups

%files
/usr/share/man/man1/fax4CUPS.1*
/usr/lib/cups/backend/efax
/usr/lib/cups/backend/mgetty-fax
/usr/lib/cups/backend/capisuite-fax
/usr/lib/cups/backend/hylafax
/usr/share/cups/model/FAX/efax.ppd
/usr/share/cups/model/FAX/mgetty-fax.ppd
/usr/share/cups/model/FAX/capisuite-fax.ppd
/usr/share/cups/model/FAX/hylafax.ppd
%doc COPYING CHANGES

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.29
- Rebuilt for Fedora
* Wed Feb 10 2010 Sebastiano Vigna <vigna@dsi.unimi.it>
- Fixes, updates, Samba jobname-based printing.
* Wed Jan 18 2006 Sebastiano Vigna <vigna@dsi.unimi.it>
- Fixes and better cleanup suggested by Diab Jerius.
  The obsolete fax back end has been dropped.
* Fri Aug 19 2005 Sebastiano Vigna <vigna@dsi.unimi.it>
- Some more fixes.
* Tue Jul 19 2005 Sebastiano Vigna <vigna@dsi.unimi.it>
- Better return codes for empty phone numbers.
* Wed Jul 07 2004 Sebastiano Vigna <vigna@dsi.unimi.it>
- New capisuite-fax backend by Daniel Glanzmann and many small fixes.
* Fri Sep 06 2003 Sebastiano Vigna <vigna@dsi.unimi.it>
- Fixed wrong location for HylaFAX sendfax program.
* Thu May 29 2003 Sebastiano Vigna <vigna@dsi.unimi.it>
- New mgetty-fax backend by Daniel Glanzmann and many small fixes.
* Fri Sep 20 2002 Sebastiano Vigna <vigna@dsi.unimi.it>
- Added feature and fix proposed by Kevin Ivory and Michael Goffioul
* Mon Jun 10 2002 Sebastiano Vigna <vigna@dsi.unimi.it>
- Fixed problems with CUPS 1.14
* Sat Apr 13 2002 Sebastiano Vigna <vigna@dsi.unimi.it>
- Added support for HylaFAX written by Arnold Moene
* Fri Jun 20 2001 Sebastiano Vigna <vigna@dsi.unimi.it>
- Added note in man page about octal numbers 
* Fri May 06 2001 Sebastiano Vigna <vigna@dsi.unimi.it>
- The CUPS deamon is now restarted after installation.
* Fri May 05 2001 Sebastiano Vigna <vigna@dsi.unimi.it>
- Support for graphical KDE interface added by Michael Goffioul
* Fri May 04 2001 Sebastiano Vigna <vigna@dsi.unimi.it>
- Fixed problems with old bash
* Thu Apr 26 2001 Sebastiano Vigna <vigna@dsi.unimi.it>
- Added efax to dependencies
* Sat Apr 9 2001 Sebastiano Vigna <vigna@dsi.unimi.it>
- new /usr/share/man location for man page.
* Sat Apr 7 2001 Sebastiano Vigna <vigna@dsi.unimi.it>
- First RPM release
