Name:           linuxcommunity-backgrounds
Version:        20091211
Release:        8.1
Summary:        Linux Community backgrounds
Group:          User Interface/Desktops
License:        CC-BY-SA
URL:            http://www.linux-community.de/Internal/Artikel/Online-Artikel/LC-Adventsaktion-Freie-Hintergrundbilder-zum-Download
Source0:        http://www.linux-community.de/content/download/111923/888824/file/lc-wallpaper-bundle.tar.gz
Source1:        linuxcommunity-backgrounds.xml
BuildArch:      noarch

%description
This package contains 12 desktop backgrounds collected by Linux Community.

%prep
%setup -q -n lc-wallpaper-bundle

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/linuxcommunity
cp -a *.jpg $RPM_BUILD_ROOT/%{_datadir}/backgrounds/linuxcommunity
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc download-urls
%{_datadir}/backgrounds/linuxcommunity
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Wed Mar 06 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20091211
- Rebuilt for Fedora
