Name:           q
Version:        7.11
Release:        46
Summary:        Equational programming language
License:        GPLv2+
Source:         http://ovh.dl.sourceforge.net/sourceforge/q-lang/q-%{version}.tar.gz
URL:            http://q-lang.sourceforge.net
BuildRequires:  make
BuildRequires:  GraphicsMagick-devel, bison, curl-devel, dx-devel
BuildRequires:  flex, freetype-devel, gdbm-devel, gmp-devel
BuildRequires:  libxml2-devel, libxslt-devel, ncurses-devel
BuildRequires:  readline-devel, tcl-devel, tk-devel, unixODBC-devel
BuildRequires:  which, zlib-devel, libtool-ltdl-devel, automake
BuildRequires:  autoconf, libtool, gettext-devel
# bz#1037264. Upstream support discontinued according to offsite, so nothing send - just add patch in Fedora.
Patch0: q-7.11-format-security.patch
# bz#1106959
Patch1: q-7.11-tcl86.patch
Patch2: q-7.11-configure.patch

%description
Q is a powerful and extensible functional programming language based
on the term rewriting calculus. You specify an arbitrary system of
equations which the interpreter uses as rewrite rules to reduce
expressions to normal form. Q is useful for scientific programming and
other advanced applications, and also as a sophisticated kind of
desktop calculator. The distribution includes the Q programming tools,
a standard library, add-on modules for interfacing to Curl, GNU dbm,
ODBC, GNU Octave, ImageMagick, Tcl/Tk, XML/XSLT and an Emacs mode.

%package dx
Summary:        DX module for Q
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description dx
%{summary}.

%package curl
Summary:        cURL module for Q
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description curl
%{summary}.

%package magick
Summary:        ImageMagick module for Q
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description magick
%{summary}.

%package tk
Summary:        Tk module for Q
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tk
%{summary}.

%package devel
Summary:        Headers and static library for developing programs using Q
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libtool

%description devel
%{summary}.

%prep
%setup -q
%patch 0 -p0 -b .format-security
%patch 1 -p1 -b .tcl86
%patch 2 -p1 -b .configure
sed -i 's|@libtool@|libtool|' src/Makefile.in

rm -fr libltdl* libtool
./autogen.sh

# We do not want any provides for the Q modules.
%{?filter_setup:
%filter_provides_in %{_libdir}/q/.*\.so$
%filter_setup
}

sed -i '1221s|, &exception||' modules/magick/magick.c

%build
%configure --with-unicode --with-rl="-lreadline -lncurses" --with-dxl="-lDX -lDXL" --with-magick="`pkg-config GraphicsMagick --libs`" --with-magick-includes="`pkg-config GraphicsMagick --cflags`"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# %{?_smp_mflags} breaks the build
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/q/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mkdir -p _docs_staging
mv $RPM_BUILD_ROOT%{_datadir}/q/etc _docs_staging
mv $RPM_BUILD_ROOT%{_datadir}/q/examples _docs_staging

