Name:           razercfg
Version:        0.42
Release:        1
Summary:        A Razer device configuration tool
# Icons are http://creativecommons.org/licenses/by/4.0/
License:        GPLv2
Group:          Applications/System
URL:            http://bues.ch/cms/hacking/razercfg.html
Source0:        http://bues.ch/razercfg/%{name}-%{version}.tar.xz
# Upstream provides none of the following files
Source1:        razercfg.appdata.xml
BuildRequires:  cmake >= 2.4
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  libusb-devel
BuildRequires:  libappstream-glib
BuildRequires:  python3-qt4
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  python3-devel
BuildRequires:  systemd-devel
BuildRequires:  desktop-file-utils

%description
Razercfg is the next generation Razer device configuration
tool bringing the Razer gaming experience to the free Open Source world.
Including commandline tool (razercfg) and QT GUI qrazercfg.

%prep
%setup -q
sed -i 's|DESTINATION lib|DESTINATION lib${LIB_SUFFIX}|' librazer/CMakeLists.txt

%build
%cmake .
%make_build %{?_smp_mflags} -C %{_host}

%install
%make_install DESTDIR=%{buildroot} -C %{_host}
rm %{buildroot}%{_libdir}/librazer.so
# Systemd service and udev rule
#install -D -m 444 razerd.service %{buildroot}%{_unitdir}/razerd.service
#install -D -m 444 udev.rules %{buildroot}%{_udevrulesdir}/80-razer.rules
# install man pages
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N ./ui/razercfg > %{buildroot}%{_mandir}/man1/razercfg.1
# Note that the following line breaks if razercfg is actually installed
help2man -N -n "Use specific profiles per game" ./ui/razer-gamewrapper > \
%{buildroot}%{_mandir}/man1/razer-gamewrapper.1
#LD_LIBRARY_PATH=./librazer/ help2man -N ./razerd/razerd > \
#%{buildroot}%{_mandir}/man1/razerd.1
# install appdata file
install -Dpm 0644 %{SOURCE1} \
%{buildroot}%{_datadir}/appdata/razercfg.appdata.xml
appstream-util validate-relax --nonet \
%{buildroot}%{_datadir}/appdata/razercfg.appdata.xml
# Set icon for desktop file
desktop-file-edit --set-icon=razercfg \
%{buildroot}%{_datadir}/applications/razercfg.desktop

%check
ctest -V %{?_smp_mflags}

%post
# By default, Fedora services are not enabled and started
# Policy is to configure services with  Presets. But razerd
# is quite useless for the user if not started...
#%systemd_post razerd.service
systemctl enable razerd.service
systemctl start razerd.service
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
udevadm control --reload-rules 2>&1 > /dev/null || :
ldconfig

%preun
%systemd_preun razerd.service

%postun
%systemd_postun_with_restart razerd.service
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
udevadm control --reload-rules 2>&1 > /dev/null || :
ldconfig

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc HACKING.md README.md COPYING ui/icons/LICENSE
%{_bindir}/*
%{_datadir}/applications/razercfg.desktop
%{_datadir}/appdata/razercfg.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/razercfg*.svg
%{_unitdir}/razerd.service
%{_libdir}/librazer.so.1
%{_sysconfdir}/pm/sleep.d/50-razer
%{_udevrulesdir}/*.rules
%{_mandir}/man1/razer*
%{python3_sitelib}/*
/usr/lib/tmpfiles.d/razerd.conf

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.42
- Rebuild for Fedora
* Sun Nov 20 2016 Johan Heikkilä <johan.heikkila@gmail.com> 0.38
- Updated for latest version and Fedora 24
* Sun Oct 16 2016 Johan Heikkilä <johan.heikkila@gmail.com> 0.37
- Updated for latest version and Fedora 24
* Tue May 17 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.32
- Rebuild for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 0.22-3.mga5
+ Revision: 747083
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.22-2.mga5
+ Revision: 688620
- Mageia 5 Mass Rebuild
* Sun Feb 16 2014 dams <dams> 0.22-1.mga5
+ Revision: 592569
- new version 0.22
* Fri Oct 18 2013 umeabot <umeabot> 0.19-5.mga4
+ Revision: 521578
- Mageia 4 Mass Rebuild
* Wed Jan 23 2013 fwang <fwang> 0.19-4.mga3
+ Revision: 391313
- update rpm group
* Wed Jan 16 2013 fwang <fwang> 0.19-3.mga3
+ Revision: 388470
- correct udev rules dir
  + umeabot <umeabot>
    - Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Oct 17 2012 shlomif <shlomif> 0.19-1.mga3
+ Revision: 307632
- New version 0.19
* Mon Aug 27 2012 fedya <fedya> 0.18-1.mga3
+ Revision: 284614
- mkrel 1 added
- OpenSource it's mispelling
- rpmlint fixes
- imported package razercfg
