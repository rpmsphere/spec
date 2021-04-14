Name:           angrybirds-backgrounds
Version:        20110719
Release:        13.1
Summary:        AngryBirds related backgrounds
Group:          User Interface/Desktops
License:        freeware
URL:            http://www.rovio.com/
Source0:        angrybirds-backgrounds.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
deviantart-bradsmith20.jpg
deviantart-dearcane.jpg
deviantart-fairytalesartist.jpg
deviantart-the_bambookazee.jpg

elance-katie_peppers.jpg
walops-pig.jpg
zero_lives-genus_aves_iratus.jpg

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/angrybirds
cp -a * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/angrybirds
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/backgrounds/angrybirds
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Tue Jul 19 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20110719
- Rebuilt for Fedora
