Name:		thotkeeper
Summary: 	Cross-platform personal daily journaling
Version: 	0.4.0
Release: 	3.1
Source:		https://thotkeeper.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	%{name}.png
URL:		https://code.google.com/p/thotkeeper/
License:	New BSD License
Group:		Applications/Productivity
Requires:	python2-wxpython
BuildArch:	noarch

%description
ThotKeeper is a simple, open source, daily journal application created
by C. Michael Pilato for his wife, Amy. Features:
* Cross-platform functionality with native widgets
* Simple, easy-to-navigate interface
* XML storage format
* Support for multiple entries per day
* Per-entry authors
* Hierarchical tag support

%prep
%setup -q
sed -i 's|lib|/usr/share/thotkeeper|' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp lib/* $RPM_BUILD_ROOT%{_datadir}/%{name}

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Thot Keeper
Comment=Cross-platform personal daily journaling
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
EOF

#icons
install -Dm755 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES INSTALL LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
