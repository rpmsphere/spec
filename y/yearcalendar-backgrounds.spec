Name:           yearcalendar-backgrounds
Version:        2017
Release:        3.1
Summary:        Whole year calendar backgrounds
Group:          User Interface/Desktops
License:        free
Source0:        yearcalendar-backgrounds.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
https://www.publicdomainpictures.net/download-picture.php?adresar=190000&soubor=2017-calendar-with-dandelion.jpg
https://www.shinetalks.com/wp-content/uploads/2016/12/happy-new-year-2017-calendar-1.jpg
https://www.2017newyearseve.com/wp-content/uploads/2016/08/2017-happy-new-year-calendar-b.jpg

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/yearcalendar
cp -a * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/yearcalendar
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%files
%{_datadir}/backgrounds/yearcalendar
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Wed Jan 04 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2017
- Rebuilt for Fedora
