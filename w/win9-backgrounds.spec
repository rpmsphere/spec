Name:           win9-backgrounds
Version:        2014
Release:        1.1
Summary:        Win 9 backgrounds
Group:          User Interface/Desktop
License:        freeware
Source0:        win9-backgrounds.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
This package contains desktop backgrounds as for Win 9.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/win9
cp * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/win9
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%files
%{_datadir}/backgrounds/win9
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Fri Oct 17 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2014
- Rebuilt for Fedora
