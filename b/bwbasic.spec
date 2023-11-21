Name:         bwbasic
Summary:      A Basic interpreter
Version:      3.20
Release:      6.1
License:      GPL
Group:        Development/Languages/Other
URL:          https://sourceforge.net/projects/bwbasic/
BuildRequires: unzip
BuildRequires: autoconf
BuildRequires: automake
Source0:      https://dl.sourceforge.net/project/%{name}/%{name}/version%20%{version}/%{name}-%{version}.zip
Source1:      %{name}.png
Source2:      %{name}.desktop

%description
The Bywater BASIC Interpreter (bwBASIC) implements a large superset of the ANSI
Standard for Minimal BASIC (X3.60-1978) and a significant subset of the ANSI
Standard for Full BASIC (X3.113-1987) in C.

It also offers shell programming facilities as an extension of BASIC. bwBASIC
seeks to be as portable as possible.

%prep
%setup -q -c

%build
cp /usr/share/automake-1.??/install-sh .
autoconf
sh configure
sed -i 's|-g -ansi|-g -ansi -fPIE|' Makefile
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 bwbasic $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m755 renum $RPM_BUILD_ROOT%{_bindir}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README* bwbasic.doc COPYING DOCS/*
%{_bindir}/%{name}
%{_bindir}/renum
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jan 30 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.20
- Rebuilt for Fedora
* Mon Jul 27 2009 lars@linux-schulserver.de
- update to 2.50:
  + main change was support for CMS
    (another IBM mainframe - last release added MVS)
  + New build procedure for MVS and CMS
  + some bug fixes
- adapted patches for new version
- added bwbasic-2.50-docu.patch
* Thu Jan 15 2009 lars@linux-schulserver.de
- added debian patches:
  + bwbasic-2.20pl2-silence.patch (usage of stderr)
  + bwbasic-2.20pl2-save_startposition.patch (self explaining)
  + bwbasic-2.20pl2-overflow.patch (fixed buffer overflow)
- added bwbasic-2.20pl2-optflags.patch for renum.c
- added bwbasic-2.20pl2-uninitialized-variable.patch
* Wed Oct  8 2008 lars@linux-schulserver.de
- added bwbasic-2.20pl2-gcc-warnings.patch
* Mon Sep 22 2008 lars@linux-schulserver.de
- moved to Education base repository
* Mon May 19 2008 lars@linux-schulserver.de
- added URL
- fix desktop file category
* Mon Apr 21 2008 lars@linux-schulserver.de
- package reduxed for openSUSE-Education
* Wed Apr  3 2002 ro@suse.de
- automake is in /usr/share/automake-1.6 currently, use wildcard in specfile
* Mon Apr 23 2001 cihlar@suse.cz
- fixed warnings on ia64
* Mon Oct 30 2000 cihlar@suse.cz
- bzipped sources
- added suse_update_config
- used RPM_OPT_FLAGS
* Mon May 15 2000 cihlar@suse.cz
- Group sorted
* Tue Apr  4 2000 cihlar@suse.cz
- upgrade to version 2.20 patch level 2
- added BuildRoot
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Tue Sep 22 1998 ro@suse.de
- update to version 2.20 pl 1
