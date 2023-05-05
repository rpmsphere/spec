Summary: Application for Mind Mapping, Knowledge and Project Management
Name: freeplane
Version: 1.10.6u1
Release: 1.bin
License: LGPL
Group: Applications
Source0: https://sourceforge.net/projects/freeplane/files/freeplane%20stable/freeplane_bin-%{version}.zip
URL: https://docs.freeplane.org/
Source1: freeplane.png
BuildRequires: unzip
BuildArch: noarch

%description
Application for Mind Mapping, Knowledge Management, Project Management.
Develop, organize and communicate your ideas and knowledge in the most
effective way.

%prep
%setup -q

%build
#No build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

# script
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/usr/bin/sh
cd /usr/share/%{name}
./%{name}.sh "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Freeplane
Comment=%{summary}
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Education;Java;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc license.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10.6u1
- Rebuilt for Fedora
