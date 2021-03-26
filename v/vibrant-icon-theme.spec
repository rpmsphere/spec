Summary: Vibrant icon theme
Name: vibrant-icon-theme
Version: 6.4
Release: 10.1
BuildArch: noarch
License: LGPL2.1
Group: User Interface/Desktops
Source0: vibrant-%{version}.tar.bz2

%description
This package contains Vibrant style cursors and icons.

%prep
%setup -q -c
find . -type f -name "*~" -delete -print

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons
cp -a vibrant $RPM_BUILD_ROOT/%{_datadir}/icons/Vibrant
ln -sf gnome-terminal.svg %{buildroot}%{_datadir}/icons/Vibrant/scalable/apps/terminal.svg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/Vibrant

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 6.4
- Rebuild for Fedora
* Thu Jul 29 2010 awafaa@opensuse.org
- Remove unwanted backup files (~)
* Tue Jul 13 2010 awafaa@opensuse.org
- Initial import for openSUSE version 6.4
