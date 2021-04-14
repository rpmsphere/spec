Name:           rfb
BuildRequires:  gcc-c++ xclass-devel libX11-devel libXpm-devel imake libXtst-devel
License:        GPL v2 or later
Group:          System/X11/Utilities
Requires:       xclass
Version:        0.6.1
Release:        1379.1
URL:            http://www.hexonet.de/software/rfb/
#Original source: http://www.hexonet.de/download/rfb-0.6.1.tar.gz
Source0:        http://www.hexonet.de/download/rfb-0.6.1.tar.bz2
Patch0:         rfb-0.6.1-rpmoptflags.patch
Patch1:         rfb-0.6.1-gcc3.dif
Patch2:         rfb-0.6.1-socklen_t.dif
Patch3:         %{name}-%{version}-gcc4.3.diff 
Summary:        heXoNet RFB (remote control for the X Window System)

%description
The heXoNet RFB Software package includes many different projects. The
goal of this package is to provide a comprehensive collection of
rfb-enabled tools and applications. One application, x0rfbserver, was,
and maybe still is, the only complete remote control solution for the X
Window System.

Authors:
--------
    Jens Wagner <jwagner@hexonet.de>

%prep
%setup0
%patch0 -p1
%patch1
%patch2
%patch3

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall"
make depend
make

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1 $RPM_BUILD_ROOT%{_bindir}
install -m 644 man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 x0rfbserver/x0rfbserver $RPM_BUILD_ROOT%{_bindir}/
install -m 755 xrfbviewer/{xrfbviewer,xplayfbs} $RPM_BUILD_ROOT%{_bindir}/
install -m 755 rfbcat/rfbcat $RPM_BUILD_ROOT%{_bindir}/
install -m 755 xvncconnect/xvncconnect $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING INSTALL README rfm_fbs.1.0.html
%doc %{_mandir}/man1/*.1*
%{_bindir}/*

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuilt for Fedora
* Fri Oct 26 2007 anicka@suse.cz
- fix for gcc 4.3
* Tue May 29 2007 anosek@suse.cz
- changed BuildRequires xclass -> xclass-devel
* Wed Dec 13 2006 anosek@suse.cz
- changed prefix /usr/X11R6/bin -> /usr/bin
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sat Jan 14 2006 schwab@suse.de
- Don't strip binaries.
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Fri Jun 13 2003 mfabian@suse.de
- remove /usr/X11R6/bin directory from filelist because it is
  already part of the filesystem RPM.
* Thu Jun 13 2002 mfabian@suse.de
- Add "Requires: xclass". I thought it was only required at
  build time because the rfb stuff is statically linked
  against xclass, but that's not quite true, xplaybfs needs
  some icons from the xclass package. Thanks to
  Michael Hasenstein <mha@suse.com> for noticing.
* Sun May 12 2002 schwab@suse.de
- Use socklen_t.
* Sat Apr 13 2002 ro@suse.de
- make it compile with gcc-3.1
* Tue Feb 26 2002 mfabian@suse.de
- update to version 0.6.1
* Wed Feb  6 2002 ihno@suse.de
- Use of CFLAGS in makefile
- fix the reading of the passwords (was endiandependend)
* Wed Jun 13 2001 mfabian@suse.de
- remove unnecessary "Requires: xclass", it is only required
  at build time
- move binaries to /usr/X11R6/bin
- strip binaries
* Fri Jun  8 2001 mfabian@suse.de
- new package: rfb-0.1.2
