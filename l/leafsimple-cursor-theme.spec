Name:           leafsimple-cursor-theme
Version:        1.0.0
Release:        3.1
Summary:        leafSimple X11 Mouse Cursor theme
Group:          System/X11/Icons
License:        Creative Commons by-nc
URL:            https://www.box-look.org/p/999912/
Source0:        https://dl.opendesktop.org/api/files/download/id/1460735239/164200-leafSimple.tgz
BuildArch:      noarch

%description
leafSimple is a X11 mouse theme multisized to 24, 32, 40, 48, 56 and 64 pixels,
for both: righties and lefties. It is dedicated to Linux Mint Petra with Cinnamon
as desktop environment. I want to thank Brahim Salem, who is a member of this
website, for his contribution with ideas for the conclusion of this project.

%prep
%setup -q -n leafSimple

%build

%install
install -d %{buildroot}%{_datadir}/icons/leafSimple
cp -a cursors %{buildroot}%{_datadir}/icons/leafSimple
install -m644 index.theme %{buildroot}%{_datadir}/icons/leafSimple/cursor.theme

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/leafSimple

%changelog
* Tue Aug 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuild for Fedora
