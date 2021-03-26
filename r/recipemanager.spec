%define _date 20071108

Name:           recipemanager
Version:        0.3
Release:        4.1
Summary:        Easily manage your recipes
Group:          Applications/Productivity
License:        GPLv3+
URL:            http://www.recipemanager.org/
Source0:        http://www.recipemanager.org/files/%{name}-%{_date}.tar.bz2
Requires:	pygtk2, gnome-python2-gconf, gnome-python2-gnomevfs, dbus-python
Requires:       avahi-ui-tools
BuildArch:	noarch

%description
* Simple, user-friendly interface
* Powerful live searching
* Print recipes and recipe books
* Themeable recipe card view
* Browse and share recipes with others

%prep
%setup -q -n %{name}-%{_date}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/bash
cd %{_datadir}/%{name}
python2 %{name}
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Recipe Manager
Comment=Easily manage your recipes
Icon=%{_datadir}/%{name}/%{name}.svg
Exec=%{name}
Terminal=false
Type=Application
Categories=Office;
StartupNotify=false
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Thu Apr 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
