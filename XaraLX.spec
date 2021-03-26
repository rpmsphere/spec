Name:           XaraLX
License:        GNU General Public License (GPL)
Group:          Productivity/Images/Editor
Version:        0.7r1785
Release:        1
Summary:        Xara Xtreme for Linux is a powerful, general purpose vector graphics program
URL:            http://www.xaraxtreme.org/developers/general/source_code__building.html
# mandriva libwxgtk2.6-devel is 2.6.1, XaraLX needs 2.6.3, so we bring our own wxGTK-devel
BuildRequires:  gcc-c++ libjpeg-devel libtiff-devel libpng-devel perl libxml2-devel zip unzip gettext-devel 
BuildRequires:  wxGTK-devel
# documentation has wrong file end of line encoding
BuildRequires:  dos2unix
Requires:       ImageMagick
Source:         http://downloads2.xara.com/opensource/%name-%version.tar.bz2
Source1:        XARFormatDocument.pdf
Source2:        xaralx.desktop
Source3:        %name-0.7.zh_TW.po
Requires:       ImageMagick
Patch:          abuild.diff
Patch2:         XaraLX-0.7r1785-missing-declaration.patch
Patch3:		xaralx_fix_gcc4.patch
Patch4:		xaralx_avoid_glib2.patch
ExclusiveArch:  %ix86  x86_64

%description
Xara Xtreme for Linux is a powerful, general purpose vector graphics program for Unix
platforms including Linux, FreeBSD and (in development) OS-X.  Formely known as
Xara LX, it is based on Xara Xtreme for Windows, which is the fastest graphics
program available, period. The Xara Xtreme source code was made available
open-source in early 2006, and is being ported to Linux. This process is almost
complete and Xara Xtreme for Linux is available for download now. 

Authors:
--------
    dev@xaraxtreme.org


%package devel
Summary:        Development files for XaraLX
Group:          Development/Other
License:        GNU General Public License (GPL)
Requires:       %name = %version

%description devel
Files to develop applications using XaraLX.

Authors:
--------
    dev@xaraxtreme.org

%prep
%setup -q -n XaraLX-%{version}
%patch -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
find -type d -name .svn -print0 | xargs -0 rm -rf {} \;

%build
./autogen.sh
pushd filters/SVGFilter
autoreconf -f -i
popd
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
%configure --enable-unicode \
           --enable-xarlib \
           --enable-filters \
           --disable-svnversion

%{__make} %{?jobs:-j%jobs}

%install
mkdir -p %buildroot/%{_bindir}
%makeinstall
(cd %buildroot%{_bindir} && ln -s XaraLX xara  && ln -s XaraLx xaralx)
mkdir -p %buildroot/%{_datadir}/%{name}
(cd %buildroot/%{_datadir} && ln -s %{name} xaralx)

# /usr/share/xaralx/doc/xarax/ is used by the application for online help
(cd %buildroot/%{_datadir}/%{name} && ln -s %{_docdir}/%{name}/help doc)

install -m 644 %{S:1} %buildroot%{_datadir}/%{name}
install -D -m 644 doc/en/LICENSE %buildroot%{_docdir}/%{name}/help/LICENSE

cp -a Designs TextDesigns Templates filters/SVGFilter/{tests,images,openclipart,samples} testfiles %buildroot/%{_datadir}/%{name}
cat doc/en/xaralxHelp.tar.gz | (cd %buildroot/%{_docdir}/%{name}/help; tar zxvf - )

find %buildroot/%{_docdir} -type f -print0 | xargs -0 dos2unix -q -o;
find %buildroot/%{_datadir} %buildroot/%{_docdir} -type f -print0 | xargs -0 chmod 644;

perl -ape 's{((src|document.location\s+)=.?")}{$1help/}g;' < %buildroot/%{_docdir}/%{name}/help/xaralx.htm > %buildroot/%{_docdir}/%{name}/help.html

install -m 644 COPYING LICENSE README MTRand.txt doc/gifutil.txt doc/XSVG.txt %buildroot/%{_docdir}/%{name}/

install -D -m 644 doc/xaralx.1 %buildroot%{_mandir}/man1/XaraLX.1
(cd %buildroot%{_mandir}/man1 && ln -s XaraLX.1 xaralx.1 && ln -s XaraLX.1 xara.1)

install -D -m 644 xaralx.png %buildroot%{_datadir}/pixmaps/xaralx.png
install -D -m 644 %{SOURCE2} %buildroot%{_datadir}/applications/xaralx.desktop

chmod 750 %buildroot%{_datadir}/XaraLX/tests/makerandom.sh

mkdir -p %buildroot%{_datadir}/locale/zh_TW/LC_MESSAGES
msgfmt %{SOURCE3} -o %buildroot%{_datadir}/locale/zh_TW/LC_MESSAGES/XaraLX.mo

%clean
rm -rf %buildroot

%files
%doc %{_docdir}/%{name}
%{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/xaralx
%dir %{_datadir}/xaralx/filters
%{_datadir}/%{name}/*
%{_datadir}/xaralx/*
%{_datadir}/xaralx/filters/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/xaralx.png
%{_datadir}/locale/*/LC_MESSAGES/XaraLX.mo
%{_mandir}/man1/*

%files devel
%dir  %_includedir/xarlib
%_includedir/xarlib/*.h
%_libdir/libXar.a
%_libdir/pkgconfig/Xar.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7r1785
- Rebuild for Fedora
* Wed Jan 23 2008 kirill.kirillov@gmail.com
- disabled update-desktop-files macros not to remove existing translations
- fixed desktop file to be displayed in main menu
* Mon Jan 21 2008 lars@linux-schulserver.de
- added XaraLX-0.7r1785-missing-declaration.patch to build with
  gcc4.3.0
- convert documentation from dos to unix encoding
- use fdupes
* Sun Nov 25 2007 lars@linux-schulserver.de
- update to 0.7r1785
- added ImageMagick to Requires
- fix desktop file again
* Tue Oct  9 2007 lars@linux-schulserver.de
- build against up-to-date wxGTK version
- fix desktop file
- added unzip to buildrequires
- use -fno-strict-aliasing
* Wed Oct  3 2007 lars@linux-schulserver.de
- deleted wrong suse_version macro in desktop file creation
  fixes OSE #0000001
- updated to 0.7r1780 which some small functions and testfile more
* Mon Aug 13 2007 lars@linux-schulserver.de
- update to 0.7r1777
- desktop file added
- enable unicode
- enable filters
- disable svnversion
- build devel package
- compile against wxGTK 2.6 (see bugzilla.xara.com #2496)
* Wed Feb 14 2007 jw@suse.de
- %%install and %%files section completed.
  Online Documentation files unpacked.
  Renamed xara to XaraLX.
* Fri Feb  9 2007 jw@suse.de
- initial check in of XaraLX 0.7r1766
  working around inconsistent libxml headers.
