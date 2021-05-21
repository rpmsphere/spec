Name:           hot-babe
BuildRequires:  gtk2-devel
Version:        0.2.2
Release:        1
License:        Artistic License
Summary:        System Activity Monitor
Group:          System/Monitoring
Source:         http://dindinx.net/hotbabe/downloads/%{name}-%{version}.tar.bz2
Patch0:         hot-babe-optflags.patch
URL: 	        https://sourceforge.net/projects/hotbabe/

%description
Hot-babe is a small graphical utility which display the system activity
in a very special way. When the CPU is idle, it displays a dressed girl,
and when the activity goes up, as the temperature increases, the girl
begins to undress, to finish totally naked when the system activity
reaches 100%. Of course, if you can be shocked by nudity, don't use it!

%prep
%setup -q
%patch0

%build
make PREFIX=/usr

%install
make PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT install
rm -r $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

# menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Hot Babe
Comment=CPU meters
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=System;Monitor;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog NEWS TODO LICENSE CONTRIBUTORS copyright config.example
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/man/man1/%{name}.*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
* Thu Jan 24 2008 mmarek@suse.cz
- packaged hot-babe-0.2.2
