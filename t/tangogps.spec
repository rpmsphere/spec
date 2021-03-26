Name:          tangogps
Version:       0.99.4
Release:       1
Summary:       GTK+ mapping and GPS application
Group:         Applications/Productivity
License:       GPLv2
URL:           http://www.tangogps.org/
Source0:       http://www.tangogps.org/downloads/%{name}-%{version}.tar.gz
Source1:       tangogps.desktop
Source2:       %{name}-0.99.4.zh_TW.po
Patch0:        tangogps-fixdso.patch
BuildRequires: bluez-libs-devel
BuildRequires: dbus-devel
BuildRequires: gtk2-devel
BuildRequires: GConf2-devel
BuildRequires: libcurl-devel
BuildRequires: libexif-devel
BuildRequires: libsoup-devel
BuildRequires: libxml2-devel
BuildRequires: sqlite-devel
BuildRequires: gettext
BuildRequires: desktop-file-utils
Requires: dbus
Requires: gpsd
Requires: gpscorrelate
Requires: jhead

%description
tangoGPS is a lightweight and fast mapping application. It runs on handheld 
devices like the Openmoko Neo1973 as well as on the eeePC and the Linux 
desktop. By default is uses map data from the OpenStreetMap.org project; 
additionally a variety of other repositories can easily be added.

%prep
%setup -q

%patch0 -p1 -b .fixdso
cp %{SOURCE2} po/zh_TW.po
sed -i 's/pl ru sk/pl ru sk zh_TW/' configure*
sed -i 's|curl/types.h|curl/curl.h|' src/*

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor="fedora" \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
rm -rf %{buildroot}%{_datadir}/applications/tangogps.desktop
rm -rf %{buildroot}/usr/doc/%{name}/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc COPYING 
%{_bindir}/tangogps
%{_datadir}/applications/fedora-tangogps.desktop
%{_datadir}/pixmaps/tangogps.png
%{_datadir}/pixmaps/tangogps-*.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.99.4
- Rebuild for Fedora
* Fri Jun 25 2010 Peter Robinson <pbrobinson@gmail.com> 0.99.4-2
- Add new deps
* Fri Jun 25 2010 Peter Robinson <pbrobinson@gmail.com> 0.99.4-1
- New upstream 0.99.4 release
* Sat Apr 17 2010 Peter Robinson <pbrobinson@gmail.com> 0.99.3-3
- Add jhead and gpscorrelate deps to fix photo geotagging
* Mon Feb 15 2010 Peter Robinson <pbrobinson@gmail.com> 0.99.3-2
- Add patch to fix DSO linking. Fixes bug 565166
* Mon Feb 15 2010 Peter Robinson <pbrobinson@gmail.com> 0.99.3-1
- New upstream 0.99.3 release
* Thu Dec  3 2009 Peter Robinson <pbrobinson@gmail.com> 0.99.2-1
- New upstream 0.99.2 release
* Mon Nov 30 2009 Peter Robinson <pbrobinson@gmail.com> 0.99.1-1
- New upstream 0.99.1 release
* Thu Nov  5 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.9-1
- New upstream 0.9.9 release
* Sun Nov  1 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.8-1
- New upstream 0.9.8 release
* Tue Sep 22 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.7-1
- New upstream 0.9.7 release
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Thu Feb 5  2009 Peter Robinson <pbrobinson@gmail.com> 0.9.6-2
- Add BR: libexif-devel to support new photo geotagging
* Thu Feb 5  2009 Peter Robinson <pbrobinson@gmail.com> 0.9.6-1
- New upstream release
* Mon Jan 19 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.5-1
- New upstream release
* Mon Sep 1 2008 Peter Robinson <pbrobinson@gmail.com> 0.9.3-3
- Cleanups from package review
* Fri Aug 29 2008 Peter Robinson <pbrobinson@gmail.com> 0.9.3-2
- Spec fixes
* Tue Aug 26 2008 Peter Robinson <pbrobinson@gmail.com> 0.9.3-1
- New release
* Mon Jul 7 2008 Peter Robinson <pbrobinson@gmail.com> 0.9.2-1
- Initial package
