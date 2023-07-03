Summary: RADial Menu
Name: radmenu
Version: 2009.3.28
Release: 7.1
Source0: https://fraggod.net/oss/projects/rad_menu.py
Source1: https://fraggod.net/oss/projects/rad_menu.cfg
License: unknown
URL: https://fraggod.net/code/rad_menu
Group: Desktop/User interface
BuildArch: noarch
Requires: pygtk2

%description
Rad name might be quite self-explanatory (in a _rad_ way)), but actually just
stands for "radial" and also might be borrowed from another standalone menu
I've used - "ratmenu" (along w/ the ratpoison wm).

%prep
%setup -T -c

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/%{name}
cp %{SOURCE0} %{SOURCE1} %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec python rad_menu.py
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2009.3.28
- Rebuilt for Fedora
