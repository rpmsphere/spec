Name:           gnome-specimen
Version:        0.4
Release:        1
Summary:        A simple tool to view and compare fonts installed on your system
Group:          Applications/System
License:        GPLv2+
URL:            http://uwstopia.nl/geek/projects/gnome-specimen/
Source0:        http://uwstopia.nl/geek/projects/gnome-specimen/releases/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  GConf2-devel, gnome-python2, pygtk2-libglade, perl-XML-Parser, pkgconfig, gettext, desktop-file-utils
Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
Gnome Specimen is a simple tool to view and compare fonts installed on 
your system

%prep
%setup -q

%build
export PYTHON=/usr/bin/python2
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %{buildroot}%{python2_sitelib}
mv %{buildroot}%{python2_sitearch}/specimen %{buildroot}%{python2_sitelib}

desktop-file-install --vendor="" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications        \
  $RPM_BUILD_ROOT%{_datadir}/applications//%{name}.desktop

%find_lang %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
    killall -HUP gconfd-2 || :
fi

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
killall -HUP gconfd-2 || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
    killall -HUP gconfd-2 || :
fi

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{python2_sitelib}/specimen
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{name}.schemas

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Wed Jul 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3-2
- fix license tag
* Wed Jul 18 2007 Damien Durand <splinux@fedoraproject.org> - 0.3-1
- Update to 0.3
* Wed Jul 11 2007 Damien Durand <splinux@fedoraproject.org> - 0.2-4
- Fix desktop-file section
* Wed Jun 27 2007 Damien Durand <splinux@fedoraproject.org> - 0.2-3
- Fix owned directories
* Fri Jun 09 2007 Damien Durand <splinux@fedoraproject.org> - 0.2-2
- Fix gconf shemas
- Set BuildArch to noarch
- Fix wrong entries from desktop file
* Fri Jun 08 2007 Damien Durand <splinux@fedoraproject.org> - 0.2-1
- Initial RPM release
