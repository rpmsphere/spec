%define theme_name VAEW

Summary: Virus Are EveryWhere theme Suite
Name: vaew-theme
Version: 2.2
Release: 11.1
License: GPLv2+
Group: User Interface/Desktops
Source0: https://rsm.website/software/gnu-linux/repository/pool/main/g/gtk-theme-vaew/gtk-theme-vaew_2.2~0_all.deb
Source1: https://tubeguy.org/puppybg/Honeycomb_wallpaper-1600x1200.jpg
Source2: VAEW-index.theme
URL: https://rsm.website/software/gnu-linux/software/gtk-theme-vaew/
BuildArch: noarch
Requires: golden3d-cursor-theme

%description
Virus are everywhere is a dark Gtk 2.x and 3.x theme. It displays some privative formats with an virus image.

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
mkdir -p %{buildroot}
tar xf data.tar.xz -C %{buildroot}
mv %{buildroot}%{_datadir}/doc/gtk-theme-vaew %{buildroot}%{_datadir}/doc/%{name}
mv %{buildroot}%{_datadir}/themes/virus_are_everywhere %{buildroot}%{_datadir}/themes/%{theme_name}
mv %{buildroot}%{_datadir}/icons/virus_are_everywhere %{buildroot}%{_datadir}/icons/%{theme_name}
cp %{SOURCE1} %{buildroot}%{_datadir}/themes/%{theme_name}/backgrounds/
cp %{SOURCE2} %{buildroot}%{_datadir}/themes/%{theme_name}/index.theme
sed -i -e 's|&gt);|\&gt;)|' -e 's|& |\&amp; |' -e 's|&#194;||' %{buildroot}%{_datadir}/themes/%{theme_name}/metacity-1/metacity-theme-?.xml

%files
%{_datadir}/doc/%{name}
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/%{theme_name}

%changelog
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
