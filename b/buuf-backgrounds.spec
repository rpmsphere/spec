Name:           buuf-backgrounds
Version:        20110707
Release:        6.1
Summary:        Buuf backgrounds
Group:          User Interface/Desktops
License:        CC-BY-NC-SA
URL:            https://mattahan.deviantart.com/
Source0:        buuf-backgrounds.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
Must...replenish...my strength...Birdman!
(https://mattahan.deviantart.com/art/Some-clouds-sun-39780964)

I guess it depends on what icon you put on the other side.
(https://mattahan.deviantart.com/art/Why-42200754)

Let's go inside my astroplane.
(https://mattahan.deviantart.com/art/Bring-the-Pain-39781904)

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/buuf
cp -a * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/buuf
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%files
%{_datadir}/backgrounds/buuf
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Thu Jul 07 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20110707
- Rebuilt for Fedora
