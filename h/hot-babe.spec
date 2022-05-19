Name:           hot-babe
BuildRequires:  gtk2-devel
Version:        0.4git
Release:        1
License:        Artistic License
Summary:        System Activity Monitor
Group:          System/Monitoring
#Source:         http://dindinx.net/hotbabe/downloads/%{name}-%{version}.tar.bz2
Source:		https://github.com/allanlw/hot-babe/archive/refs/heads/master.zip#/%{name}-master.zip
#URL: 	        https://sourceforge.net/projects/hotbabe/
URL:		https://github.com/allanlw/hot-babe

%description
Hot-babe is a small graphical utility which display the system activity
in a very special way. When the CPU is idle, it displays a dressed girl,
and when the activity goes up, as the temperature increases, the girl
begins to undress, to finish totally naked when the system activity
reaches 100%. Of course, if you can be shocked by nudity, don't use it!

%prep
%setup -q -n %{name}-master
mv doc/* .

%build
make PREFIX=/usr

%install
make PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT install

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
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/man/man1/%{name}.*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Apr 17 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4git
- Rebuild for Fedora
* Thu Jan 24 2008 mmarek@suse.cz
- packaged hot-babe-0.2.2
