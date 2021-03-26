Name:           linuxlexos-backgrounds
Version:        1.0
Release:        3.1
Summary:        A collection of wallpapers for LinuxLexOS
Group:          User Interface/Desktops
License:        Creative Commons by-nc-nd
URL:            http://gnome-look.org/content/show.php/?content=145168
Source0:        http://linuxlex.cz/phocadownload/linuxlexos-backgrounds_1.0_all.deb
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
Wallpaper for LinuxLexOS, DEB files (debian, ubuntu).

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
tar xf data.tar.gz -C $RPM_BUILD_ROOT
cp -a $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties $RPM_BUILD_ROOT%{_datadir}/mate-background-properties

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/doc/linuxlexos-backgrounds/changelog.Debian.gz
%{_datadir}/backgrounds/linuxlex
%{_datadir}/*-background-properties/linuxlex-wallpapers.xml

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