%files
%{_bindir}/q
%{_bindir}/qc
%{_infodir}/*
%{_libdir}/lib*.so.*
%{_libdir}/q
%{_mandir}/man*/*
%{_datadir}/q
%doc _docs_staging/*
%exclude %{_libdir}/q/dxl.so
%exclude %{_datadir}/q/lib/dxl.q
%exclude %{_libdir}/q/curl.so
%exclude %{_datadir}/q/lib/curl.q
%exclude %{_libdir}/q/magick.so
%exclude %{_datadir}/q/lib/magick.q
%exclude %{_libdir}/q/tk.so
%exclude %{_datadir}/q/lib/tk.q

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_bindir}/qcc
%{_bindir}/qld

%files dx
%{_libdir}/q/dxl.so
%{_datadir}/q/lib/dxl.q

%files curl
%{_libdir}/q/curl.so
%{_datadir}/q/lib/curl.q

%files magick
%{_libdir}/q/magick.so
%{_datadir}/q/lib/magick.q

%files tk
%{_libdir}/q/tk.so
%{_datadir}/q/lib/tk.q

%changelog
* Sun Nov 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 7.11
- Rebuilt for Fedora
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
* Sun Oct 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.11-44
- Rebuild against new ImageMagick
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 7.11-39
- Fix configure tests compromised by LTO
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.11-37
- Rebuild for readline 8.0
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 7.11-35
- Rebuilt for libcrypt.so.2 (#1666033)
* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 7.11-34
- Rebuild for ImageMagick 6.9.10
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 7.11-31
- Rebuilt for switch to libxcrypt
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Mon Jul 31 2017 Kevin Fenzi <kevin@scrye.com> - 7.11-29
- Rebuild for new ImageMagick
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 7.11-27
- Rebuild due to bug in RPM (RHBZ #1468476)
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 7.11-25
- Rebuild for readline 7.x
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Tue Jun 24 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 7.11-21
- Fix FTBFS with tcl-8.6 (#1106959)
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 7.11-19
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86
* Sun Apr 13 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 7.11-18
- ImageMagick 6.8.8.10-3 rebuild.
- Add Patch0: q-7.11-format-security.patch to fix FBFS due to -Wformat-security (bz#1037264).
* Fri Aug  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 7.11-17
- Use special %%doc to install docs.
* Sat Mar 30 2013 Kevin Fenzi <kevin@scrye.com> - 7.11-16
- Rebuild for broken deps in rawhide
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Apr 13 2012 Tom Callaway <spot@fedoraproject.org> - 7.11-13
- use new filtering macros
- rebuild for new ImageMagick
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-12.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-11.2
- Rebuilt for glibc bug#747377
* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 7.11-10.2
- rebuild with new gmp without compat lib
* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 7.11-10.1
- rebuild with new gmp
* Tue Feb 22 2011 Gérard Milmeister <gemi@bluewin.ch> - 7.11-10
- Rebuild against system libltdl
* Fri Sep 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 7.11-7.1
- rebuild (ImageMagick)
* Mon May 24 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.11-7
- disable rpath
- rebuild for non-static libxslt
* Wed Mar 24 2010 Mike McGrath <mmcgrath@redhat.com> - 7.11-6.1
- Rebuilt for broken dep
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Mar 18 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 7.11-5
- Comment-out the AcquireOnePixel patch, appears to be no longer necessary for 
  new ImageMagick-6.4.9 (#490874)
* Thu Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 7.11-4
- adapt AcquireOnePixel usage for current ImageMagick api
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Tue Aug  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 7.11-2
- new release 7.11
- split some modules into separate packages
* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 7.10-3
- Autorebuild for GCC 4.3
* Sat Jan  5 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 7.10-2
- Rebuild for new Tcl 8.5
* Sun Dec 30 2007 Gerard Milmeister <gemi@bluewin.ch> - 7.10-1
- new release 7.10
* Wed Oct 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 7.8-1
- new version 7.8
* Thu Feb 15 2007 Gerard Milmeister <gemi@bluewin.ch> - 7.6-2
- use ncurses instead of termcap
* Sun Jan  7 2007 Gerard Milmeister <gemi@bluewin.ch> - 7.6-1
- new version 7.6
* Tue Oct 31 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.5-2
- patch for curl options
* Tue Oct 31 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.5-1
- new version 7.5
* Wed Aug 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.4-1
- new version 7.4
* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.1-3
- Rebuild for FE6
* Tue Jun 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.1-2
- disable provides for modules
* Mon Jun 12 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.1-1
- new version 7.1
- use system libtool
* Sun Jun 11 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.1-0.2.rc2
- removed %%{_infodir}/dir
- modified %%description
- built apache module
- removed gqbuilder until gnocl is available
* Sat Jun 10 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.1-0.1.rc2
- changed version scheme
* Thu Jun  8 2006 Gerard Milmeister <gemi@bluewin.ch> - 7.1-1
- new version 7.1rc2
* Sun Sep 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 6.2-1
- New Version 6.2
* Sun Mar  6 2005 Gerard Milmeister <gemi@bluewin.ch> - 6.0-1
- First Fedora release

