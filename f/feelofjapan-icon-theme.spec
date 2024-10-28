%define theme_name Feel-of-Japan

Summary: %{theme_name} icon theme
Name: feelofjapan-icon-theme
Version: 0.1
Release: 4.1
License: free
Group: User Interface/Desktops
URL: https://www.gnome-look.org/content/show.php/Feel+of+Japan?content=83828
Source0: https://www.mediafire.com/download/0k9x85g2d80fk0k/Feel-of-Japan.tar.gz
Source1: https://dl.opendesktop.org/api/files/download/id/1460808367/158335-Japanese_Room.jpg
BuildArch: noarch

%description
An icon set for linux (GNOME) based on :
* Buuf-Deuce >> icons by mattahan
* Hinode by dunedhel
* and of course, Yoritsuki by HYBRIDWORKS
With Japanese_Room.jpg by palko

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Aug 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
