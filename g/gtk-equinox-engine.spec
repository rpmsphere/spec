%global engine equinox
%global tarname 121881-%{engine}
%global tarver 1.50
%global tarthemes 140449-%{engine}-themes

Name:           gtk-equinox-engine
Version:        1.50
Release:        16.1
Summary:        Equinox theme engine for GTK+ 2.x
Group:          System Environment/Libraries
License:        GPLv2+
URL:            https://gnome-look.org/content/show.php/Equinox+GTK+Engine?content=121881
Source0:        https://gnome-look.org/CONTENT/content-files/%{tarname}-%{tarver}.tar.gz
Source1:        https://gnome-look.org/CONTENT/content-files/%{tarthemes}-%{tarver}.tar.gz
Patch0:         gtk-equinox-engine-includefix.patch
BuildRequires:  gtk2-devel
Requires:       faience-icon-theme
Requires:       dmz-cursor-themes
Requires:       adayinthelife-backgrounds

%description
A new engine derived from Aurora 1.4. It features smooth gradients or glassy
effects, subtle shadows, rounded widgets.

%prep
%setup -q -n %{engine}-%{tarver}
%patch0 -p1

# Unpack gtk themes here
tar -xzf %{SOURCE1}

# Fix executable bits for debuginfo package
chmod 0644 src/*

%build
%configure --enable-animation
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Copy themes to proper directory
mkdir -p %{buildroot}%{_datadir}/themes
mkdir -p tmpdoc
mv *.crx tmpdoc
mv Equinox* %{buildroot}%{_datadir}/themes

# Remove .la files
find %{buildroot} -name *.la | xargs rm -f || true

# Fix executable bits for files in themes
chmod 0644 %{buildroot}%{_datadir}/themes/Equinox\ Evolution/README
chmod 0644 %{buildroot}%{_datadir}/themes/Equinox\ Evolution\ Dawn/index.theme
chmod 0644 %{buildroot}%{_datadir}/themes/Equinox\ Evolution\ Midnight/index.theme
chmod 0644 %{buildroot}%{_datadir}/themes/Equinox\ Evolution\ Midnight/README
chmod 0644 %{buildroot}%{_datadir}/themes/Equinox\ Evolution\ Midnight/gtk-2.0/apps/gnome-panel.rc
chmod 0644 %{buildroot}%{_datadir}/themes/Equinox\ Evolution\ Midnight/gtk-2.0/apps/google-chrome.rc
chmod 0644 %{buildroot}%{_datadir}/themes/Equinox\ Evolution\ Midnight/gtk-2.0/fixes/fixes.rc

# Fix executable bits for doc files
chmod 0644 AUTHORS ChangeLog COPYING README

sed -i -e 's|Faenza-Darkest|Faience-Claire|' -e 's|Faenza-Dark|Faience-Ocre|' -e 's|Faenza|Faience|' $RPM_BUILD_ROOT%{_datadir}/themes/Equinox*/index.theme
sed -i -e 's|DMZ-White|dmz|' -e 's|DMZ-Black|dmz-aa|' $RPM_BUILD_ROOT%{_datadir}/themes/Equinox*/index.theme
sed -i -e '$a BackgroundImage=/usr/share/backgrounds/aDayInThelife/default.xml' $RPM_BUILD_ROOT%{_datadir}/themes/Equinox*/index.theme

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING README tmpdoc/*
%{_libdir}/gtk-2.0/2.10.0/engines/libequinox.so
%{_datadir}/themes/Equinox*

%changelog
* Mon Feb 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.50
- Rebuilt for Fedora
* Mon Sep 09 2013 Germán A. Racca <skytux@fedoraproject.org> 1.50-8
- Added dependency on gnome-icon-theme again because faenza was retired (see BZ#1005176)
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Wed Dec 14 2011 Karsten Hopp <karsten@redhat.com> 1.50-3
- don't include glib/gtimer.h directly, use glib/glib.h instead
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.50-2
- Rebuild for new libpng
* Thu Aug 25 2011 Germán A. Racca <skytux@fedoraproject.org> 1.50-1
- Updated to new version
* Thu Apr 20 2011 Germán A. Racca <skytux@fedoraproject.org> 1.40-1
- Updated to new version
- Removed old gtk themes and added new ones
- Added dependency on Faenza icons
* Mon Oct 04 2010 Germán A. Racca <skytux@fedoraproject.org> 1.30.2-1
- Updated to new version
- Defined some globals
* Fri Sep 03 2010 Germán A. Racca <skytux@fedoraproject.org> 1.30-1
- Updated to new version
- Icon name in Equinox Glass theme corrected by upstream
* Thu Aug 26 2010 Germán A. Racca <gracca@gmail.com> 1.20-4
- Removed dependency on gnome-icon-theme because faenza-icon-theme was released
- Fixed icon name in Equinox Glass theme
* Wed Jul 07 2010 German A. Racca <gracca@gmail.com> 1.20-3
- Fix permissions for debuginfo package
* Tue Jul 06 2010 German A. Racca <gracca@gmail.com> 1.20-2
- Fixed confused release number
- Removed %%BuildRoot tag
- Replaced Faenza icon theme by Gnome
- Added %%Requires tag
* Tue Jun 29 2010 German A. Racca <gracca@gmail.com> 1.20-1
- New version
* Tue Jun 01 2010 German A. Racca <gracca@gmail.com> 1.1-3
- Rebuilt for Fedora 13
- Added %%{dist} tag
* Thu May 13 2010 German A. Racca <gracca@gmail.com> 1.1-2
- Rearrangement of spec file
* Tue Apr 06 2010 German A. Racca <gracca@gmail.com> 1.1-1
- Initial release of RPM package
