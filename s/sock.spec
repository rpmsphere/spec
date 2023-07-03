Name:         sock
URL:          https://atrey.karlin.mff.cuni.cz/~mj/linux.shtml
License:      GPL, Other License(s), see package
Group:        Productivity/Networking/Other
Version:      1.1
Release:      94.1
Summary:      A Simple Shell Interface to Network Sockets
Source:       %{name}-%{version}.tar.bz2

%description
This program serves as an interface for network sockets for use in both
shell scripts and manually from the command line. In contrast to
netcat, it handles EOF in a way so, for example, tar archives can
easily be transferred. See the man page (man 1 sock) for more details.

Example:

host1 # sock -l :7777 > file host2 # cat file | sock host1:7777

host1 # sock -l :7777 | tar xvzfp - host2 # tar czfp - some/dir | sock
host1:7777

Authors:
--------
    Martin Mares <mj@ucw.cz> 

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=$RPM_BUILD_ROOT/usr --mandir=$RPM_BUILD_ROOT/%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}

%changelog
* Sun Sep 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Feb 26 2004 hmacht@suse.de
- added option # norootforbuild in specfile
* Thu Jul 24 2003 poeml@suse.de
- update to 1.1
  - When an address is missing, assume localhost. This way
    "sock :23" etc. works as expected
  - UNIX domain sockets work with long filenames
  - Added "-n" (avoid reverse DNS lookups) switch
  - Inverted the "-e" switch: default is now to terminate after
    seeing EOF in both direction
  - Updated man page
* Tue May 13 2003 poeml@suse.de
- use %%defattr
- bzip sources
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Wed Mar 21 2001 poeml@suse.de
- create package
