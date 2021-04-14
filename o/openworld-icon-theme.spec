%global theme_name OpenWorld

Name:		openworld-icon-theme
Version:	20060508
Release:	2.1
Summary:	%{theme_name} icon theme
Group:		System/GUI/GNOME
License:	CDDL open source
URL:		https://blogs.oracle.com/chandan/entry/openworld_icon_theme
Source0:	ICON-OpenWorld.tar.bz2
BuildArch:      noarch

%description
All icons are original and they do not intend to copy icons from any other
operating system or icon theme.

%prep
%setup -q -c

%build

%install
install -d %{buildroot}%{_datadir}/icons
cp -a %{theme_name} %{buildroot}%{_datadir}/icons

%files
%doc %{theme_name}/*.txt
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Jul 07 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20060508
- Rebuilt for Fedora
