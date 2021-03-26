Name:           ios4mac-backgrounds
Version:        2011
Release:        9.1
Summary:        iOS for Mac backgrounds
Group:          User Interface/Desktop
License:        freeware
Source0:        http://www.jeanmarcdenis.me/goodies/iOS4Mac.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
This package contains desktop backgrounds as on iPAD.

%prep
%setup -q -c
rm -f ios4mac-1280x800 ios4mac-2560x1600.png

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/ios4mac
cp *.png $RPM_BUILD_ROOT/%{_datadir}/backgrounds/ios4mac
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/backgrounds/ios4mac
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Mon May 23 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2011
- Rebuild for Fedora
