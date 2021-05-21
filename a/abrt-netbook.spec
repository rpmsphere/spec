Name:           abrt-netbook
Summary:        Control Panel Applet for abrt
Version:        0.0.1
Release:        7.1
Group:          System/Libraries
License:        GPLv2+
URL:            http://www.meego.org
Source0:        %{name}-%{version}.tar.bz2
Source1:        moblin-abrt.png
Requires:       abrt
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.21
BuildRequires:  libmx-devel
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(libgnome-control-center-extension)
BuildRequires:  intltool
BuildRequires:	mutter-moblin-devel
BuildRequires:  hicolor-icon-theme
##BuildRequires:  update-desktop-files

%description
This application allows users to control global settings for abrt.

%prep
%setup -q 

%build
%configure --disable-static
%__make %{?jobs:-j%jobs}

%install
%makeinstall
find %{buildroot}%{_libdir} -name '*.la' -delete -print
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/abrt.png
##%suse_update_desktop_file abrt-properties
%find_lang %name

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %name.lang
%defattr(-,root,root,-)
%{_libdir}/control-center-1/extensions/libabrt.so
%{_datadir}/applications/abrt-properties.desktop
%{_datadir}/icons/hicolor/48x48/apps/abrt.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Fri Aug  6 2010 andrea@opensuse.org
- spec file clean up
* Mon Jun 21 2010 glin@novell.com
- Add icon, moblin-abrt.png, for abrt-properties.destkop
* Fri Jun 18 2010 awafaa@opensuse.org
- Hackishly remove the .desktop file to enable package to build
* Wed Jun  9 2010 awafaa@opensuse.org
- Initial import for openSUSE version 0.0.1
