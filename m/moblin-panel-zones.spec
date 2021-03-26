# norootforbuild

Name:          moblin-panel-zones
Summary:       Zones panel
Group:         System/X11/Utilities
Version:       0.1.19
License:       LGPL2
URL:           http://www.moblin.org
Release:       7.1
Source0:       %{name}-%{version}.tar.bz2
Source1:	people.png
# PATCH-FIX-UPSTREAM moblin-panel-zones_new_clutter-gtk.patch awafaa@opensuse.org -- We are using clutter-gtk-0.90 already.
Patch0:        moblin-panel-zones_new_clutter-gtk.patch
# PATCH-FIX-UPSTREAM moblin-panel-zones_configure.ac_clutter-gtk-0.90.patch awafaa@opensuse.org -- We are using clutter-gtk-0.90 already.
Patch1:        moblin-panel-zones_configure.ac_clutter-gtk-0.90.patch
BuildRequires: pkgconfig(clutter-x11-1.0)
BuildRequires: pkgconfig(gdk-x11-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libgnome-menu)
BuildRequires: mutter-moblin-devel
BuildRequires: pkgconfig(libwnck-1.0)
BuildRequires: pkgconfig(clutter-gtk-0.10)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: libmx-devel
##BuildRequires: update-desktop-files
Requires:      libmx
Requires:      mutter-moblin

%description
Moblin zones panel

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1
#%patch1 -p1

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
%makeinstall

##%suse_update_desktop_file %buildroot/%_datadir/mutter-moblin/panels/moblin-panel-zones.desktop
# remove invalid locales on suse
%__rm -rf %buildroot/%_datadir/locale/ast

mkdir -p $RPM_BUILD_ROOT%{_datadir}/moblin-panel-zones/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/moblin-panel-zones/people.png

%find_lang %name

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
	if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
		mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
	fi
done

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root,-)
%doc COPYING
%{_libexecdir}/moblin-panel-zones
%{_datadir}/dbus-1/services/org.moblin.UX.Shell.Panels.zones.service
%{_datadir}/%name
%dir %_datadir/mutter-moblin
%dir %_datadir/mutter-moblin/panels
%{_datadir}/mutter-moblin/panels/moblin-panel-zones.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Tue Oct 19 2010 awafaa@opensuse.org
- Replace people.png (MeeGo image) with Smeegol image
* Fri Aug 13 2010 awafaa@opensuse.org
- Revert to using clutter-gtk-0.10
* Thu Aug  5 2010 andrea@opensuse.org
- spec file clean up
* Thu Jul 29 2010 awafaa@opensuse.org
- Replace nbtk with mx
* Mon Jul 19 2010 awafaa@opensuse.org
- Update to version 0.1.19
- Rework moblin-panel-zones-clutter-gtk-0.90.patch into
  moblin-panel-zones-_new_clutter-gtk.patch
- Add moblin-panel-zones_configure.ac_clutter-gtk-0.90
* Tue Jun 15 2010 dimstar@opensuse.org
- Add moblin-panel-zones-clutter-gtk-0.90.patch to compile against
  clutter-gtk-0.90 instead of *-0.10 and adjust RuildRequire for
  pkgconfig(clutter-gtk-0.90)
* Thu Jun 10 2010 awafaa@opensuse.org
- Initial import into openSUSE version 0.1.15
* Thu Apr 15 2010 Thomas Wood <thomas.wood@intel.com> - 0.1.15
- Update background asset for new visual design
  - Updated translations
* Wed Apr  7 2010 Thomas Wood <thomas.wood@intel.com> - 0.1.14
- Update to version 0.1.14
  - Further updates to visual design
  - Updated translations
* Tue Apr  6 2010 Thomas Wood <thomas.wood@intel.com> - 0.1.13
- Update to version 0.1.13
  - Further updates to visual design
* Tue Apr  6 2010 Thomas Wood <thomas.wood@intel.com> - 0.1.12
- Update to version 0.1.12
  - Further updates to visual design
* Thu Apr  1 2010 Thomas Wood <thomas.wood@intel.com> - 0.1.11
- Update to version 0.1.11
  - New visual design assets
* Mon Mar 22 2010 Rob Bradford <rob@linux.intel.com> - 0.1.10
- Update to version 0.1.10 (ported to latest MX)
* Tue Mar  2 2010 Thomas Wood <thomas.wood@intel.com> 0.1.9
- Update to version 0.1.9
* Mon Mar  1 2010 Thomas Wood <thomas.wood@intel.com> 0.1.8
- Update to version 0.1.8
* Tue Feb 16 2010 Thomas Wood <thomas.wood@intel.com> 0.1.7
- Update to version 0.1.7
* Thu Feb 11 2010 Thomas Wood <thomas.wood@intel.com> 0.1.6
- Update to version 0.1.6
* Wed Feb 10 2010 Thomas Wood <thomas.wood@intel.com> 0.1.5
- Update to version 0.1.5
* Tue Feb  9 2010 Thomas Wood <thomas.wood@intel.com> 0.1.4
- Update to version 0.1.4
* Tue Feb  9 2010 Thomas Wood <thomas.wood@intel.com> 0.1.3
- Update to version 0.1.3
* Tue Feb  9 2010 Thomas Wood <thomas.wood@intel.com> 0.1.2
- Update to version 0.1.2
* Tue Feb  9 2010 Thomas Wood <thomas.wood@intel.com> 0.1.1
- Update to version 0.1.1
* Mon Feb  8 2010 Thomas Wood <thomas.wood@intel.com> 0.1.0
- Initial package
