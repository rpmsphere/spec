Name: webapp-manager
Summary: Web Application Manager
Version: 1.1.8
Release: 2
Group: admin
License: Free Software
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils
#Requires: python3
#Requires: python3-gi
#Requires: python3-configobj
Requires: python3-setproctitle
Requires: python3-tldextract
Requires: xapps
#Requires: dconf-gsettings-backend
#Requires: gsettings-backend

%description
Launch websites as if they were apps.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}

%files
%{_bindir}/%{name}
/usr/lib/%{name}
%{_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.x.%{name}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/%{name}
%{_datadir}/desktop-directories/webapps-webapps.directory
%{_datadir}/icons/hicolor/scalable/categories/applications-webapps.svg

%changelog
* Wed Sep 20 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.8-2
- Rebuilt for Fedora
