%global theme_name nouveGnome

Name:		nouvegnome-icon-theme
Version:	0.0.1
Release:	5.1
Summary:	%{theme_name} icon theme
Group:		System/GUI/GNOME
License:	free
URL:		https://tsujan.deviantart.com/art/nouveGnome-301614547
#URL:            https://www.gnome-look.org/p/1015824/
#Source0:        https://www.deviantart.com/download/301614547/nouvegnome_by_tsujan-d4zkn9v.7z
Source0:	%{theme_name}.tgz
#Source1:        https://www.deviantart.com/download/300365158/nouvegnomegray_by_tsujan-d4ytv8m.7z
Source1:        %{theme_name}Gray.tgz
Source2:        https://dl.dropboxusercontent.com/s/1u3uxya8z1m6kng/%{theme_name}Steel.tgz
BuildArch:      noarch
BuildRequires:  ghostscript-core ImageMagick

%description
nouveGnome & nouveGnomeGray by tsujan.
nouveGnomeSteel by keithhedger.

%prep
%setup -q -c -a 1 -a 2
mogrify -resize 256x256 nouveGnomeSteel/scalable/filesystems/*.png

%build

%install
install -d %{buildroot}%{_datadir}/icons
cp -a * %{buildroot}%{_datadir}/icons

%files
%{_datadir}/icons/%{theme_name}*

%changelog
* Tue Jul 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuilt for Fedora
