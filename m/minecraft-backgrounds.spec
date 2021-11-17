Name:           minecraft-backgrounds
Version:        2021
Release:        1
Summary:        Minecraft Backgrounds
Group:          User Interface/Desktop
License:        freeware
Source0:        minecraft-backgrounds.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
This package contains desktop backgrounds from Minecraft.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/minecraft
cp * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/minecraft
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/backgrounds/minecraft
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Sun Sep 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2021
- Rebuilt for Fedora
