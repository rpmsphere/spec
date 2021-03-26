%global debug_package %{nil}

Name:           gnome-pie
Version:        0.7.2
Release:        1
Summary:        A visual application launcher for Gnome
License:        MIT
URL:            http://%{name}.simonschneegans.de/
Source0:        https://codeload.github.com/Schneegans/Gnome-Pie/tar.gz/v%{version}#/Gnome-Pie-%{version}.tar.gz
BuildRequires:  vala-devel
BuildRequires:  bamf-devel
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(gee-1.0)
BuildRequires:  libxml2-devel
BuildRequires:  gtk3-devel
BuildRequires:  cmake
BuildRequires:  unique3-devel
BuildRequires:  libgee-devel
BuildRequires:  libXtst-devel
BuildRequires:  gnome-menus-devel
BuildRequires:  desktop-file-utils      

%description
Gnome-Pie is a circular application launcher for Linux. It is made of
several pies, each consisting of multiple slices. The user presses a 
key stroke which opens the desired pie. By activating one of its slices,
applications may be launched, key presses may be simulated or files can 
be opened.

%prep
%setup -q -n Gnome-Pie-%{version}
sed -i 's|public Action|Action|' src/actions/action.vala

%build
#cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_LDFLAGS=-lgthread
#make CFLAGS='%{optflags}' %{?_smp_mflags}
%cmake .
%make_build

%install
%make_install
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc AUTHORS COPYING TRANSLATING README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/%{name}.1.*
%{_datadir}/locale/zanata.xml

%changelog
* Thu Oct 17 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.2
- Rebuild for Fedora
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-9.20130330git0a5aa2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8.20130330git0a5aa2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-7.20130330git0a5aa2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-6.20130330git0a5aa2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Thu Jun 12 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.5-5.20130330git0a5aa2
- Fix BuildRequires (#1106682)
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-4.20130330git0a5aa2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Tue Aug 13 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.5.5-3.20130330git0a5aa2
- Fixed doc section 
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2.20130330git0a5aa2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Sat Apr 06 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.5.5-1.20130330git0a5aa2
- New version release, which have major fixes 
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3.20120826git1b93e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Sep 06 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.5.3-2.20120826git1b93e1
- Added Debug info package 
* Sun Aug 26 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.5.3-1.20120826git1b93e1
- Added latest version of gnome-pie
* Sat Oct 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.2-1
- Initial version of the package
