%undefine _debugsource_packages

Name:           xbanner
BuildRequires:  libX11-devel, libXpm-devel, imake
License:        GPL v2 or later
Group:          Amusements/Toys/Background
Version:        1.31
Release:        2089.1
Summary:        X Window System background writings and images
URL:            https://www.hijinks.com/~spade/linux/XBanner/
Source:         XBanner%{version}.tar.bz2
Patch0:         XBanner%{version}.dif
Patch1:         xbanner-%{version}-gets.patch

%description
How about your company's name in the background of the login screen? Or
your company's logo? It will work with xbanner which is designed for
use with, for example, XDM login screens.

Many example configurations may be found in /usr/share/xbanner and its
subdirectories. Documentation lies in /usr/share/doc/packages/xbanner.
There you can find an HTML version of the documents.

Authors:
--------
    Amit Margalit <amitm@netvision.net.il>

%prep
%setup -qn XBanner%{version}
%patch0
%patch1

%build
xmkmf -a
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Makefile
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
#
# examples
#
BINDIR=../../../bin
DEMODIR=$RPM_BUILD_ROOT/usr/share/xbanner
APPDEF=$RPM_BUILD_ROOT/usr/share/X11/app-defaults/
install -d $DEMODIR
(cd samples/ && cp -a * $DEMODIR)
(cd $DEMODIR/Demo
cat Demo.bash | sed -e "s:\.\./\.::g" >Demo
rm Demo.bash
ln -s $BINDIR/xbanner
ln -s $BINDIR/freetemp
cd ..
rm README.Demo XBanner.sample
install -d $APPDEF
mv XBanner.ad $APPDEF/XBanner
)
#
# docs
#
DOCDIR=$RPM_BUILD_ROOT/$RPM_DOC_DIR/xbanner
install -d $DOCDIR
install -m 644 *.xpm $DEMODIR
install -m 644 docs/{C*,*.html,*.gif} $DOCDIR

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/xbanner/
%doc %{_docdir}/xbanner/
%{_bindir}/*
%config %{_datadir}/X11/app-defaults/XBanner

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.31
- Rebuilt for Fedora
* Thu Nov 16 2006 anosek@suse.cz
- replaced dangerous gets() function by fgets()
  [#219044] (gets.patch)
* Mon Aug  7 2006 mmarek@suse.cz
- moved from /usr/X11R6 to /usr to build with new Xorg
* Sat May 27 2006 schwab@suse.de
- Don't strip binaries.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sun Oct 10 2004 schwab@suse.de
- Fix requires.
* Sun Jan 11 2004 adrian@suse.de
- add %%defattr
* Wed Sep 13 2000 vinil@suse.cz
- upgrade to 1.31
- major file relocation
- description fixed
* Wed Jul 19 2000 vinil@suse.cz
- no more requires xpm
* Thu May  4 2000 vinil@suse.cz
- buildroot added
- bugs in demos fixed
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Jan  2 1997 maddin@suse.de
  first S.u.S.E. version
  copy all sample files to /usr/X11R6/lib/X11/xbanner
  copy all doc files (including html) to /usr/doc/packages/xbanner
