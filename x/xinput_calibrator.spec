Name:           xinput_calibrator
Version:        0.7.5
Release:        20
Summary:        A generic touchscreen calibration program for X.Org
Summary(fr):    Programme de calibrage d'écran tactile générique pour X.Org
License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/xinput_calibrator
Source0:        http://github.com/downloads/tias/xinput_calibrator/xinput_calibrator-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libXtst-devel
BuildRequires:  gtk2-devel

%description
xinput_calibrator is a program for calibrating your touchscreen, when using
the X Window System.
It currently features:
 - works for any standard Xorg touchscreen driver (uses XInput protocol)
 - mis-click detection (prevents bogus calibration)
 - dynamically recalibrates the evdev driver
 - outputs the calibration as xorg.conf.d snippet or HAL policy file
 - and more

%description -l fr
xinput_calibrator est un programme pour calibrer votre écran tactile, quand
le système X Window est utilisé.
Il propose actuellement:
 - fonctionnement sur n'importe quel pilote Xorg d'écran tactile standard
 (utilise le protocole XInput)
 - détection des faux-clics (prévient les calibrations boguées)
 - recalibre dynamiquement le pilote evdev
 - fragmente les sorties de calibration pour xorg.conf.d ou fichier de règle
 HAL
 - et plus encore

%prep
%setup -q

%build
%configure --with-gui=gtkmm \
           --with-gui=x11
make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR=%{buildroot}
# Install xinput_calibrator.desktop :
desktop-file-install                       \
--dir=%{buildroot}%{_datadir}/applications \
./scripts/%{name}.desktop

%files
%doc README COPYING Changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Thu Jan 21 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.5
- Rebuild for Fedora
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.5-11
- Rebuilt for GCC 5 C++11 ABI change
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Aug 16 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 0.7.5-6
- Add French translation in spec file
- Remove Group tag in spec file
- Fix manfile extention in %%files section
* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for c++ ABI breakage
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Wed Nov 04 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 0.7.5-2
- minor cleanup spec file
* Tue Oct 25 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 0.7.5-1
- initial RPM
