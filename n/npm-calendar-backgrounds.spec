Name:           npm-calendar-backgrounds
Version:        2020
Release:        1
Summary:        National Palace Meseum calendar backgrounds
Group:          User Interface/Desktops
License:        freeware
Source0:        %{name}-%{version}.zip
URL:            https://www.npm.gov.tw/zh-TW/Article.aspx?sNo=03001536
Source1:        %{name}.xml
Source2:        npm-calendar-default.xml
BuildArch:      noarch

%description
Taiwan bi-monthly calendar from National Palace Meseum.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/npm-calendar
cp -a * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/npm-calendar
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/backgrounds/npm-calendar/default.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%files
%{_datadir}/backgrounds/npm-calendar
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Thu Nov 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2020
- Rebuilt for Fedora
