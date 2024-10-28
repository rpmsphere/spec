%undefine _debugsource_packages

Name:           litebook
Version:        3.0
Release:        10.1
Summary:        Light-weight and useful reader
Source0:        https://litebook-project.googlecode.com/files/LiteBook_v%{version}.tar.gz
URL:            https://code.google.com/p/litebook-project/
Group:          Applications/Text
License:        Apache License 2.0
BuildRequires:  ghostscript-core ImageMagick
Requires:       python2-wxpython, python2-chardet, python2-rarfile, python2-netifaces
#BuildArch:  noarch

%description
Light-weight book reader written with wxPython.

%prep
%setup -q -n %{name}3
convert litebook.ico litebook.png
rm -rf .svn */.svn */*/.svn */*/*/.svn

%build

%install
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -R * $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/UnRAR2

%__install -d $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
python2 litebook.py
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}

%__install -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%_datadir/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Litebook
Comment=Light-weight book reader written with wxPython
Icon=litebook
Categories=Application;Utility;
Exec=litebook
Terminal=false
Type=Application
EOF

%__install -D -m 644 %{name}-0.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jan 6 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora
