%define theme_name Shaded

Summary:        Shaded GTK theme
Name:           shaded-gtk-theme
Version:        20080601
Release:        34.1
License:        freeware
Group:          User Interface/Desktops
URL:            http://msart2k.deviantart.com/art/shaded-87330082
Source0:        shaded-gtk2.tar.gz
Source1:        %{theme_name}-index.theme
Source2:        color-777777.jpg
Requires:       gtk-murrine-engine
BuildArch:      noarch
Requires:       notitle2-metacity-theme
Requires:       areao43-icon-theme
Requires:       obsidian-cursor-theme

%description
Shaded theme for gtk2, first release!

%prep
%setup -q -n shaded
cp %{SOURCE1} index.theme
cp %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/themes/%{theme_name}

%changelog
* Fri Jun 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20080601
- Rebuilt for Fedora
