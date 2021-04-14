%define theme_name Ubo

Summary: %{theme_name} icon theme
Name: ubo-icon-theme
Version: 0.1alpha
Release: 11.1
License: Artistic 2.0
Group: User Interface/Desktops
URL: http://pen-art.ru/icons.html
Source0: http://pen-art.ru/downloads/icons/ubo-icons-0.1alpha.tar.gz
Source1: ubo-home-1920x1200.png
BuildArch: noarch

%description
My Icons theme - Not glamorous, not glossy, drawn with ballpoint pen,
scanned and colored in GIMP.

There is still much work to support many applications and major DE.
Theme still has the status "work in progress ", but now you can try it
on your desktop.

%prep
%setup -q -n ubo-icons-%{version}
sed -i 's|Example=preferences-desktop-icons|Example=folder|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}*

%changelog
* Wed May 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1alpha
- Rebuilt for Fedora
