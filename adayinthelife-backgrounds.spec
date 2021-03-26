%global _name aDayInThelife

Name:           adayinthelife-backgrounds
Version:        2016
Release:        8.1
Summary:        A Day in the Life backgrounds
Group:          User Interface/Desktops
License:        freeware
Source0:        a_day_in_the_life_by_barid42-d3dzbcc.7z
URL:            http://barid42.deviantart.com/art/A-Day-in-the-Life-204881196
Source1:        %{name}.xml
Source2:        %{_name}-default.xml
BuildArch:      noarch
BuildRequires:  p7zip

%description
A changing wallpaper for Linux. Size is 1366x768.

%prep
%setup -q -n %{_name}_barid42

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/%{_name}
cp -a *.png $RPM_BUILD_ROOT/%{_datadir}/backgrounds/%{_name}
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/backgrounds/%{_name}/default.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%files
%{_datadir}/backgrounds/%{_name}
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2016
- Rebuild for Fedora
