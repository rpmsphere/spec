Summary: Graphical front-end for ndiswrapper
Name: ndisgtk
Version: 0.8.5
Release: 1
License: GPL
Group: System Environment/Kernel
URL: https://launchpad.net/ndisgtk/
Source: https://jak-linux.org/projects/ndisgtk/ndisgtk-%{version}.tar.gz
Patch: ndisgtk-0.8-centos.patch
BuildRequires: intltool, python2-devel, pygtk2-devel
Requires: python, pygtk2, ndiswrapper
BuildArch: noarch

%description
Ndisgtk is a graphical front-end for ndiswrapper, which gives users an easy
way to install the Windows wireless drivers.

%prep
%setup -q
#%patch0 -p0

%{__cat} <<EOF >ndisgtk.desktop.in
[Desktop Entry]
_Name=Windows Wireless Drivers
_Comment=Install windows wireless drivers using ndiswrapper
Exec=ndisgtk
Icon=ndisgtk.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;SystemSetup;
EOF

%{__cat} <<EOF >ndisgtk.console
USER=root
PROGRAM=%{_sbindir}/ndisgtk
SESSION=true
EOF

%{__cat} <<EOF >ndisgtk.pam
#%PAM-1.0
auth       sufficient   /lib/security/pam_rootok.so
auth       sufficient   /lib/security/pam_timestamp.so
auth       required     /lib/security/pam_stack.so service=system-auth
session    required     /lib/security/pam_permit.so
session    optional     /lib/security/pam_timestamp.so
session    optional     /lib/security/pam_xauth.so
account    required     /lib/security/pam_permit.so
EOF

%build
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -dp -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/ndisgtk

%{__install} -Dp -m0644 ndisgtk.8 %{buildroot}%{_mandir}/man8/ndisgtk.8
%{__install} -Dp -m0644 ndisgtk.console %{buildroot}%{_sysconfdir}/security/console.apps/ndisgtk
%{__install} -Dp -m0644 ndisgtk.pam %{buildroot}%{_sysconfdir}/pam.d/ndisgtk

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/applications/ndisgtk-kde.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_sbindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%doc NEWS
%doc %{_mandir}/man8/ndisgtk.8*
%config %{_sysconfdir}/pam.d/ndisgtk
%config %{_sysconfdir}/security/console.apps/ndisgtk
%{_bindir}/ndisgtk
%{_datadir}/applications/ndisgtk.desktop
%{_datadir}/icons/hicolor/48x48/apps/ndisgtk-error.png
%{_datadir}/icons/hicolor/48x48/apps/ndisgtk.png
%{_datadir}/ndisgtk/
%{_datadir}/pixmaps/ndisgtk.xpm
%{_sbindir}/ndisgtk

%changelog
* Sun May 22 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.5
- Rebuilt for Fedora
* Mon Dec 03 2007 Dag Wieers <dag@wieers.com> - 0.8-1 - +/
- Initial package. (using DAR)
