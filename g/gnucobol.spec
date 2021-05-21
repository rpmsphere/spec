%global debug_package %{nil}

Name:           gnucobol
Version:        3.0rc1
Release:        16.1
Summary:        A free and open COBOL compiler
License:        GPL-3.0+ and LGPL-3.0+
Group:          Development/Languages/Other
URL:            https://savannah.gnu.org/projects/gnucobol
Source0:        https://ftp.gnu.org/gnu/gnucobol/gnucobol-3.0-rc1.tar.xz
BuildRequires:  libdb-devel
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  texinfo
BuildRequires:  ncurses-devel
Requires:       libcob-devel
Obsoletes:      opencobol open-cobol
Provides:       gnu-cobol

%description
GNU Cobol (formerly OpenCOBOL) is a free COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%package -n libcob
Summary:        GNU COBOL shared library
License:        LGPL-3.0+
Group:          Development/Languages/Other

%description -n libcob
GNU Cobol (formerly OpenCOBOL) is a free COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%package -n libcob-devel
Summary:        Include files for GNU COBOL shared library
License:        LGPL-3.0+
Group:          Development/Languages/Other
Requires:       libcob = %{version}
Requires:       gmp-devel
Requires:       ncurses-devel

%description -n libcob-devel
GNU Cobol (formerly OpenCOBOL) is a free COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%prep
%setup -q -n gnucobol-3.0-rc1
sed -i -e 's|/-g//|/-g //|' -e 's|/-fstack-protector//|/-fstack-protector //|' configure
sed -i '18568,18569d' configure
find .  -name '*.[ch]' |\
    xargs sed -i "s/__DATE__/\"Sep  7 2017\"/g;s/__TIME__/\"00:00\"/g"

%build
./configure --prefix=/usr --libdir=%{_libdir} --enable-static=no
make -j1

%install
%make_install
%find_lang gnucobol

%post -n libcob -p /sbin/ldconfig

%postun -n libcob -p /sbin/ldconfig

%files -f gnucobol.lang
%doc ABOUT-NLS AUTHORS COPYING COPYING.DOC ChangeLog NEWS README THANKS TODO
%{_bindir}/cob-config
%{_bindir}/cobc
%{_bindir}/cobcrun
%{_datadir}/gnucobol
%{_infodir}/gnucobol.info*
%exclude %{_infodir}/dir
%{_libdir}/gnucobol
%{_mandir}/man1/cobc.1*
%{_mandir}/man1/cobcrun.1*

%files -n libcob
%doc COPYING.LESSER
%{_libdir}/libcob.so.*

%files -n libcob-devel
%{_includedir}/libcob.h
%{_includedir}/libcob
%exclude %{_libdir}/libcob.la
%{_libdir}/libcob.so

%changelog
* Mon Oct 22 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0rc1
- Rebuilt for Fedora
* Thu Sep  7 19:42:36 UTC 2017 - aloisio@gmx.com
- Update to version 2.2 (see NEWS or ChangeLog)
- Switched license to GPL-3.0+/LGPL-3.0+
- Updated source URL and homepage on account of being accepted
  into the GNU Project
- Added gnucobol-CFLAGS.patch
- Dropped types.diff (apparently no longer necessary)
* Mon Apr  6 15:00:39 UTC 2015 - mpluskal@suse.com
- Cleanup spec file with spec-cleaner
- Use url for source
- Update info dependencies
- Use macro for locale handling
- Do not create static library
* Wed Jul 16 16:32:55 UTC 2014 - dvlaeev@suse.com
- Fix SLE11 builds by defining buildroot
* Wed Apr 30 00:00:00 UTC 2014 - MihailJP
- First packaging
