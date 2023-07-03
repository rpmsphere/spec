%global _name skyscene

Name:           skyscene-backgrounds
Version:        20100525
Release:        4.1
Summary:        Skyscene animated wallpaper
Group:          User Interface/Desktops
License:        CC-BY
Source0:        https://dl.dropboxusercontent.com/u/2845888/skyscene.tar.gz
URL:            https://www.gnome-look.org/p/1063044/
Source1:        %{name}.xml
BuildArch:      noarch

%description
This is an animated wallpaper that changes as the day goes by.
The foreground is a photo I took of the hill overlooking Buckeye hot springs,
just outside of Bridgeport, CA. The various skies are from pictures I took in
the desert and the stars are from the Hubble Space Telescope (sorry, I can't
recall the specific image). https://hubblesite.org/gallery/album/entire/

%prep
%setup -q -n %{_name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/%{_name}
cp sky.xml *.jpg $RPM_BUILD_ROOT/%{_datadir}/backgrounds/%{_name}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%files
%{_datadir}/backgrounds/%{_name}
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Fri Oct 07 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20100525
- Rebuilt for Fedora
