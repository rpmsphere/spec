Name:		ulipad
Version:	4.1
Release:	5.1
Summary:	An editor written with wxPython
Source:		http://ulipad.googlecode.com/files/%{name}.%{version}.zip
URL:		http://code.google.com/p/ulipad/
Group:		Applications/Editors
License:	GNU General Public License v2 (GPL)
BuildArch:      noarch
Requires:	python2-wxpython
BuildRequires:	ghostscript-core ImageMagick
BuildRequires:	sane-backends-libs

%description
UliPad uses Mixin and Plugin technique as its architecture.
Most of its classes can be extended via mixin and plugin components,
and finally become an integrity class when creating the instance.

%prep
%setup -q -n ulipad
convert ulipad.ico ulipad.png

%build

%install
%__rm -rf $RPM_BUILD_ROOT
%__install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -R * $RPM_BUILD_ROOT%{_datadir}/%{name}

%__install -d $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
python2 UliPad.py
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}

%__install -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=UliPad
Comment=UliPad is an editor written with wxPython
Icon=ulipad
Categories=Application;Utility;Editor;
Exec=ulipad
Terminal=false
Type=Application
EOF

%__install -D -m 644 %{name}-0.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*

%changelog
* Sun Nov 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1
- Rebuild for Fedora
