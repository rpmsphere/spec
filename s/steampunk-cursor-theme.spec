%global theme_name SteamPunk

Name:           steampunk-cursor-theme
Version:        20110425
Release:        2.1
Summary:        %{theme_name} X11 Mouse Cursor theme
Group:          System/X11/Icons
License:        GPL
URL:            https://www.gnome-look.org/p/999963/
Source0:        https://dl.opendesktop.org/api/files/download/id/1460735338/140755-SteamPunk.tar.gz
BuildArch:      noarch

%description
Original theme by Vampothika. Thanks to Vampothika, allowed me to convert this pointer.
For the conversion I used the wonderful script by coolwanglu cfx2xc (CursorFX converter!!!)

%prep
%setup -q -n %{theme_name}

%build

%install
install -d %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a * %{buildroot}%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Tue Oct 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20110425
- Rebuilt for Fedora
