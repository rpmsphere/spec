Summary: An interactive sky map for exploring the stars and planets
Name: flash-planetarium
Version: 20110815
Release: 1
License: freeware
Group: Applications/Emulators
Source0: http://neave.com/planetarium/planetarium.swf
Source1: %{name}.png
URL: http://neave.com/planetarium/app/
Requires: oxzilla, flash-plugin
BuildArch: noarch

%description
Planetarium shows you over 1,500 stars - that's every star up to magnitude "+5".
These stars are the brightest in the night sky, the ones you can see with your own
naked eye on a good dark night away from city lights.

%prep
%setup -q -T -c

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%{__cat} > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Flash Planetarium
Comment=An interactive sky map for exploring the stars and planets
Categories=Education;
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/%{name}.png
EOF

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla planetarium.swf
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
* Wed Nov 02 2011 Wei-Lun Chao <bluebat@member.fsf.org> 20110815
- Initial build
