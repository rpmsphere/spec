Name:           moemoe-backgrounds
Version:        2011
Release:        9.1
Summary:        Moe-Moe wallpapers for moebuntu
Group:          User Interface/Desktops
License:        freeware
URL:            http://photozou.jp/photo/top/1101860
Source0:        moemoe-wallpapers.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
Peace Sign Girl's illustration was drawn by TOY.
Eva chin's illustration is provided by Sakae.
Hinomoto Oniko-tan's illustration is provided by Sakae.
Nukumimi Yukarin's illustration is provided by Kitsunegami.
Ohimesama Fūmi Hina's illustration is provided by Kitsunegami.
Angel's illustration is provided by saki_12.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/moemoe
cp -a * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/moemoe
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/backgrounds/moemoe
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Mon Jul 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2011
- Rebuilt for Fedora
