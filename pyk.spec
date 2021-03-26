Name: pyk
Summary: Text editor in PyQt4
Version: 1.0.16
Release: 3.1
Group: Applications/Editors
License: GPLv2
URL: http://kib2.free.fr/PyK/
Source0: http://kib2.free.fr/PyK/PYK.zip
BuildArch: noarch
Requires: python-docutils
Requires: PyQt4
Obsoletes: pyedit, restinpeace

%description
PyK is a new editor, successor of PyEdit and reStInPeace, written in Python
with the help of the Qt4 toolkit. It has nice features and is highly extensible
via plugins and commands. I'm developping it for fun, because I really like
text editors.

%prep
%setup -q -n PYK!

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=PyK
Comment=Text editor in PyQt4
Exec=pyk
Icon=%{_datadir}/%{name}/PyK.png
Terminal=false
Type=Application
Categories=Utility;TextEditor;
StartupNotify=true
EOF
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
cd %{_datadir}/%{name}
python2 main.py
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py %{buildroot}%{_datadir}/%{name}/*/*.py %{buildroot}%{_datadir}/%{name}/*/*/*.py
sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/Scripts/to_tex.py

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.16
- Rebuild for Fedora
