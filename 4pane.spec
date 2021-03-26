Summary: A quad-pane detailed-list file manager
Name: 4pane
Version: 2.0
Release: 5.1
License: GPL
Group: Productivity/File utilities
URL: http://www.4pane.co.uk/
Source: http://sourceforge.net/projects/fourpane/files/%{version}/%{name}-%{version}.tar.gz
BuildRequires: wxGTK-devel xz-devel

%description
4Pane is a detailed-list file manager which displays directories and files
in separate panes. Generally two pairs of these twin-panes are displayed
at a time, resulting in easy dragging/pasting of files. 4Pane aims to be fast
and fully-featured without bloat.

%prep
%setup -q

%build
%configure --disable-symlink --disable-desktop
make %{?_smp_mflags} CXX="g++ -g3 -ggdb"

%install
make DESTDIR=%{buildroot} install
%find_lang 4Pane

# Create the .desktop on the fly, as it's not quite the same as the tarball one
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
GenericName=File Manager
Comment=A four-pane file manager
Exec=%{name} -c /usr/share/4pane/
Icon=%{name}
Terminal=false
Type=Application
Version=1.0
StartupNotify=false
Categories=Utility;FileManager;
EOF

# Icons. In theory these should go into icons/hicolor/
install -D -m 644 bitmaps/4PaneIcon48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -m 644 bitmaps/4PaneIcon32.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
install -D -m 644 bitmaps/4PaneIcon16.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm
# In practice, fedora doesn't seem to look there, but does in:
install -D -m 644 bitmaps/4PaneIcon48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

mv $RPM_BUILD_ROOT%{_bindir}/4Pane $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/4Pane $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/doc/4Pane $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
cp README INSTALL LICENCE $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%files -f 4Pane.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Dec 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
* Fri Apr 13 2012 DH
- Minor changes for 1.0 release:
- LDFLAGS no longer required
- Extra deps
* Fri Dec 24 2010 DH
- Use DESTDIR=%{buildroot} instead of %makeinstall
- Use %find_lang for translations
* Tue Jun 1 2010 DH
- Explicitly added LDFLAGS to cope with FC13 DSO linking change
* Sat May 9 2009 DH
- Made more standards-compliant, and provide a menu entry
* Sat May 3 2008 DH
- Minor changes for 0.5.1 release
* Sun Nov 11 2007 DH
- Build for Fedora
