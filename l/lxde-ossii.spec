Name:           lxde-ossii
Version:        0.3.2.1
Release:        1
Summary:        Liteweight X11 desktop session
Group:          Applications/System
License:        GPL
URL:            http://sourceforge.net/projects/lxde/
Source:         http://downloads.sourceforge.net/lxde/lxde-common-%{version}.tar.bz2
Source1:	ossii.png
Requires:       lxsession-lite, lxpanel, lxappearance, lxtask, pcmanfm
#Requires:	xscreensaver or gnome-screensaver or xautolock+xlockmore
Provides:	lxde
Obsoletes:	lxde-common

%description
This project aimed to provide a new desktop environment which is useful
enough and keep resource usage lower at the same time. Useabiliy, speed,
and memory usage are our main concern.

%prep
%setup -q -n lxde-common-%{version}
sed -i -e 's|sNet/ThemeName=|#sNet/ThemeName=|' -e 's|sNet/IconThemeName=|#sNet/IconThemeName=|' lxde-settings/config
sed -i -e '/xscreensaver/d' -e '/smproxy/d' default.in
sed -i -e 's/firefox/mozilla-firefox/' -e 's/my-computer/ossii/' lxpanel/panel.in

%build
%configure
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}
%__rm -rf *.in */*.in
%__install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/lxpanel/images/ossii.png

%clean
%__rm -rf %{buildroot}

%files
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/*
%{_bindir}/*
%{_datadir}/lxde
%exclude %{_datadir}/icons/nuoveXT2
%{_datadir}/xsessions/LXDE.desktop
%{_datadir}/lxpanel/profile/LXDE/*
%{_datadir}/lxpanel/images/*
%{_datadir}/man/man1/*.1.gz

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2.1
- Rebuild for Fedora
