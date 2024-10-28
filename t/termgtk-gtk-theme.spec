%define theme_name termGTK

Summary:        Dead simple GTK theme
Name:           termgtk-gtk-theme
Version:        20100924
Release:        8.1
License:        CC by-nc-sa
Group:          User Interface/Desktops
URL:            https://rent0n86.deviantart.com/art/termGTK-169819259
Source0:        https://www.deviantart.com/download/169819259/termgtk_by_rent0n86-d2t3tdn.zip
Source1:        %{theme_name}-index.theme
Source2:        https://www.deviantart.com/download/76699998/leaf_skin_by_epheus.jpg
BuildArch:      noarch
Requires:       notitleslim-metacity-theme
Requires:       retropixel-icon-theme
Requires:       vienna3-cursor-theme

%description
It aims to stay out of the way and tries to resemble a cli environment,
so that you won't notice so much you're using a gtk app.
I made it for myself and I didn't test it too much as I'm not using many
gtk apps at the moment, but it seems to work fine.

%prep
%setup -q -n %{theme_name}
cp %{SOURCE1} index.theme
cp %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files 
%{_datadir}/themes/%{theme_name}

%changelog
* Mon Sep 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20100924
- Rebuilt for Fedora
