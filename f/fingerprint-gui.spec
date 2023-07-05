%undefine _debugsource_packages

Name:           fingerprint-gui
Version:        1.09git
Release:        1
Summary:        Tool for fingerprint enrollment and verification
License:        GPL-2.0+
Group:          Hardware/Other
URL:            https://ullrich-online.cc/Appliance/fingerprint/
#Source0:        https://ullrich-online.cc/nview/Appliance/fingerprint/download/fingerprint-gui-%{version}.tar.gz
Source0:	%{name}-master.zip
Source1:        fingerprint-gui.svg
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libfakekey)
BuildRequires:  libfprint-devel
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(polkit-qt-1)
BuildRequires:  pkgconfig(qca2)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(udev)
BuildRequires:  hicolor-icon-theme
Requires:       xdg-utils

%description
Fingerprint GUI is a set of GUI tools for the use of fingerprint scanners on
Linux systems. It enables the recording and checking of fingerprints of users
and allows login and authentication of users by their fingerprint through its
PAM module. An additional "fingerprintIdentifier" application can be used for
customized (shell) scripts when users have to be identified or authenticated
by their fingerprints. The system is based on device drivers from the
"libfprint" project.

%prep
%setup -q -n %{name}-master

%build
export QTDIR=%{_libexecdir}/
qmake-qt5 QMAKE_CFLAGS="%{optflags}" QMAKE_CXXFLAGS="%{optflags}" PREFIX=%{_prefix} LIB=%{_lib} LIBEXEC=%{_lib}
#cmake -DCMAKE_PREFIX=/usr .
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

## install new icon and desktop file
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

cat > %{buildroot}%{_datadir}/applications/fingerprint-gui.desktop << EOF
[Desktop Entry]
Type=Application
Name=Fingerprint GUI
GenericName=Fingerprint Tool
GenericName[de]=Fingerabdruck Hilfsprogramm
GenericName[fr]=Outil pour les empreintes digitales
Comment=Tool for fingerprint enrollment and verification
Comment[de]=Hilfsprogramm zum Registrieren und Verifizieren der Fingerabdrücke
Comment[fr]=Outil pour enregistrer et vérifier les empreintes digitales
Icon=fingerprint-gui
Terminal=false
Exec=fingerprint-gui
Categories=System;Security;HardwareSettings;
EOF

mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/92-fingerprint-gui-uinput.rules %{buildroot}%{_udevrulesdir}/92-fingerprint-gui-uinput.rules

%files
%doc README CHANGELOG COPYING
%{_sysconfdir}/xdg/autostart/fingerprint-polkit-agent.desktop
/%{_lib}/security/pam_fingerprint-gui.so
%{_bindir}/fingerprint-gui
%{_bindir}/fingerprint-identifier
%{_libdir}/fingerprint-gui
%{_datadir}/applications/fingerprint-gui.desktop
%{_datadir}/icons/hicolor/*/apps/fingerprint-gui.png
%{_datadir}/pixmaps/fingerprint-gui.svg
%{_datadir}/pixmaps/fingerprint-gui.xpm
%{_datadir}/doc/fingerprint-gui
%{_mandir}/man1/fingerprint-gui.1.*
%{_mandir}/man1/fingerprint-identifier.1.*
%{_mandir}/man8/pam_fingerprint-gui.8.*
%{_udevrulesdir}//92-fingerprint-gui-uinput.rules
%{_datadir}/polkit-1/actions/cc.ullrich-online.fingerprint-gui.policy

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.09git
- Rebuilt for Fedora
* Sat Mar  5 2016 mailaender@opensuse.org
- fix license according to README
- add udev update rules
- update to 1.07
  * Bugfix: Fingerprint export doesn't handle well spaces in custom filename;
  * Security: Directory "/var/lib/fingerprint-gui" and all its subdirectories
    are now owned by root.root with mode 755. All files in these directories
    are also owned by root.root with mode 600 now. The helper module
    "fingerprint-suid" was replaced by a new module "fingerprint-rw" not set
    to suid root any more. This module is executed via "pkexec" for reading
    and modifying fingerprint data.
    A new policy file "cc.ullrich-online.fingerprint-gui.policy" is installed
    in "/usr/share/polkit-1/actions/". This policy requires user authentication
    via polkit when the users fingerprint data are modified. So an attacker with
    access to a user's desktop while the user is away, can not register his
    fingerprint in the name of this user any more.
  * libpolkit-qt-1.0 is not supported any more;
* Wed Mar  4 2015 fstrba@suse.com
- update to 1.06
- clean some rpmlint/post-build warnings/errors
* Thu Oct  3 2013 mailaender@opensuse.org
- update to 1.05
* Sun Apr  7 2013 johann.luce@wanadoo.fr
- update to 1.04
* Mon Jan 17 2011 quentin@links2linux.de
- initial package with version 1.00
