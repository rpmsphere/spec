Name:           paranoid-backgrounds
Version:        20090111
Release:        7.1
Summary:        Paranoid backgrounds
Group:          User Interface/Desktops
License:        freeware
URL:            http://kon.deviantart.com/art/Paranoid-109245740
Source0:        Paranoid_by_kon.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
New wallpapers by kon.
Six color variation inside at 2560x1600.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/Paranoid
rm -f paranoid_preview.png
cp -a * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/Paranoid
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/backgrounds/Paranoid
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Mon Jul 04 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20090111
- Rebuild for Fedora
