Name:		ezgo-menu
Version:	0.1
Release:	1
Summary:	Common menu for Ezgo
License:	GPLv2
Group:		System
Source:		http://of.openfoundry.org/download_path/ezgomenu/%{version}/%{name}.tgz
URL:		http://of.openfoundry.org/projects/928
Vendor:		ericsun, yurenju
BuildArch:	noarch

%description
The purpose of ezgo-menu is to build a menu for EzGo system.
You could understand the function of software just through
it's name on this menu suitable for every Linux distribution.

%prep
%setup -q -n %{name}

%build

%install
%__rm -rf %{buildroot}
##%__make DESTDIR=%{buildroot} install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a * %{buildroot}%{_datadir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
MENU_DIR=\$HOME/.config/menus/
APP_DIR=\$HOME/.local/share/applications/
mkdir -p \$MENU_DIR \$APP_DIR

cp -f files/*.menu \$MENU_DIR
cp -f files/desktop/*.desktop \$APP_DIR
EOF

%clean
%__rm -rf %{buildroot}

%files
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%changelog
* Tue Feb 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
