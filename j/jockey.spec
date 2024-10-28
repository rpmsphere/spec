%global selinux_variants mls targeted

Name:           jockey
Version:        0.9.7
Release:        7.4
Summary:        Jockey driver manager
License:        GPLv2+
URL:            https://launchpad.net/jockey
Source0:        https://launchpad.net/jockey/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        fedora-%{name}-0.9.6.tar.bz2
Patch0:         jockey-0.9.3-gtkwidthfix.patch
BuildArch:      noarch 
BuildRequires:  python2-devel python2-distutils-extra gettext intltool
BuildRequires:  selinux-policy-devel
Requires:       dbus-python polkit PackageKit python-xkit

%description
Jockey provides an user interface and desktop integration for installation 
and upgrade of third-party drivers. It is written in a distribution agnostic 
way, and to be easily portable to different front-ends (GNOME, KDE, 
command line).

%package gtk
Summary:        GTK front-end for Jockey driver manager
Requires:       %{name} = %{version}-%{release}
Requires:       dbus-python polkit-gnome gdk-pixbuf2 gtk3 
Requires:       gobject-introspection libnotify pygobject3

%description gtk
This package provides a GTK interface for Jockey.

Jockey provides an user interface and desktop integration for installation 
and upgrade of third-party drivers. It is written in a distribution agnostic 
way, and to be easily portable to different front-ends (GNOME, KDE, 
command line).

%package kde
Summary:        KDE front-end for Jockey driver manager
Requires:       %{name} = %{version}-%{release}
Requires:       dbus-python polkit-kde PyQt4 PyKDE4
Requires:       pygobject3

%description kde
This package provides a KDE interface for Jockey.

Jockey provides an user interface and desktop integration for installation 
and upgrade of third-party drivers. It is written in a distribution agnostic 
way, and to be easily portable to different front-ends (GNOME, KDE, 
command line).

%package selinux
Summary:        SELinux module for Jockey driver manager
Epoch:          1
BuildRequires:  checkpolicy selinux-policy util-linux
Requires:       %{name}
Requires:       selinux-policy selinux-policy-targeted
Requires(post):   /usr/sbin/semodule
Requires(postun): /usr/sbin/semodule

%description selinux
This package provides an SELinux module for Jockey driver manager.
You should install this package if you are using SELinux, so that Jockey
can be run in enforcing mode.

%prep
%setup -q -a 1
%patch 0 -p1 -b .gtkwidthfix
sed -i.trayfix "s|if indicator:|if indicator or trayicon:|" gtk/jockey-gtk
sed -i.nocert "s|'repository' not in|'repository' in|" jockey/ui.py
sed -i.noblacklist "s|do_blacklist=True|do_blacklist=False|" jockey/handlers.py
cp fedora-%{name}-0.9.6/%{name}/* %{name}/

%build
python2 setup.py build

# building SELinux module
cd fedora-%{name}-0.9.6/selinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv %{name}.pp %{name}.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

%install
python2 setup.py install -O1 --root $RPM_BUILD_ROOT
rm -r $RPM_BUILD_ROOT%{_datadir}/doc
mkdir -p $RPM_BUILD_ROOT%{_var}/cache/%{name}

# Install config file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 fedora-%{name}-0.9.6/config/%{name}.conf \
      $RPM_BUILD_ROOT%{_sysconfdir}/

# Move autostart files to the new place
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/
mv $RPM_BUILD_ROOT%{_datadir}/autostart/* $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/
rmdir $RPM_BUILD_ROOT%{_datadir}/autostart/

# install fedora extra files
cp -a fedora-%{name}-0.9.6/handlers \
      $RPM_BUILD_ROOT%{_datadir}/%{name}

# install the selinux module
for selinuxvariant in %{selinux_variants}
do
  install -d $RPM_BUILD_ROOT%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 \
    fedora-%{name}-0.9.6/selinux/%{name}.pp.${selinuxvariant} \
    $RPM_BUILD_ROOT%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done
hardlink -cv $RPM_BUILD_ROOT%{_datadir}/selinux

%find_lang %{name}
sed -i 's|DesktopSettings;X-GNOME-Settings-Panel;||' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-gtk.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/jockey-backend %{buildroot}%{_bindir}/*

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%post selinux
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/%{name}.pp &> /dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%postun selinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
    /usr/sbin/semodule -s ${selinuxvariant} -r %{name} &> /dev/null || :
  done
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README.txt
%config %{_sysconfdir}/%{name}.conf
%{_bindir}/jockey-text
%{python2_sitelib}/*
%{_datadir}/%{name}/%{name}-backend
%{_datadir}/%{name}/handlers
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/dbus-1/system-services/*
%{_datadir}/polkit-1/actions/*
%{_sysconfdir}/dbus-1/system.d/*
%{_var}/cache/%{name}

%files gtk
%{_bindir}/jockey-gtk
%{_datadir}/%{name}/%{name}-gtk.ui
%{_datadir}/applications/jockey-gtk.desktop
%{_sysconfdir}/xdg/autostart/jockey-gtk.desktop
%{_datadir}/dbus-1/services/*

%files kde
%{_bindir}/jockey-kde
%{_datadir}/%{name}/LicenseDialog.ui
%{_datadir}/%{name}/ManagerWindowKDE4.ui
%{_datadir}/%{name}/ProgressDialog.ui

%{_datadir}/applications/jockey-kde.desktop
%{_sysconfdir}/xdg/autostart/jockey-kde.desktop
%{_datadir}/kde4/apps/jockey/jockey.notifyrc

%files selinux
%doc fedora-%{name}-0.9.6/selinux/*te
%{_datadir}/selinux/*/%{name}.pp

%changelog
* Fri Jan 31 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.7
- Rebuilt for Fedora
* Fri Dec 09 2011 Chris Smart <chris@kororaa.org> - 0.9.6-2
- Added pygobject3 to list of runtime dependencies, fixes breakage on KDE
* Thu Dec 08 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.9.6-1
- Updated to latest upstream version 0.9.6
* Wed Dec 07 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.9.5-2
- Add an Epoch for jockey-selinux to resolve versioning inconsistency
* Tue Dec 06 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.9.5-1
- Remove separate versioning for -selinux subpackage
* Mon Dec 05 2011 Chris Smart <chris@kororaa.org> - 0.9.5-1
- Update to upstream version 0.9.5
- Added support for akmods (where available), if enabled in Jockey config file.
* Sun Oct 16 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.9.3-3
- Add initial PAE kernel module installation support
* Thu Aug 18 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.9.3-2
- jockey should depend on xkit, not jockey-gtk
* Thu Jul 28 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.9.3-1
- Initial version
