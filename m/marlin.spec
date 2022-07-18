Name:           marlin
Version:        0.13
Release:        17.1
Summary:        A Sound Sample Editor for GNOME
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://live.gnome.org/Marlin
Source0:        http://folks.o-hand.com/iain/%{name}-releases/%{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-link-fix.patch
Patch1:         %{name}-%{version}-icon-path.patch
BuildRequires:  GConf2-devel
BuildRequires:  gtk2-devel
BuildRequires:  unique-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  soundtouch-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  scrollkeeper
Requires(pre):    GConf2
Requires(post):   GConf2
Requires(preun):  GConf2
Requires(post):   scrollkeeper
Requires(postun): scrollkeeper

%description
Marlin aims to be a fully featured and powerful sample editor for the
GNOME2 platform.

%prep
%setup -q
%patch0 -p1 -b .link-fix
%patch1 -p1 -b .icon-path
sed -i 's|glib/gmarkup\.h|glib.h|' src/libegg/egg-toolbars-model.c

%build
%configure
#use system libtool to disable standard RPATH
make %{?_smp_mflags} LIBTOOL=%{_bindir}/libtool CFLAGS+=-Wno-format-security

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%find_lang %{name} --with-gnome
desktop-file-install                                    \
        --dir %{buildroot}%{_datadir}/applications      \
        --delete-original                               \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
        %{_sysconfdir}/gconf/schemas/%{name}.schemas
 >& /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` 
    gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :
update-desktop-database &> /dev/null || :
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` 
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor ||:
fi

%postun
scrollkeeper-update -q || :
update-desktop-database &> /dev/null || :

touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi

%files -f %{name}.lang
%doc AUTHORS README NEWS
%{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_libdir}/*.so.*
%{_libdir}/%{name}-%{version}/*.so.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}/
%exclude %{_libdir}/*.so
#exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a
%exclude %{_libdir}/%{name}-%{version}/*.a
#exclude %{_libdir}/%{name}-%{version}/*.la
%exclude %{_libdir}/%{name}-%{version}/*.so
%exclude %{_includedir}/lib%{name}/

%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Thu Jan 28 2010 Dodji Seketeli <dodji@redhat.com> - 0.13-6
- Add scrollkeeper BuildRequires
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Sun Feb 22 2009 Dodji Seketeli <dodji@redhat.org> 0.13-4
- Patch to fix broken application menu icon installation
* Thu Feb 19 2009 Dodji Seketeli <dodji@redhat.org> 0.13-3
- Remove --vendor from desktop-file-install
- Remove 'Requires(post)/(postun): desktop-file-utils'
- Use system libtool to disable standard rpath
* Wed Feb 18 2009 Dodji Seketeli <dodji@redhat.org> 0.13-2
- Killed $RPM_BUILD_ROOT in favour of %%{buildroot}
- Added a %%pre section to remove potentially
- Fix scrollkeeper-update and update-desktop-database scriptlets.
- Added correct Requires(post[un]) for desktop-file-utils
* Tue Feb 17 2009 Dodji Seketeli <dodji@redhat.org> 0.13-1
- Initial import
