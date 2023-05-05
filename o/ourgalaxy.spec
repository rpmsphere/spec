%global _name OurGalaxy
%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Summary: A Three Dimensional Galactic Atlas
Name: ourgalaxy
Version: 2.1
Release: 1.bin
License: Free Software
Group: Applications
Source0: https://otherwise.com/OurGalaxy_Linux.zip
URL: https://otherwise.com/
AutoReq: off
ExclusiveArch: x86_64

%description
Our Galaxy is a unique app that helps you understand the structural components
of the Galaxy and visualize the locations and physical properties of deep sky
objects in and around it.

%prep
%setup -q -n %{_name}_Linux
rm -f *.debug
chmod +x %{_name}_Linux.x86_64

%build
#No build

%install
install -d $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_libexecdir}/%{name}

# script
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/usr/bin/sh
cd %{_libexecdir}/%{name}
./%{_name}_Linux.x86_64 "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{_name}
Comment=%{summary}
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Education;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -Dm644 OurGalaxy_Linux_Data/Resources/UnityPlayer.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
