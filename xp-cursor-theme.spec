%define theme_name XP

Summary: XP theme for cursor
Name: xp-cursor-theme
Version: 1.0
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source: xp_cursor.tar.gz
BuildArch: noarch

%description
Cursor XP created by uplink.

%prep
%setup -q -n xp

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a cursors index.theme %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
