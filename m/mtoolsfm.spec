%undefine _debugsource_packages
%global _name MToolsFM

Summary: A graphical frontend to mtools
Name: mtoolsfm
Version: 1.9.5
Release: 7.1
License: GPL
Group: X11/Utilities
URL: https://mtoolsfm.sourceforge.net/
Requires:	mtools
BuildRequires:	gtk+-devel
Source: https://downloads.sourceforge.net/mtoolsfm/%{_name}-%{version}.tar.gz

%description
This program is a little file-manager and allows easy access 
to (dos-)floppies under linux / UNIX. It uses mtools and has a nice GUI.

%prep
%setup -q -n %{_name}-%{version}

%build
export CPPFLAGS="-fPIE -I/usr/lib64/glib/include -I/usr/include/glib-1.2 -I/usr/include/gtk-1.2"
#autoreconf -ifv
./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{_name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Comment=Graphical interface to mtools
Exec=%{_name} 
Icon=%{_name}.color.png
Terminal=false
Type=Application
Categories=Application;Utility;System;
EOF

# install icons
install -d %{buildroot}%{_datadir}/pixmaps
install -m 644 %{_name}*.png %{_name}*.xpm %{buildroot}%{_datadir}/pixmaps

%clean
rm -rf %{buildroot}

%files
%doc COPYING ChangeLog AUTHORS NEWS README THANKS
%{_mandir}/man1/%{_name}.1.*
%{_bindir}/%{_name}
%{_datadir}/locale/*/LC_MESSAGES/%{_name}.mo
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Fri Jun 05 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.5
- Rebuilt for Fedora 
