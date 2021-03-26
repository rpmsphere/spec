%define real_name circular-application-menu

Name:		cam
Version:	0svn52
Release:	1
Summary:	circular application menu for GNOME
Group:		User Interface/Desktops
License:	GPL
URL:		http://code.google.com/p/%{real_name}/
Source:		%{real_name}-%{version}.tar.gz
BuildRequires:  gnome-menus-devel
BuildRequires:  gtk2-devel >= 2.12, gnome-vfs2-devel
Requires:	gtk2 >= 2.12, gnome-vfs2
#BuildRequires:  compiz-devel
#Requires:       compiz

%description
This is a circular-application-menu (C-A-M) prototype mirroring the
same structure as the existing application menu for the GNOME desktop.

%prep
%setup -q -n %{real_name}
sed -i 's/gnome-desktop-2.0/gnome-desktop-2.0 libgnomeui-2.0 gio-unix-2.0/' Makefile
sed -i 's|gnome-menus/|gnome-menus-3.0/|' src/*

%build
%__make

%install
%__rm -rf %{buildroot}
%__install -Dm755 circular-main-menu %{buildroot}%{_bindir}/%{name}
%__install -Dm644 %{real_name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir -p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=C.A.M.
Name[zh_TW]=環狀選單
Comment=Circular Application Menu
Comment[zh_TW]=環狀應用軟體選單
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;System;Utility;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0svn52
- Rebuild for Fedora
