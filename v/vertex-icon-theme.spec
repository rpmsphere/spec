%define theme_name Vertex

Summary:        A Gnome icon theme to match the Vertex Gtk theme
Name:           vertex-icon-theme
Version:        20150507
Release:        2.1
License:        GPL2+
Group:          User Interface/Desktops
URL:            https://github.com/horst3180/vertex-icons
Source0:        vertex-icons-master.zip
BuildArch:      noarch

%description
The Vertex icon theme is designed to go well together with the Vertex Gtk theme.
At the moment it includes mainly icons for folders and mimetypes.

%prep
%setup -q -n vertex-icons-master

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Apr 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20150507
- Rebuilt for Fedora
