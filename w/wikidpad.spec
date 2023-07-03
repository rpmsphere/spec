Name: wikidpad
Summary: A real-time wiki
Version: 2.1
Release: 7.1
Group: Applications/Editors
License: BSD
URL: https://wikidpad.sourceforge.net/
Source0: https://nchc.dl.sourceforge.net/project/wikidpad/wikidpad/2.1/2.1_01/WikidPad-2.1_01-src.zip
Source1: %{name}.png
BuildArch: noarch
BuildRequires: python

%description
wikidPad is a Wiki-like notebook for storing your thoughts, ideas, todo lists,
contacts, or anything else you can think of to write down.

%prep
%setup -q -c

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec python WikidPad.py
EOF

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=WikidPad
Comment=A real-time wiki
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Applications;Utility;
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
