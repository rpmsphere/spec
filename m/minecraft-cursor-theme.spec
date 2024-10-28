%define theme_name Minecraft

Summary:        Minecraft cursor theme
Name:           minecraft-cursor-theme
Version:        1.1
Release:        1
License:        freeware
Group:          User Interface/Desktops
URL:            https://www.gnome-look.org/p/999440/
Source0:        140649-MinecraftCursorTheme-%{version}.tar.gz
BuildArch:      noarch

%description
Uses icons from Minecraft.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a minecraft/cursors $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cat > $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}/cursor.theme <<EOF
[Icon Theme]
Name=Minecraft
Comment=Minecraft Cursor Theme
Example=left_ptr
Inherits=default
EOF

%files 
%doc README
%{_datadir}/icons/%{theme_name}

%changelog
* Sun Nov 7 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
