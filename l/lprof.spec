Name:           lprof
BuildRequires:  libdrm-devel
BuildRequires:  lcms-devel
BuildRequires:  libtiff-devel
BuildRequires:  qt3-devel
BuildRequires:  scons
BuildRequires:  vigra-devel
BuildRequires:  atlas
Version:        1.11.4.1
Release:        7.1
URL:            https://lprof.sourceforge.net/
Summary:        ICC Profiler
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Source:         %{name}-%{version}.tar.bz2
Patch:          lprof-desktop.patch
Patch1:         lprof-lcms.patch
Patch2:         lprof-scons.patch
Patch3:         argyll-typo.patch

%description
LPROF is the only open source ICC profiler with a graphical user
interface. It can be used to create profiles for cameras, scanners, and
monitors, and fills a necessary niche in the emerging open source color
management effort.

Authors:
--------
    Hal Engel <hvengel@users.sourceforge.net>
    Marti Maria <marti@littlecms.com>

%prep
%setup -q
%patch
%patch1
%patch2
%patch3
sed -i /includehint/d */*/*.ui
(
  find -name SConstruct
  find -name SConscript
  echo lprof.pro build_config.py
  find -name Makefile
) | while read ; do
  sed -i "
s:/lib:/%_lib:g
s:\(os.path.join\|qtdir\)\(.*\)'lib':\1\2'%_lib':g
s:src/%_lib:src/lib:g
s:usr/%_lib/qt3:usr/lib/qt3:g
s/%{_lib}lprof/liblprof/g
s:%{_lib}qtlcmswidgets:libqtlcmswidgets:g
" $REPLY
done

%build
cat >lprof.conf <<EOF
PREFIX = '%{_prefix}'
ccflags = [$(echo $RPM_OPT_FLAGS | sed -e "s/[^ ]*/'&'/g" -e "s/ /,/g")]
cxxflags = [$(echo $RPM_OPT_FLAGS | sed -e "s/[^ ]*/'&'/g" -e "s/ /,/g")]
EOF
export QTDIR=%{_libdir}/qt-3.3
$QTDIR/bin/qmake
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/{applications,pixmaps}}
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 data/desktop/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 data/icons/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a data/pics data/profiles data/template $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING KNOWN_BUGS README sRGB_profile_License
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Feb 26 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11.4.1
- Rebuilt for Fedora
* Wed Jun 25 2014 pgajdos@suse.com
- buildrequire liblcms-devel
* Fri Mar  1 2013 cfarrell@suse.com
- license update: GPL-2.0+
  Package does not expose libraries under LGPL-2.1+ (if it did they should
  be build as a subpackage with an individual license). The package does
  contain scons with a MIT license but this is subsumed by the GPL-2.0
  license of the derived binary)
* Thu Feb 28 2013 coolo@suse.com
- update license to new format
* Thu Oct 30 2008 sbrabec@suse.cz
- Fixed typo in argyll (bnc#440145).
* Tue Oct 14 2008 sbrabec@suse.cz
- Fix build with the latest scons.
* Sun Nov  4 2007 ro@suse.de
- fix build with lcms 1.17
* Tue Nov  7 2006 ro@suse.de
- fix data file permissions
* Fri Oct 20 2006 sbrabec@suse.cz
- Updated to version 1.11.4.1:
  * Translation support.
  * Improved pick template placement code.
  * The proofing code has been improved.
  * Uses the ArgyllCMS spline regression code.
  * Dialogs have been reworked.
  * Detects these non-conforming profiles.
  * Perform cross validation on the regression model.
  * QT QSetting API.
  * CIE based weighting for color patches.
  * Expanded the the number of items that are actively tracked.
  * Uses VIGRA for all image file IO (no longer needs TiffIO).
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 23 2006 sbrabec@suse.cz
- Updated to version 1.11.2.
* Tue Jan 17 2006 sbrabec@suse.cz
- Updated to version 1.11.1.
* Fri Nov 25 2005 sbrabec@suse.cz
- New SuSE package, version 1.11.0.
