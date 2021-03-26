%global debug_package %{nil}

Name:           hextris
Provides:       cxhextris
Provides:       xhextris
Version:        1.0
Release:        7.1
Summary:        Xhextris and CXhextris, hexagonal versions of Xtetris
License:        MIT
Group:          Amusements/Games/Puzzle
Source:         hextris.tar.gz
Patch:          hextris.dif
URL:            http://www.hextris.com/blog/
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel

%description
This package provides two games under X Window System:
Xhextris and the colored version CXhextris.  Both are fast games involving
dropping hexagonal blocks similar to xtetris.
Both version are modified. They use the same font (but different
letters) and they use the cursor keys.

Authors:
--------
    David Markley <dam@cs.cmu.edu>
    Khun Yee Fung <clipper@csd.uwo.ca>

%prep
%setup -q -n hextris
%patch

%build
make %{?_smp_mfalgs} -f Makefile.Linux compile FONTDIR=%{_datadir}/fonts MANDIR=%{_mandir}

%install
make -f Makefile.Linux install DESTDIR=%{buildroot} FONTDIR=%{_datadir}/fonts MANDIR=%{_mandir}

%files
%{_bindir}/*%{name}
%{_datadir}/fonts/misc/xhextris.pcf.gz
%{_mandir}/man1/*hextris.1.*
%config(noreplace) /var/games/*hextris-scores

%changelog
* Wed Jun 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
* Mon Oct  1 2012 werner@suse.de
- Use new font rpm scriptlets API
* Sat Mar 24 2012 jengelh@medozas.de
- Parallel build with %%_smp_mflags; strip redundant spec sections
- add homepage URL
* Mon Dec  8 2008 dominique-obs@leuenberger.net
- Remove the suid/sgid from the binary. OBS does not like to
  distribute such packages. Will have to check if everzthing works
* Thu Jan 10 2008 werner@suse.de
- Bump it to openSuSE.org
* Thu Mar  2 2000 werner@suse.de
- /usr/man -> /usr/share/man
* Fri Jan 28 2000 werner@suse.de
- Make xhextris.pcf.gz instead of xhextris.pcf.Z (avoid compress)
* Mon Nov 29 1999 ke@suse.de
- fix score files problem: binaries are games.game and sgid "game"; score
  files living are 664.
- cleanup the %%files list.
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
