%define theme_name Britanzan

Summary: British Library icon theme
Name: britanzan-icon-theme
Version: 3
Release: 2.1
License: freeware
Group: User Interface/Desktops
URL: http://samantha-wright.deviantart.com/art/British-Library-for-Gnome-285573042
Source0: http://orig00.deviantart.net/2c83/f/2012/048/9/c/britanzan_by_samantha_wright-d4q0tki.zip
#Source1: 
BuildArch: noarch

%description
Gnome version of Icons of the Library contributed by... actually I forget.
I'm really really sorry. Full credit for the mod implementation to whoever
that was. Named "Britanzan" by the creator, based on the "Balanzan" theme.

%prep
%setup -q -n britanzan
rm index.theme~

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Mon Oct 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3
- Rebuilt for Fedora
