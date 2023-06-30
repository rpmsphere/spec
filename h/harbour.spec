Summary: A multiplatform Clipper language compiler
Name: harbour
Version: 4.3.2
Release: 1
License: GPLv2+
Group: Development/Languages
URL: https://github.com/hernad/harbour
#URL: https://www.harbour-project.org/
Source0: harbour-%{version}.tar.gz
BuildRequires: zlib-devel, pcre-devel, gpm-devel
BuildRequires: slang-devel, ncurses-devel, libX11-devel
BuildRequires: qt4-devel, qt4-webkit-devel
BuildRequires: openssl-devel, mysql-devel, libpq-devel
BuildRequires: unixODBC-devel, firebird-devel, file-devel, gd-devel
BuildRequires: freeimage-devel, libcurl-devel, cups-devel, cairo-devel
BuildRequires: allegro-devel
BuildRequires: bzip2-devel, expat-devel
BuildRequires: ghostscript-devel
BuildRequires: lzo-devel
Requires: gpm-devel

%description
The Harbour Project is a Free Open Source Software effort to build a
multiplatform Clipper language compiler. Harbour consists of the xBase
language compiler and the runtime libraries with different terminal
plugins and different databases (not just DBF).

%package libs
Summary: Libraries for Harbour applications
Group: System Environment/Libraries

%description libs
Runtime libraries needed for Harbour applications.

%prep
%setup -q
%if 0
perl -pi -e's,(LIBS = hbcplr hbpp hbcommon) ,$1 m ,' utils/hbrun/Makefile utils/hbmk2/Makefile
echo -e "\n{unix}libpaths=%{_libdir}/mysql" >> contrib/hbmysql/hbmysql.hbc
echo -e "\n{unix}libpaths=%{_libdir}/mysql" >> contrib/sddmy/sddmy.hbc
perl -pi -e's,-quiet,-info,' contrib/make.hbs
perl -pi -e's,{!darwin},{!darwin&!win},' contrib/hbqt/hbqt_common.hbm \
  contrib/hbqt/qtwebkit/hbqtwebkit.hbm
perl -pi -e's,libs=png,libs=png14,' contrib/hbwin/hbwin.hbc
perl -pi -e's,(-depincpath=png:/usr/include),#$1,' contrib/hbwin/hbwin.hbp
perl -pi -e's,(-depincpath=png:/usr/include),#$1,' contrib/hbhpdf/3rd/libhpdf/libhpdf.hbp
#sed -i 's| abs(| fabs(|' contrib/hbqt/qtgui/hbqt_hbqgraphicsscene.cpp
%endif
sed -i '/define HAVE_SYS_SYSCTL_H/d' src/rtl/arc4.c

%build
%if 0
qt_prefix=`pkg-config --variable=exec_prefix QtCore` || :
if [ "$qt_prefix" = "" ]; then
  qt_prefix=`ls -d %{_libdir}/qt4* 2>/dev/null | tail -n 1`
fi

if ! echo ${PATH} | /bin/grep -q $qt_prefix/bin ; then
   PATH=$qt_prefix/bin:${PATH}
fi
%endif
make \
     HB_BUILD_VERBOSE=yes \
     HB_INSTALL_PREFIX=%{_prefix} \
     HB_BUILD_PKG=yes \
     HB_USER_CFLAGS="%{optflags} -I%{_includedir} -DHB_USE_BSDLOCKS_OFF" \
#     HB_USER_LDFLAGS="-L%{_libdir}/mysql" \
     HB_BUILD_SHARED=yes \
     HB_BUILD_CONTRIB=yes HB_BUILD_CONTRIB_DYN=yes \
     HB_QTPOSTFIX=-qt4

%install
make install \
     HB_INSTALL_PKG_ROOT=$RPM_BUILD_ROOT \
     HB_INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} \
     HB_INSTALL_INC=$RPM_BUILD_ROOT%{_includedir}/harbour \
     HB_INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir}/harbour \
     HB_INSTALL_DYN=$RPM_BUILD_ROOT%{_libdir}/harbour \
     HB_INSTALL_ETC=$RPM_BUILD_ROOT%{_sysconfdir}/harbour \
     HB_INSTALL_MAN=$RPM_BUILD_ROOT%{_mandir} \
     HB_INSTALL_DOC=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
     \
     HB_BUILD_VERBOSE=yes \
     HB_INSTALL_PREFIX=%{_prefix} \
     HB_BUILD_PKG=yes \
     HB_USER_CFLAGS="%{optflags} -I%{_includedir}" \
#     HB_USER_LDFLAGS="-L%{_libdir}/mysql" \
     HB_BUILD_SHARED=yes \
     HB_BUILD_CONTRIB=yes HB_BUILD_CONTRIB_DYN=yes \
     HB_QTPOSTFIX=-qt4
chmod +x %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_docdir}/%{name}-%{version}
%{_bindir}/*
%{_mandir}/man1/harbour.1*
%{_mandir}/man1/hbpp.1*
%{_includedir}/harbour
%dir %{_libdir}/harbour
%dir %{_sysconfdir}/harbour
#%config(noreplace) %{_sysconfdir}/harbour/hb-charmap.def

%files libs
%{_libdir}/harbour
#%{_libdir}/libharbour.so*
%config %{_sysconfdir}/ld.so.conf.d/harbour.conf

%changelog
* Thu Dec 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3.2
- Rebuilt for Fedora
* Sun Aug  7 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 3.0.0-11
- Update to 3.0.0.
* Thu Jan 20 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.1.0-9_beta3
- Update to beta3.
* Sat Nov 27 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.1.0-1_beta2
- Initial build.
