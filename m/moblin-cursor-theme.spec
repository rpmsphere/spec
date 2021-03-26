%define theme_name Moblin

Summary: %{theme_name} cursor theme
Name: moblin-cursor-theme
Version: 0.3
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1460734787/113721-moblin-cursor-theme-0.3.tar.gz
URL: https://www.gnome-look.org/p/999723/
BuildArch: noarch

%description
Taken from http://git.moblin.org/cgit.cgi/moblin-cursor-theme/

%prep
%setup -q
mv index.theme cursor.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}/*

%changelog
* Thu Oct 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
