Name:           finalcut
Version:        0.8.0
Release:        1
Summary:        Console widget library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/gansm/finalcut/
Source:         https://github.com/gansm/finalcut/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++ >= 5.1
BuildRequires:  gdb
BuildRequires:  glib2-devel
BuildRequires:  gpm-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel

%description
FINAL CUT is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%package devel
Summary:        Development files for the FINAL CUT text widget library
Group:          Development/Libraries/C and C++
Requires:       bdftopcf
Requires:       coreutils
Requires:       gcc-c++ >= 5.1
Requires:       gpm-devel
Requires:       grep
Requires:       gzip
Requires:       %{name} = %{version}
Requires:       ncurses-devel
Requires:       sed
Requires:       vim
Provides:       libfinal-devel = %{version}

%description devel
FINAL CUT is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%package bitmap-fonts
Summary:        X11 bitmap font for FINAL CUT
Group:          System/X11/Fonts
Requires(pre):  fontconfig
# install the fonts only if we have X11 fonts anyways
BuildArch:      noarch

%description bitmap-fonts
Special X11 bitmap font used by FINAL CUT to display graphic objects.

%prep
%setup -q

%build
autoreconf -vif
export CPPFLAGS="%{optflags} -Wall -Wextra -Wpedantic"
%ifnarch %ix86 x86_64
export CPPFLAGS="$CPPFLAGS -Wno-error=unused-parameter"
%endif
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%global _miscfontsdir %{_datadir}/fonts
make install libdir=%{buildroot}%{_libdir}/ \
             includedir=%{buildroot}%{_includedir} \
             bindir=%{buildroot}%{_bindir} \
             docdir=%{buildroot}%{_docdir}/%{name}/ \
             fontdir=%{buildroot}%{_miscfontsdir}/%{name}/
mkdir -p %{buildroot}%{_miscfontsdir}/%{name}/
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}/examples
mkdir -p %{buildroot}/etc/fonts/conf.d
mkdir -p %{buildroot}/usr/share/fontconfig/conf.avail
cp -p examples/.libs/* %{buildroot}%{_libdir}/%{name}/examples
cp -p examples/*.cpp %{buildroot}%{_libdir}/%{name}/examples
cp -p examples/Makefile.clang %{buildroot}%{_libdir}/%{name}/examples
cp -p examples/Makefile.gcc %{buildroot}%{_libdir}/%{name}/examples
cp -p final/font/40-finalcut-newfont.conf %{buildroot}/usr/share/fontconfig/conf.avail
ln -s /usr/share/fontconfig/conf.avail/40-finalcut-newfont.conf %{buildroot}/etc/fonts/conf.d/40-finalcut-newfont.conf
rm -f %{buildroot}%{_libdir}/libfinal.la
rm %{buildroot}%{_docdir}/%{name}/ChangeLog %{buildroot}%{_docdir}/%{name}/COPYING.LESSER
# Add config for X font path
mkdir -p %{buildroot}%{_datadir}/X11/xorg.conf.d
cat <<EOF > %{buildroot}%{_datadir}/X11/xorg.conf.d/80-finalcut-bitmap-fonts.conf
Section "Files"
    FontPath "%{_miscfontsdir}/finalcut:unscaled"
EndSection
EOF
# make sure we own all generated files
for i in .fonts-config-timestamp encodings.dir fonts.dir fonts.scale; do
    > %{buildroot}%{_miscfontsdir}/finalcut/$i
done

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%reconfigure_fonts_scriptlets -n %{name}-bitmap-fonts

%files
%license COPYING.LESSER
%doc ChangeLog README.md
%{_libdir}/libfinal.so.*

%files devel
%{_docdir}/%{name}
%{_libdir}/libfinal.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/final
%{_libdir}/%{name}

%files bitmap-fonts
%dir %{_miscfontsdir}
%dir %{_miscfontsdir}/finalcut
%{_miscfontsdir}/finalcut/*.gz
%{_miscfontsdir}/finalcut/fonts.alias
%ghost %{_miscfontsdir}/finalcut/fonts.dir
%ghost %{_miscfontsdir}/finalcut/fonts.scale
%ghost %{_miscfontsdir}/finalcut/encodings.dir
%ghost %{_miscfontsdir}/finalcut/.fonts-config-timestamp
%dir /etc/fonts/conf.d/
%dir /usr/share/fontconfig/conf.avail
%dir %{_datadir}/X11
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/80-finalcut-bitmap-fonts.conf
/etc/fonts/conf.d/40-finalcut-newfont.conf
/usr/share/fontconfig/conf.avail/40-finalcut-newfont.conf

%changelog
* Sun Jan 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuilt for Fedora
* Sun Oct 31 2021 Markus Gans <guru.mail@muenster.de>
- Release (version 0.8.0)
* Sat Nov 14 2020 Markus Gans <guru.mail@muenster.de>
- Release (version 0.7.1)
* Sat Nov  7 2020 Markus Gans <guru.mail@muenster.de>
- Release (version 0.7.0)
* Wed Oct 21 2020 Markus Gans <guru.mail@muenster.de>
- Release (version 0.6.1 pre-release 0.7.0)
- deleted patch
  - 0001-arm-glibc-2.30.patch (upstreamed)
* Mon Jan 20 2020 Ludwig Nussel <lnussel@suse.de>
- libfinal-devel needs to require ncurses-devel and gpm-devel as some header
  files include files from those
- install built examples so libfinal-examples can be tried directly
- add package for the special font
* Thu Oct 17 2019 Markus Gans <guru.mail@muenster.de>
- 0001-arm-glibc-2.30.patch: Fixes compilation error with arm architecture with glibc >= 2.30
* Tue Oct 15 2019 Markus Gans <guru.mail@muenster.de>
- Release (version 0.6.0)
* Sat Dec  1 2018 Markus Gans <guru.mail@muenster.de>
- Release (version 0.5.1)
* Wed Nov 28 2018 Markus Gans <guru.mail@muenster.de>
- Package name adjustment
* Tue Nov 27 2018 Luigi Baldoni <aloisio@gmx.com>
- Use correct package names in Requires.
* Tue Nov 27 2018 Jan Engelhardt <jengelh@inai.de>
- Fix summary containing just of the name. Edit RPM groups.
* Mon Nov 26 2018 aloisio@gmx.com
- Install examples into docdir
- Add libfinal-devel = %%{version} to devel package
* Mon Nov 26 2018 mvetter@suse.com
- Prepare to push to devel project
- Remove old tarball: finalcut-0.3.0.tar.gz
- Remove old tarball: finalcut-0.4.0.tar.gz
- Clean spec with spec-cleaner
- Add changes file
* Sun Nov 25 2018 Markus Gans <guru.mail@muenster.de>
- Release (version 0.5.0)
* Sat Nov  4 2017 Markus Gans <guru.mail@muenster.de>
- Release (version 0.4.0)
* Sun Nov 27 2016 Markus Gans <guru.mail@muenster.de>
- Release (version 0.3.0)
* Sat Dec 19 2015 Markus Gans <guru.mail@muenster.de>
- Release (version 0.2.0)
* Fri Sep 18 2015 Markus Gans <guru.mail@muenster.de>
- Initial Release (version 0.1.1)
