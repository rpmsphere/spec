%define __os_install_post %{nil}

Summary: Visual authoring of HTML5 user interfaces
Name: html5-maqetta
Version: 3.1
Release: 0.1
License: AFL or BSD
Group: Applications/Editors
Source0: http://maqetta.org/downloads/maqetta-Preview3.1.zip
Source1: maqetta.png
URL: http://maqetta.org/
Requires: jre, oxzilla
BuildArch: noarch

%description
Maqetta is an open source project that provides WYSIWYG visual authoring of
HTML5 user interfaces. The Maqetta application itself is authored in HTML,
and therefore runs in the browser without requiring additional plugins or
downloads.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a %{SOURCE1} * $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=HTML5 Maqetta
Comment=Visual authoring of HTML5 user interfaces
Categories=Development;
Exec=%{name}
Terminal=true
Type=Application
Icon=%{_datadir}/%{name}/maqetta.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
(sleep 5 ; oxzilla http://127.0.0.1:50000/maqetta ; pkill maqetta) &
./maqetta.local.unix.sh
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Mon Nov 21 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial build
