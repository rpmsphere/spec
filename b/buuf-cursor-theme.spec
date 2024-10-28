%define theme_name BuufCursor

Summary:        Buuf cursor theme
Name:           buuf-cursor-theme
Version:        20061223
Release:        3.1
License:        freeware
Group:          User Interface/Desktops
URL:            https://gnome-look.org/content/show.php/Buuf+Cursor?content=74495
Source0:        Buuf.tar.gz
BuildArch:      noarch

%description
This is only a port. Original work done by aroche: https://www.skinbase.org/profile.php?uname=aroche
This is the only thing I needed to match the Buuf stuff. Permission is inside the file. Hope you like it!!!

%prep
%setup -q -n cursor-theme
cat > index.theme << EOF
[Icon Theme]
Name=Buuf Cursor
Example=left_ptr
EOF

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Fri Jun 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20061223
- Rebuilt for Fedora
