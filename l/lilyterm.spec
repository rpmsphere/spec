%undefine _debugsource_packages

Name:           lilyterm
Version:        0.9.9.4
Release:        20190725
Summary:        Light and easy to use X Terminal Emulator
License:        GPLv3+
URL:            https://github.com/Tetralet/LilyTerm
#Source0:        http://lilyterm.luna.com.tw/file/lilyterm-%{version}%{?prerelease:~%{?prerelease}}.tar.gz
Source0:	%{name}-master.zip
BuildRequires:  gcc
BuildRequires:  gtk2-devel >= 2.8.20
BuildRequires:  vte-devel >= 0.12.2
BuildRequires:  desktop-file-utils intltool
BuildRequires:  make

%description
LilyTerm is a light and easy to use libvte based X Terminal Emulator with a 
lot of features:
 * Supports multiple tabs, reorderable tabs and hides the tab tray when there 
   is only one tab
 * Add, close, swith, move, rename tabs with function keys
 * Disable/Enable function keys for temporary (use <Ctrl><`> by default).
 * Shows the foreground running command on tab and/or window title.
 * Change the font name, size, and window size with right click menu.
 * User custom function keys (need to edit profile).
 * Support for User/System profiles.
 * Supports true transparency if the window manager is composited.
 * Support for transparent background and background saturation.
 * Support for text and background color (need to edit profile).
 * Good support for UTF-8.
 * Decide the text encoding via environment. Using UTF-8 by default.
 * Change the text encoding with right click menu.


%prep
%setup -qn LilyTerm-master


%build
#export NOCONFIGURE=yes
#sh autogen.sh
%configure

# parallel make breaks with "Text file busy"
#make %{?_smp_mflags}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install                                       \
  --delete-original                                        \
  --remove-category=Utility                                \
  --add-category=System                                    \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications          \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
# we install the docfiles versioned
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/doc/lilyterm/



%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README TODO
%config(noreplace) %{_sysconfdir}/lilyterm.conf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/lilyterm.*
%{_mandir}/man*/%{name}.*.*


%changelog
* Thu Jan 9 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9.4
- Rebuilt for Fedora
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild
* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Thu Dec 19 2019 Tom Callaway <spot@fedoraproject.org> - 0.9.9.2-15
- fix FTBFS
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Sat Aug 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.9.2-1
- Update to 0.9.9.2
- Disable parallel make for now as it breaks
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-0.5.rc8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.9-0.4.rc8
- Rebuild for new libpng
* Thu Jun 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.9-0.3.rc8
- Completely disable GNOME control-center integration, it won't return (#715952)
* Wed Feb 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.9-0.2.rc8
- Temporarily disable GNOME control-center integration for 
  https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sat Jan 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.9-0.1.rc8
- Update to 0.9.9 RC8
* Wed Apr 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.8-1
- Update to 0.9.8
- License change from BSD to GPLv3+
- Require control-center-filesystem for gnome-default-applications integration
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Jun 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.6-2
- Rebuilt for libvte SONAME bump
* Sat Apr 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.6-1
- Update to 0.9.6
* Fri Jul 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.5-1
- Update to 0.9.5
* Thu Jul 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.4-1
- Update to 0.9.4
* Thu Jun 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3
* Mon May 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0
* Mon Apr 21 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.6-1
- Initial Fedora RPM
