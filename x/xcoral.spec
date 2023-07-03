%undefine _debugsource_packages

Name:           xcoral
BuildRequires:  libX11-devel, libXt-devel
License:        GPL-2.0+
Group:          Productivity/Editors/Other
Summary:        X11 Editor with C/C++/Java Browser and lots more
Version:        3.50.2
Release:        1
URL:            https://xcoral.free.fr/
Source0:        %{name}-%{version}.tar.gz
Patch0:         xcoral-3.47.configure.diff
Patch1:         xcoral-arraysubscript.patch

%description
Half of the YaST developers swear on it, not only because of the built
in C/C++/Java browser. Xcoral provides support for the work with C,
C++, Java, Perl, Ada, and Fortran programs and for the creation of
LaTeX and HTML documents. With the help of the built in 'SMall Ansi C
Interpreter' (SMAC), xcoral can be configured and extended in almost
arbitrary ways. Examples can be found in the directory /usr/lib/xcoral.

Further information about Xcoral and SMAC is available in the detailed
online help system (also available Postscript format).

Authors:
--------
    Lionel Fournigault <xcoral@free.fr>
    Bruno Pages        <xcoral@free.fr>
    Dominique Leveque  <xcoral@free.fr>

%prep
%setup -q
#patch0
#patch1

%build
export LDFLAGS=-Wl,--allow-multiple-definition
CFLAGS="$RPM_OPT_FLAGS -Wno-format-security" \
./configure --prefix=$RPM_BUILD_ROOT/usr --bindir=$RPM_BUILD_ROOT/usr/bin
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib
make installprefix=$RPM_BUILD_ROOT install
find Doc -name '*.ps' -exec bzip2 {} \;
find Doc -name '*.pdf' -exec bzip2 {} \;
#install -D -m 644 %{S:1} $RPM_BUILD_ROOT/etc/skel/.xcoralrc
install -D -m 644 SmacLib/xcoralrc.lf $RPM_BUILD_ROOT/etc/skel/.xcoralrc
sed -i 's|%{buildroot}||' %{buildroot}/usr/bin/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Doc/*
%config(noreplace) /etc/skel/.xcoralrc
%{_bindir}/xcoral
/usr/lib/xcoral

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.50.2
- Rebuilt for Fedora
* Wed Aug 26 2009 mls@suse.de
- make patch0 usage consistent
* Wed Nov  5 2008 meissner@suse.de
- use RPM_OPT_FLAGS, fixed all check_gcc_output errors and warnings.
* Mon May 26 2008 ma@suse.de
- Version 3.47
- Fix using an outdated /etc/skel/.xcoralrc. Use the one included
  in the tarball.
* Wed Dec  5 2007 ro@suse.de
- move /etc/skel/.xcoralrc here
* Fri Jan 26 2007 ma@suse.de
- Fixed array subscript out of range (#152845).
* Wed Jan 24 2007 ro@suse.de
- move from /usr/X11R6 to /usr
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Nov  8 2005 dmueller@suse.de
- don't build as root
* Wed Apr 27 2005 ro@suse.de
- build with gcc-4
* Mon Sep 15 2003 ma@suse.de
- Version 3.42b, fixes segfault when used with KDE-3.1.1.
* Mon Feb 24 2003 ma@suse.de
- Version 3.42, fixes several bugs.
* Thu Sep 19 2002 ma@suse.de
- New Version 3.40
* Tue Oct 30 2001 ma@suse.de
- fixed missing refresh of toolbar if was obscured by popup menu.
* Tue May  8 2001 mfabian@suse.de
- bzip2 sources
* Mon Mar 12 2001 uli@suse.de
- added xf86 to neededforbuild
* Tue Oct 31 2000 ma@suse.de
- removed group unsorted
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Sep  9 1999 bs@suse.de
- fixed call of Check at the end of %%install section
* Mon Jan 25 1999 ma@suse.de
- Zip all "documentation.ps"
* Thu Dec 10 1998 ma@suse.de
- New Version 3.2
* Sat Sep 19 1998 ro@suse.de
- dont redeclare sys_errlist for glibc
* Wed Aug 26 1998 ma@suse.de
- New Version 3.14
- Minor fixes for window geometry handling
- Minor fixes for backspace/delete handling, documentation
  updated
* Tue Oct 21 1997 ma@suse.de
- spec file provided
* Thu Jun 12 1997 hf@suse.de
  New Version 3.1
  Fixed the Backspace - Delete problem in sourcecode.
