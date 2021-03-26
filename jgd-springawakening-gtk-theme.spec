%define theme_name JGD-SpringAwakening

Summary:        JGD Spring Awakening GTK theme
Name:           jgd-springawakening-gtk-theme
Version:        17.10.23
Release:        4.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://www.gnome-look.org/p/1015172/
Source0:        https://raw.githubusercontent.com/jgpws/jgd-spring-awakening/master/downloads/jgd-springawakening-10-23-17.tar.gz
Source1:        %{theme_name}-index.theme
Source2:        43331344-1920x1080.jpg
BuildArch:      noarch
Recommends:     fitts-natural-metacity-theme
Recommends:     gartoonredux-icon-theme
Recommends:     leafsimple-cursor-theme

%description
The JGD-Spring Awakening GTK+ 2 theme to go with its Openbox theme, which is
included in this package. It requires the Murrine theme engine.

%prep
%setup -q -n %{theme_name}
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
* Wed Jan 10 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 17.10.23
- Rebuild for Fedora
