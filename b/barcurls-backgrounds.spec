Name:           barcurls-backgrounds
Version:        12.3
Release:        5.1
Summary:        Extra wallpapers for openSUSE 12.3
Group:          User Interface/Desktop
License:        CC-BY-SA
Source0:        wallpapers123.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
This is a collection of extra wallpapers for openSUSE 12.3.

%prep
%setup -q -n wallpapers123

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/barcurls
cp * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/barcurls
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/backgrounds/barcurls
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Sun Mar 17 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 12.3
- Rebuild for Fedora
* Tue Jan 22 2013 maoyaotang
- Initial package
