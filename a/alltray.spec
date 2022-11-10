Name:           alltray
Version:        0.7.6dev
Release:        0
Summary:        Dock any application in the tray
License:        GPLv2+
URL:            https://github.com/bill-auger/alltray
#Source0:        https://launchpad.net/alltray/old-maintenance/%{version}/+download/%{name}-%{version}.tar.gz
Source0:	%{name}-master.zip
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  GConf2-devel
BuildRequires:  gdk-pixbuf2-xlib-devel

%description
With AllTray you can dock any application without a native tray icon into the
system tray. It works well with GNOME, KDE, XFCE 4, Fluxbox, and WindowMaker.

%prep
%setup -q -n %{name}-master

%build
export CFLAGS="-Wl,--allow-multiple-definition -fPIC $RPM_OPT_FLAGS"
#configure
./autogen.sh --prefix=/usr
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
#rm $RPM_BUILD_ROOT%{_libdir}/*.so
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category Application \
  --add-category Utility \
  --add-category GTK \
  --delete-original \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}*
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/%{name}.1*
#{_libdir}/liballtray.so*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/alltray.mo

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.6dev
- Rebuilt for Fedora
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.71b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.71b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.71b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.71b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.71b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Fri Mar 20 2015 Richard Hughes <richard@hughsie.com> - 0.71b-9
- Rebuilt for gdk-pixbuf2-xlib split
* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.71b-5
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- update url and sourceurl to new websites
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.71b-2
- Rebuild for new libpng
* Mon Mar 28 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.71b-1
- New upstream release
- Update spec to match current guidelines
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Thu Aug 12 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 0.71a-1
- New upstream
* Tue Feb 16 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 0.70-5
- Fix rhbz #564621: ImplicitDSOLinking 
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.70-2
- Autorebuild for GCC 4.3
* Sun Dec 30 2007 Denis Leroy <denis@poolshark.org> - 0.70-1
- Update to upstream 0.70
* Fri Aug 17 2007 Denis Leroy <denis@poolshark.org> - 0.69-3
- Fixed License tag
* Mon Sep  4 2006 Denis Leroy <denis@poolshark.org> - 0.69-2
- Reenabled dynamic library for X funcs preload, added ldconfig
* Mon Sep  4 2006 Denis Leroy <denis@poolshark.org> - 0.69-1
- Update to 0.69
* Wed Apr 26 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.66-1
- Upstream update
* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.65-2
- Rebuilt for Fedora Extras 5
* Thu Jan 27 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.65-1
- Added -fPIC to CFLAGS
- Added preload patch
- Initial RPM release
