Name:          mpp-sdk
Summary:       SDK for mpowerplayer
Version:       1185
Release:       1%{?dist}.bin
URL:           http://mpowerplayer.com/sdk/
Group:         Development/Languages/Java
License:       freeware
Source0:       http://mpowerplayer.com/mpp-sdk-1185.zip
Source1:       mpowerplayer.png
Requires:      jre
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildArch:     noarch

%description
The mplayit software developer kit includes the mplayit widget as a standalone
application. It’s a pure Java emulator implementing MIDP 2.0 and MMAPI,
suitable for integration with your favorite environment and IDE. Third-party
integration efforts exist for Ant, Eclipse, Idea, and we hear of more efforts
almost daily.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %buildroot
mkdir -p %buildroot%{_datadir}/%{name}
mkdir -p %buildroot%{_bindir}
cp -a %{SOURCE1} * %buildroot%{_datadir}/%{name}

%__cat > %{buildroot}%{_bindir}/mpowerplayer << EOF
#!/bin/sh
cd %{_datadir}/%{name}
java -jar player.jar
EOF

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mpowerplayer.desktop <<EOF
[Desktop Entry]
Name=Mpowerplayer
Comment=Mobile applications on your desktop
Exec=mpowerplayer
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/mpowerplayer.png
Encoding=UTF-8
Categories=Application;Development;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/mpowerplayer
%{_datadir}/%{name}
%{_datadir}/applications/mpowerplayer.desktop

%changelog
* Thu Jul 28 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial package
